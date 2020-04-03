import os
from pathlib import Path

DATASET_ROOT = "/mnt/blobfusetmp/kinetics600/"
TRAIN_ROOT = os.path.join(DATASET_ROOT, "train")
VALID_ROOT = os.path.join(DATASET_ROOT, "val")
TEST_ROOT = os.path.join(DATASET_ROOT, "test")

TRAIN_FRAMES_ROOT = os.path.join(DATASET_ROOT, "train_frames")
VALID_FRAMES_ROOT = os.path.join(DATASET_ROOT, "val_frames")
TEST_FRAMES_ROOT = os.path.join(DATASET_ROOT, "test_frames")

TRAIN_SOUND_ROOT = os.path.join(DATASET_ROOT, "train_sound")
VALID_SOUND_ROOT = os.path.join(DATASET_ROOT, "val_sound")
TEST_SOUND_ROOT = os.path.join(DATASET_ROOT, "test_sound")

CATEGORIES_PATH = "resources/categories.json"
CLASSES_PATH = "resources/classes.json"

TRAIN_METADATA_PATH = "resources/600/kinetics_600_train.json"
VAL_METADATA_PATH = "resources/600/kinetics_600_val.json"
TEST_METADATA_PATH = "resources/600/kinetics_600_test.json"

SUB_CLASS_PATH = "resources/700/categories.json"
