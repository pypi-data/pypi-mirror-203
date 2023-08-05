from bsb.morphologies import Morphology, Branch
from bsb._encoding import EncodedLabels
from bsb.exceptions import MorphologyRepositoryError, MissingMorphologyError
from bsb.storage.interfaces import (
    MorphologyRepository as IMorphologyRepository,
    StoredMorphology,
)
from .resource import Resource
import numpy as np
import json
import itertools

_root = "/morphologies"


class MorphologyRepository(Resource, IMorphologyRepository):
    def __init__(self, engine):
        super().__init__(engine, _root)

    def select(self, *selectors):
        all_loaders = self.all()
        selected = []
        for selector in selectors:
            selector.validate(all_loaders)
            selected.extend(filter(selector.pick, all_loaders))
        return selected

    def preload(self, name):
        return StoredMorphology(name, self._make_loader(name), self.get_meta(name))

    def _make_loader(self, name):
        def loader():
            return self.load(name)

        return loader

    def get_meta(self, name):
        with self._engine._read():
            with self._engine._handle("r") as repo:
                try:
                    meta = _meta(repo[f"{self._path}/{name}/"])
                except KeyError:
                    raise MissingMorphologyError(
                        f"`{self._engine.root}` contains no morphology named `{name}`."
                    ) from None
        meta["name"] = name
        return meta

    def all(self):
        return [self.preload(name) for name in self.keys()]

    def has(self, name):
        with self._engine._read():
            with self._engine._handle("r") as repo:
                return f"{self._path}/{name}" in repo

    def load(self, name):
        with self._engine._read():
            with self._engine._handle("r") as repo:
                try:
                    root = repo[f"{self._path}/{name}/"]
                except Exception:
                    raise MissingMorphologyError(
                        f"`{self._engine.root}` contains no morphology named `{name}`."
                    ) from None
                data = root["data"][()]
                points = data[:, :3].copy()
                radii = data[:, 3].copy()
                # Turns the forced JSON str keys back into ints
                labelsets = {
                    int(k): v for k, v in json.loads(root["data"].attrs["labels"]).items()
                }
                labels = EncodedLabels(
                    len(points), buffer=data[:, 4].astype(int), labels=labelsets
                )
                prop_names = root["data"].attrs["properties"]
                props = dict(zip(prop_names, np.rollaxis(data[:, 5:], 1)))
                parents = {-1: None}
                branch_id = itertools.count()
                roots = []
                ptr = 0
                for nptr, p in root["graph"][()]:
                    radii[ptr:nptr]
                    labels[ptr:nptr]
                    {k: v[ptr:nptr] for k, v in props.items()}
                    branch = Branch(
                        points[ptr:nptr],
                        radii[ptr:nptr],
                        labels[ptr:nptr],
                        {k: v[ptr:nptr] for k, v in props.items()},
                    )
                    parent = parents.get(p, None)
                    parents[next(branch_id)] = branch
                    if parent:
                        parent.attach_child(branch)
                    else:
                        roots.append(branch)
                    ptr = nptr
                meta = _meta(root)
                meta["name"] = name
                morpho = Morphology(
                    roots, meta, shared_buffers=(points, radii, labels, props)
                )
                assert morpho._check_shared(), "Morpho read with unshareable buffers"
                return morpho

    def save(self, name, morphology, overwrite=False):
        with self._engine._write():
            with self._engine._handle("a") as repo:
                me = repo[self._path]
                if self.has(name):
                    if overwrite:
                        self.remove(name)
                    else:
                        root = self._engine.root
                        raise MorphologyRepositoryError(
                            f"A morphology called '{name}' already exists in `{root}`."
                        )
                root = me.create_group(name)
                # Optimizing a morphology goes through the same steps as what is required
                # to save it to disk; plus, now the user's object is optimized :)
                morphology.optimize()
                branches = morphology.branches
                n_prop = len(morphology._shared._prop)
                data = np.empty((len(morphology), 5 + n_prop))
                data[:, :3] = morphology._shared._points
                data[:, 3] = morphology._shared._radii
                data[:, 4] = morphology._shared._labels
                for i, prop in enumerate(morphology._shared._prop.values()):
                    data[:, 5 + i] = prop
                dds = root.create_dataset("data", data=data)
                dds.attrs["labels"] = json.dumps(
                    {k: list(v) for k, v in morphology._shared._labels.labels.items()}
                )
                dds.attrs["properties"] = [*morphology._shared._prop.keys()]
                graph = np.empty((len(branches), 2))
                parents = {None: -1}
                ptr = 0
                for i, branch in enumerate(morphology.branches):
                    ptr += len(branch)
                    graph[i, 0] = ptr
                    graph[i, 1] = parents[branch.parent]
                    parents[branch] = i
                root.create_dataset("graph", data=graph, dtype=int)
                try:
                    for k, v in morphology.meta.items():
                        try:
                            root.attrs[f"meta:{k}"] = v if v is not None else np.nan
                        except Exception:
                            root.attrs[f"meta:json:{k}"] = json.dumps(v)
                except Exception:
                    raise MorphologyRepositoryError(
                        f"Trying to store invalid {type(v)} metadata '{k}' on `{name}`."
                    ) from None
                if len(morphology._shared._points):
                    root.attrs["meta:ldc"] = np.min(morphology._shared._points, axis=0)
                    root.attrs["meta:mdc"] = np.max(morphology._shared._points, axis=0)
                else:
                    root.attrs["meta:ldc"] = root.attrs["meta:mdc"] = np.nan
                meta = _meta(root)
        return StoredMorphology(name, lambda: morphology, meta)

    def remove(self, name):
        with self._engine._write():
            with self._engine._handle("a") as repo:
                try:
                    del repo[f"{self._path}/{name}"]
                except KeyError:
                    raise MorphologyRepositoryError(f"'{name}' doesn't exist.") from None


def _meta(group):
    # Filter out all the keys that start with `meta:`. Deserialize JSON values if key
    # starts with `meta:json:`.
    return dict(
        (k[10:], json.loads(v)) if k.startswith("meta:json:") else (k[5:], v)
        for k, v in group.attrs.items()
        if k.startswith("meta:")
    )
