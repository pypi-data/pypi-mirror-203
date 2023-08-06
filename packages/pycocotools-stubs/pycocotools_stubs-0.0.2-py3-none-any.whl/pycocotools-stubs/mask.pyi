from typing import Any, overload

import numpy as np
import numpy.typing as npt

from .coco_types import EncodedRLE

def iou(dt: npt.NDArray[np.uint32] | list[float] | list[EncodedRLE],
        gt: npt.NDArray[np.uint32] | list[float] | list[EncodedRLE],
        pyiscrowd: list[int] | npt.NDArray[np.uint8]) -> list[Any] | npt.NDArray[np.float64]:
    """Compute intersection over union between masks."""
    ...

def merge(rleObjs: list[EncodedRLE], intersect: int = ...) -> EncodedRLE:
    """Compute union or intersection of encoded masks."""
    ...

@overload
def frPyObjects(pyobj: npt.NDArray[np.uint32] | list[list[int]] | list[EncodedRLE], h: int, w: int) -> list[EncodedRLE]:
    """Convert polygon, bbox, and uncompressed RLE to encoded RLE mask."""
    ...

@overload
def frPyObjects(pyobj: list[int] | EncodedRLE, h: int, w: int) -> EncodedRLE:
    ...

def encode(bimask: npt.NDArray[np.uint8]) -> EncodedRLE:
    ...

def decode(rleObjs: EncodedRLE) -> npt.NDArray[np.uint8]:
    ...

def area(rleObjs: EncodedRLE) -> np.uint32:
    ...

def toBbox(rleObjs: EncodedRLE) -> npt.NDArray[np.float64]:
    ...
