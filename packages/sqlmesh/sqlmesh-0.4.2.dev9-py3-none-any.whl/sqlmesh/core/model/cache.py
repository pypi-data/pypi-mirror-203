
from __future__ import annotations

import typing as t
from pathlib import Path

from sqlglot import exp

from sqlmesh.core.model import Model
from sqlmesh.utils.date import TimeLike, to_timestamp
from sqlmesh.utils.pydantic import PydanticModel


class CacheEntry(PydanticModel):
    model: Model
    depends_on: t.List[str]
    contains_star_query: bool
    columns_to_types: t.Dict[str, exp.DataType]


class ModelCache:
    def __init__(self, path: Path, loader: t.Callable[[str], Model]):
        self.path = path
        self.loader = loader

    def get(self, name: str, last_updated: TimeLike) -> Model:
        model_cache_path = self.path / f"{name}__{to_timestamp(timestamp)}.json"
        if model_cache_path.exists():
            with open(model_cache_path, "r") as fd:
                cached_entry = CacheEntry.parse_raw(fd.read())

            model = cached_entry.model
            model._depends_on = set(cached_entry.depends_on)
            return model

        for obsolete_cache_file in self.path.glob(f"{name}__*.json"):
            obsolete_cache_file.unlink()

        loaded_model = self.loader(name)
        new_entry = CacheEntry(
            model=loaded_model,
            depends_on=list(loaded_model.depends_on),
            contains_star_query=loaded_model.contains_star_query,
            columns_to_types=loaded_model.columns_to_types,
        )

        with open(model_cache_path, "w") as fd:
            fd.write(new_entry.json())

        return loaded_model
