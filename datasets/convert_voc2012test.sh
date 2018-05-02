#!/bin/bash
#
# Script to preprocess the PASCAL VOC 2012 test dataset.
#
# Usage:
#   bash ./convert_voc2012test.sh
#
# The folder structure is assumed to be:
#  + data
#     - build_data.py
#     - build_voc2012test_data.py
#     - convert_voc2012test.sh
#     + VOCdevkit
#       + VOC2012test
#         + JPEGImages
#

# Exit immediately if a command exits with a non-zero status.
set -e

CURRENT_DIR=$(pwd)
WORK_DIR="./pascal_voc_seg"
mkdir -p ${WORK_DIR}

cd "${CURRENT_DIR}"

# Root path for PASCAL VOC 2012 dataset.
PASCAL_ROOT="${WORK_DIR}/VOCdevkit/VOC2012test"

# Build TFRecords of the dataset.
# First, create output directory for storing TFRecords.
OUTPUT_DIR="${WORK_DIR}/tfrecord"
mkdir -p "${OUTPUT_DIR}"

IMAGE_FOLDER="${PASCAL_ROOT}/JPEGImages"
LIST_FOLDER="${PASCAL_ROOT}/ImageSets/Segmentation"

echo "Converting PASCAL VOC 2012 test dataset..."
python ./build_voc2012test_data.py \
  --image_folder="${IMAGE_FOLDER}" \
  --list_folder="${LIST_FOLDER}" \
  --image_format="jpg" \
  --output_dir="${OUTPUT_DIR}"
