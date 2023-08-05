from dataclasses import (
    dataclass,
)
from deprecated import (
    deprecated,
)
from fa_purity._bug import (
    LibraryBug,
)
from fa_purity.frozen import (
    freeze,
)
from fa_purity.json import (
    JsonObj as LegacyJsonObj,
    JsonValue as LegacyJsonValue,
)
from fa_purity.json_2.primitive import (
    JsonPrimitive,
    JsonPrimitiveFactory,
    JsonPrimitiveUnfolder,
    Primitive,
)
from fa_purity.json_2.value import (
    JsonObj,
    JsonValue,
    JsonValueFactory,
    UnfoldedFactory,
    Unfolder,
)
from fa_purity.utils import (
    raise_exception,
)


@deprecated("Temporal adapter for `json` -> `json_2` migration")  # type: ignore[misc]
@dataclass(frozen=True)
class LegacyAdapter:
    @classmethod
    def json_value(cls, legacy: LegacyJsonValue) -> JsonValue:
        return legacy.map(
            lambda p: JsonValue.from_primitive(
                JsonPrimitiveFactory.from_raw(p)
            ),
            lambda items: JsonValue.from_list(
                tuple(cls.json_value(i) for i in items)
            ),
            lambda d: JsonValue.from_json(
                freeze({k: cls.json_value(v) for k, v in d.items()})
            ),
        )

    @classmethod
    def json(cls, legacy: LegacyJsonObj) -> JsonObj:
        result = cls.json_value(LegacyJsonValue(legacy))
        return (
            Unfolder.to_json(result)
            .alt(lambda e: LibraryBug(e))
            .alt(raise_exception)
            .unwrap()
        )


__all__ = [
    "Primitive",
    "JsonPrimitive",
    "JsonPrimitiveFactory",
    "JsonPrimitiveUnfolder",
    "JsonValue",
    "JsonObj",
    "JsonValueFactory",
    "UnfoldedFactory",
    "Unfolder",
]
