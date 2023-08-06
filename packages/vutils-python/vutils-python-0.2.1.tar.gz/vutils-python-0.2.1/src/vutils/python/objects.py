#
# File:    ./src/vutils/python/objects.py
# Author:  Jiří Kučera <sanczes AT gmail.com>
# Date:    2022-06-24 14:07:30 +0200
# Project: vutils-python: Python language tools
#
# SPDX-License-Identifier: MIT
#
"""Python objects utilities."""

from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    from collections.abc import Callable, Generator, MutableMapping
    from typing import TypeVar

    _KT = TypeVar("_KT")
    _VT = TypeVar("_VT")


def merge_data(dest: object, src: object) -> None:
    """
    Merge data from the source object to the destination object.

    :param dest: The destination object
    :param src: The source object
    :raises TypeError: when destination and source have different types
    """
    if not isinstance(dest, type(src)):
        raise TypeError("src and dest should have same types!")

    if isinstance(src, list):
        cast("list[object]", dest).extend(src)
    elif isinstance(src, set):
        cast("set[object]", dest).update(src)
    elif isinstance(src, dict):
        cast("dict[object, object]", dest).update(src)
    else:
        cast("dict[str, object]", dest.__dict__).update(
            cast("dict[str, object]", src.__dict__)
        )


def ensure_key(
    mapping: "MutableMapping[_KT, _VT]", key: "_KT", default: "_VT"
) -> None:
    """
    Ensure :arg:`mapping` has a :arg:`key` of the same type as :arg:`default`.

    :param mapping: The mapping
    :param key: The key
    :param default: The default value if :arg:`key` is not set
    :raises TypeError: when the value under the :arg:`key` cannot be converted
        to the type that has :arg:`default`

    If :arg:`key` is present in :arg:`mapping`, ensure the value is of a same
    type as :arg:`default`. Otherwise, store :arg:`default` to :arg:`mapping`
    under :arg:`key`.
    """
    typecls: "type[_VT]" = type(default)
    if key in mapping and not isinstance(mapping[key], typecls):
        # Raises TypeError if conversion fails
        mapping[key] = cast("Callable[[_VT], _VT]", typecls)(mapping[key])
    if key not in mapping:
        mapping[key] = default


def ensure_no_key(mapping: "MutableMapping[_KT, _VT]", key: "_KT") -> None:
    """
    Ensure :arg:`key` is not present in :arg:`mapping`.

    :param mapping: The mapping
    :param key: The key
    """
    if key in mapping:
        del mapping[key]


def flatten(obj: object) -> "Generator[object, None, None]":
    """
    Flatten :arg:`obj` recursively.

    :param obj: The object to be flattened
    :return: the generator that yields items from flattened :arg:`obj`

    If :arg:`obj` is :class:`list` or :class:`tuple`, yield items from
    :arg:`obj`'s flattened element. Otherwise, yield :arg:`obj`.
    """
    if isinstance(obj, (tuple, list)):
        for elem in obj:
            yield from flatten(elem)
    else:
        yield obj
