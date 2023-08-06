__version__ = "0.0.5"

import coco_types.dicts  # pyright: ignore[reportUnusedImport]

from .coco_keypoints import AnnotationKP, CategoryKP, DatasetKP
from .coco_object_detection import (
    Annotation,
    Category,
    Dataset,
    EncodedRLE,
    Image,
    Info,
    Licence,
    RLE,
    TPolygon_segmentation,
)

__all__ = [
    "Annotation", "Licence", "Category", "Dataset", "EncodedRLE", "Image", "RLE", "Info", "TPolygon_segmentation",
    "AnnotationKP", "CategoryKP", "DatasetKP",
]
