from __future__ import annotations

from typing import List, Tuple, Union

from .group import Group, GroupId, GroupInfo
from .node_base import NestedGroup
from .properties.inputs.base_input import BaseInput

InputValue = Union[int, str]


def conditional_group(
    enum: int,
    condition: InputValue | List[str] | List[int] | Tuple[str, ...] | Tuple[int, ...],
):
    def ret(*items: BaseInput | NestedGroup) -> NestedGroup:
        info = GroupInfo(
            GroupId(-1),
            "conditional-enum",
            {"enum": enum, "conditions": (condition,) * len(items)},
        )
        return Group(info, list(items))

    return ret
