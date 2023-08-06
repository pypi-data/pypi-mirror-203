import collections
import ctypes
import itertools
import math
import struct
import sys
from typing import Any


def read_memory_from_address(id_v: int, byterange: int = 100) -> list:
    r"""
    Reads memory from a given address and returns a list of tuples containing the address, value, and hexadecimal value.

    Args:
        id_v (int): The starting address to read memory from. Example: x=(2,4,3)  read_memory_from_address(id(x))
        byterange (int, optional): The number of bytes to read from the starting address. Defaults to 100.

    Returns:
        list: A list of tuples containing the address, value, and hexadecimal value.

    Raises:
        None
    """
    results = []
    id_v2 = id_v
    for u in range(id_v2, id_v2 + byterange):
        try:
            q = ctypes.c_voidp.from_address(u).value
            results.append((u, q, hex(q)))
        except Exception as fe:
            continue
    return results


def iter_batch(iterable, n):
    r"""
    Batch data into sub-iterators of length n. The last batch may be shorter.

    Args:
        iterable (Iterable): The iterable to be batched.
        n (int): The size of each batch.

    Raises:
        ValueError: If n is less than 1.

    Yields:
        Iterator: An iterator containing the batched data.
    """
    # https://stackoverflow.com/a/74997058/15096247
    _consume = collections.deque(maxlen=0).extend
    "Batch data into sub-iterators of length n. The last batch may be shorter."
    # batched_it('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError("n must be at least one")
    n -= (
        1  # First element pulled for us, pre-decrement n so we don't redo it every loop
    )
    it = iter(iterable)
    for first_el in it:
        chunk_it = itertools.islice(it, n)
        try:
            yield itertools.chain((first_el,), chunk_it)
        finally:
            _consume(chunk_it)  # Efficiently consume any elements caller didn't consume


def tuplechanger(
    tutu: Any, tuindex: None, newvalue: Any, offsetbytes: int = 0
) -> None:
    """
    Changes the value of a tuple element at a given index.

    Args:
        tutu (Any): The tuple to modify.
        tuindex (None): The index of the element to modify.
        newvalue (Any): The new value to set at the given index.
        offsetbytes (int, optional): The number of bytes to offset the memory address of the tuple element. Defaults to 0.

    Raises:
        ValueError: If there is an error accessing the value.

    Returns:
        None
    """
    neg = False
    isfloat = False
    isint = False
    islastelement = False
    try:
        islastelement = len(tutu) == tuindex + 1
        tutuindex = tutu[tuindex]
        sizetoread = sys.getsizeof(tutu[tuindex])
        idtutu = id(tutu)
        idtutue = id(tutu[tuindex])
    except Exception:
        tutuindex = tutu
        sizetoread = sys.getsizeof(tutu)
        idtutu = id(tutu)
        idtutue = id(tutu)
    oldstringval = ""
    newstringval = ""

    if isinstance(newvalue, int) and str(newvalue) not in ["True", "False"]:
        if newvalue < 0:
            newvalue = struct.unpack("<Q", struct.pack("<q", newvalue))[0]
            tutuindex = struct.unpack("<Q", struct.pack("<q", tutuindex))[0] + 1
            neg = True
        else:
            newvalue = struct.unpack("<Q", struct.pack("<q", newvalue))[0]  # [0]
            tutuindex = struct.unpack("<Q", struct.pack("<q", tutuindex))[0]  # [0] + 1
            isint = True

    elif newvalue in [True, False]:
        ept = ctypes.c_longlong.from_address(idtutu + (3 + tuindex) * 8)
        if newvalue:
            ept.value = id(True)
        else:
            ept.value = id(False)
        return
    elif isinstance(newvalue, str):
        oldstringval = tutuindex
        newstringval = newvalue
        newvalue = newvalue[:8]
        tutuindex = tutuindex[:8]
        newvalue = sum(
            [
                x * (16**i)
                for i, x in enumerate(bytearray(newvalue.encode("utf-16-le")))
            ]
        )
        tutuindex = sum(
            [
                x * (16**i)
                for i, x in enumerate(bytearray(tutuindex.encode("utf-16-le")))
            ]
        )

    elif isinstance(newvalue, float):
        newvalue = struct.unpack("<Q", struct.pack("<d", newvalue))[0]
        tutuindex = struct.unpack("<Q", struct.pack("<d", tutuindex))[0]
        isfloat = True

    oldnumberh = (
        "0x"
        + "".join(
            reversed([hex(x)[2:].zfill(2) for x in tutuindex.to_bytes(8, "little")])
        ).lstrip("0")
        + (25 * "0")
    )[:25]
    addtochange = -1
    hundby = read_memory_from_address(
        id_v=idtutue + offsetbytes, byterange=(sizetoread * 1) - offsetbytes
    )
    for h in hundby:
        a = (h[2] + (24 * "0"))[:24]
        b = oldnumberh[:24]
        if a == b:
            addtochange = h[0]
            break
    if addtochange == -1:
        raise ValueError("Error accessing the value!")
    vala = list(
        reversed(
            [
                int(a, base=16)
                for a in (
                    [
                        f.zfill(2)
                        for f in (
                            reversed(
                                [
                                    q
                                    for q in (
                                        reversed(
                                            (
                                                [
                                                    "".join(x).rstrip("0")
                                                    for x in [
                                                        list(x)
                                                        for x in (
                                                            iter_batch(
                                                                hex(newvalue)[2:].zfill(
                                                                    16
                                                                ),
                                                                2,
                                                            )
                                                        )
                                                    ]
                                                ]
                                            )
                                        )
                                    )
                                    if q
                                ]
                            )
                        )
                    ]
                    + (["00"] * 8)
                )[:8]
            ]
        )
    )
    if newstringval != "":
        buff = (ctypes.c_ulonglong * math.ceil(len(oldstringval) / 8)).from_address(
            addtochange
        )
        barr = bytearray(buff)

        vala = (
            [x for i, x in enumerate(newstringval.encode("utf-16-le")) if i % 2 == 0]
        ) + len(barr) * [32]
        valacheck = [
            len(barr) - i - 1
            for i, y in enumerate(list(itertools.takewhile(lambda x: x == 0, barr)))
        ]

        for i in list(reversed(range(len(barr)))):
            if i in valacheck:
                continue
            barr[i] = vala[i]

        ctypes.memmove(buff, bytes(barr), len(barr))
        barr = None
        buff = None

        return

    if neg:
        addtochange = addtochange + 1
    buff = (ctypes.c_ulonglong * 1).from_address(addtochange)
    barr = bytearray(buff)
    if neg:
        vala = list(reversed([255 - y + 1 if y != 255 else y for y in vala]))
    if isfloat:
        vala[-1] = vala[-1] * 16

    if isint:
        if newvalue < 255:
            vala = vala[1:] + [0]
    valacheck = reversed(
        [
            len(barr) - i - 1
            for i, y in enumerate(list(itertools.takewhile(lambda x: x == 0, barr)))
        ]
    )

    for i in list(reversed(range(len(barr)))):
        if islastelement:
            if i in valacheck:
                continue
        barr[i] = vala[i]

    ctypes.memmove(buff, bytes(barr), len(barr))
    buff = None
    barr = None


