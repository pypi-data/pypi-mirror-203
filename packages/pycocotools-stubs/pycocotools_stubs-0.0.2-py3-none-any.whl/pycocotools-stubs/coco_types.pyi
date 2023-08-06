from typing import Generic, TypeAlias, TypedDict, TypeVar

import numpy as np
import numpy.typing as npt

class Image(TypedDict):
    id: int
    width: int
    height: int
    file_name: str


TPolygonSegmentation: TypeAlias = list[list[float]]


class RLE(TypedDict):
    size: list[int]
    counts: list[int]


class EncodedRLE(TypedDict):
    size: list[int]
    counts: str | bytes


class Annotation(TypedDict):
    id: int
    image_id: int
    category_id: int
    # Segmentation can be a polygon, RLE or encoded RLE.
    # Exemple of polygon: "segmentation": [[510.66,423.01,511.72,420.03,...,510.45,423.01]]
    # Exemple of RLE: "segmentation": {"size": [40, 40], "counts": [245, 5, 35, 5, 35, 5, 35, 5, 35, 5, 1190]}
    # Exemple of encoded RLE: "segmentation": {"size": [480, 640], "counts": "aUh2b0X...BgRU4"}
    segmentation: TPolygonSegmentation | RLE | EncodedRLE
    area: float
    # The COCO bounding box format is [top left x position, top left y position, width, height].
    # bbox exemple:  "bbox": [473.07,395.93,38.65,28.67]
    bbox: list[float]
    iscrowd: int  # Either 1 or 0


T_Seg = TypeVar("T_Seg", TPolygonSegmentation, RLE, EncodedRLE)


class AnnotationG(TypedDict, Generic[T_Seg]):
    id: int
    image_id: int
    category_id: int
    # Segmentation can be a polygon, RLE or encoded RLE.
    # Exemple of polygon: "segmentation": [[510.66,423.01,511.72,420.03,...,510.45,423.01]]
    # Exemple of RLE: "segmentation": {"size": [40, 40], "counts": [245, 5, 35, 5, 35, 5, 35, 5, 35, 5, 1190]}
    # Exemple of encoded RLE: "segmentation": {"size": [480, 640], "counts": "aUh2b0X...BgRU4"}
    segmentation: T_Seg
    area: float
    # The COCO bounding box format is [top left x position, top left y position, width, height].
    # bbox exemple:  "bbox": [473.07,395.93,38.65,28.67]
    bbox: list[float]
    iscrowd: int  # Either 1 or 0


class Category(TypedDict):
    id: int
    name: str
    supercategory: str


class EvaluationResult(TypedDict):
    image_id: int
    category_id: int
    aRng: list[int]
    maxDet: int
    dtIds: list[int]
    gtIds: list[int]
    dtMatches: npt.NDArray[np.float64]
    gtMatches: npt.NDArray[np.float64]
    dtScores: list[float]
    gtIgnore: npt.NDArray[np.float64]
    dtIgnore: npt.NDArray[np.float64]


class Dataset(TypedDict):
    images: list[Image]
    annotations: list[Annotation]
    categories: list[Category]
