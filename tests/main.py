# load coco dataset
from coco_loader.objectdetection import ObjectDetectionDataset
from pathlib import Path


def load_coco_dataset(
    coco_dataset_path: str, dataset_type: str
) -> ObjectDetectionDataset:
    file_name = None
    if dataset_type == "train":
        file_name = "instances_train2017.json"
    elif dataset_type == "val":
        file_name = "instances_val2017.json"
    elif dataset_type == "test":
        file_name = "image_info_test2017.json"

    # load the given COCO dataset JSON file using coco-lib
    coco_path = Path(coco_dataset_path).joinpath(file_name)
    coco_dataset: ObjectDetectionDataset = ObjectDetectionDataset.load(coco_path)

    return coco_dataset


# path to a COCO dataset JSON file
COCO_DATASET_PATH = "/Users/chacha/COCO2017/annotations"
dataset_type = "test"

# load the given COCO dataset JSON file using coco-lib
coco_dataset: ObjectDetectionDataset = load_coco_dataset(
    COCO_DATASET_PATH, dataset_type
)
