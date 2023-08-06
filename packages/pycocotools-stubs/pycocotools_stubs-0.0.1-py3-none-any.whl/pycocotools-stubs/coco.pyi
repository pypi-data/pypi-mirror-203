from pathlib import Path
from typing import Literal, overload

import numpy as np
import numpy.typing as npt
from typing_extensions import Self

from .coco_types import Annotation, AnnotationG, Category, Dataset, EncodedRLE, Image, RLE, TPolygon_segmentation


class COCO:
    anns: dict[int, Annotation]
    dataset: Dataset
    cats: dict[int, Category]
    imgs: dict[int, Image]
    imgToAnns: dict[int, list[Annotation]]
    catToImgs: dict[int, list[int]]

    def __init__(self, annotation_file: str | Path = ...) -> None:
        """Constructor of Microsoft COCO helper class for reading and visualizing annotations.

        Args:
            annotation_file: Location of annotation file
        """
        ...

    def createIndex(self) -> None:
        ...

    def info(self) -> None:
        """Print information about the annotation file.
        """
        ...

    def getAnnIds(self, imgIds: list[int] | int = ..., catIds: list[int] | int = ..., areaRng: list[float] = ..., iscrowd: bool | None = ...) -> list[int]:
        """Get ann ids that satisfy given filter conditions. default skips that filter.

        Args:
            imgIds: Get anns for given imgs.
            catIds: Get anns for given cats.
            areaRng: Get anns for given area range (e.g. [0 inf]).
            iscrowd: Get anns for given crowd label (False or True).

        Returns:
            Integer array of ann ids.
        """
        ...

    def getCatIds(self, catNms: list[str] | str = ..., supNms: list[str] | str = ..., catIds: list[int] | int = ...) -> list[int]:
        """Get cat ids that satisfy given filter conditions. default skips that filter.

        Args:
            catNms: get cats for given cat names
            supNms get cats for given supercategory names
            catIds: get cats for given cat ids

        Returns:
            ids: integer array of cat ids
        """
        ...

    def getImgIds(self, imgIds: list[int] | int = ..., catIds: list[int] | int = ...) -> list[int]:
        """Get img ids that satisfy given filter conditions.

        Args:
            imgIds: get imgs for given ids
            catIds : get imgs with all given cats

        Returns:
            ids: integer array of img ids
        """
        ...

    def loadAnns(self, ids: list[int] | int = ...) -> list[Annotation]:
        """Load anns with the specified ids.

        Args:
            ids: Integer ids specifying anns.

        Returns:
            anns: loaded ann objects
        """
        ...

    def loadCats(self, ids: list[int] | int = ...) -> list[Category]:
        """Load cats with the specified ids.

        Args:
            ids: integer ids specifying cats.

        Returns:
            cats: loaded cat objects.
        """
        ...

    def loadImgs(self, ids: list[int] | int = ...) -> list[Image]:
        """Load anns with the specified ids.

        Args:
            ids: integer ids specifying img

        Returns:
            imgs: loaded img objects
        """
        ...

    def showAnns(self, anns: list[Annotation], draw_bbox: bool = ...) -> None:
        """Display the specified annotations.

        Args:
            anns: Annotations to display.
            draw_bbox: Wether to draw the bounding boxes or not.
        """
        ...

    def loadRes(self, resFile: str) -> Self:
        """Load result file and return a result api object.

        Args:
            resFile: file name of result file

        Returns:
            res: result api object
        """
        ...

    def download(self, tarDir: str | None = ..., imgIds: list[int] = ...) -> Literal[-1] | None:
        """Download COCO images from mscoco.org server.

        Args:
            tarDir: COCO results directory name
            imgIds: images to be downloaded
        """
        ...

    def loadNumpyAnnotations(self, data: npt.NDArray[np.float64]) -> list[Annotation]:
        """Convert result data from a numpy array [Nx7] where each row contains {imageID,x1,y1,w,h,score,class}

        Args:
             data (numpy.ndarray)

        Returns:
            annotations (python nested list)
        """
        ...

    @overload
    def annToRLE(self, ann: AnnotationG[RLE]) -> RLE:
        """Convert annotation which can be polygons, uncompressed RLE to RLE."""
        ...

    @overload
    def annToRLE(self, ann: AnnotationG[EncodedRLE]) -> EncodedRLE:
        """Convert annotation which can be polygons, uncompressed RLE to RLE."""
        ...

    @overload
    def annToRLE(self, ann: AnnotationG[TPolygon_segmentation]) -> EncodedRLE:
        """Convert annotation which can be polygons, uncompressed RLE to RLE."""
        ...

    def annToMask(self, ann: Annotation) -> npt.NDArray[np.uint8]:
        """Convert annotation which can be polygons, uncompressed RLE, or RLE to binary mask.

        Args:
            ann: The annotation whose mask shoulb be returned.

        Returns:
            binary mask (numpy 2D array)
        """
        ...
