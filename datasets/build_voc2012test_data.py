"""Converts PASCAL VOC 2012 test data to TFRecord file format with Example protos.

PASCAL VOC 2012 test dataset is expected to have the following directory structure:

  + pascal_voc_seg
    - build_data.py
    - build_voc2012test_data.py (current working directory).
    + VOCdevkit
      + VOC2012test
        + JPEGImages
        + ImageSets
          + Segmentation
    + tfrecord

Image folder:
  ./VOCdevkit/VOC2012test/JPEGImages

list folder:
  ./VOCdevkit/VOC2012test/ImageSets/Segmentation

This script converts data into sharded data files and save at tfrecord folder.

The Example proto contains the following fields:

  image/encoded: encoded image content.
  image/filename: image filename.
  image/format: image file format.
  image/height: image height.
  image/width: image width.
  image/channels: image channels.
"""
import glob
import math
import os.path
import sys
import build_data
import tensorflow as tf

FLAGS = tf.app.flags.FLAGS

tf.app.flags.DEFINE_string('image_folder',
                           './VOCdevkit/VOC2012test/JPEGImages',
                           'Folder containing images.')

tf.app.flags.DEFINE_string(
    'list_folder',
    './VOCdevkit/VOC2012/ImageSets/Segmentation',
    'Folder containing lists for training and validation')

tf.app.flags.DEFINE_string(
    'output_dir',
    './tfrecord',
    'Path to save converted SSTable of TensorFlow examples.')


_NUM_SHARDS = 4


def _convert_dataset(dataset_split):
  """Converts the specified dataset split to TFRecord format.

  Args:
    dataset_split: The dataset split (e.g., train, test).

  Raises:
    RuntimeError: If loaded image and label have different shape.
  """
  dataset = os.path.basename(dataset_split)[:-4]
  sys.stdout.write('Processing ' + dataset)
  filenames = [x.strip('\n') for x in open(dataset_split, 'r')]
  num_images = len(filenames)
  num_per_shard = int(math.ceil(num_images / float(_NUM_SHARDS)))

  image_reader = build_data.ImageReader('jpeg', channels=3)

  for shard_id in range(_NUM_SHARDS):
    output_filename = os.path.join(
        FLAGS.output_dir,
        '%s-%05d-of-%05d.tfrecord' % (dataset, shard_id, _NUM_SHARDS))
    with tf.python_io.TFRecordWriter(output_filename) as tfrecord_writer:
      start_idx = shard_id * num_per_shard
      end_idx = min((shard_id + 1) * num_per_shard, num_images)
      for i in range(start_idx, end_idx):
        sys.stdout.write('\r>> Converting image %d/%d shard %d' % (
            i + 1, len(filenames), shard_id))
        sys.stdout.flush()
        # Read the image.
        image_filename = os.path.join(
            FLAGS.image_folder, filenames[i] + '.' + FLAGS.image_format)
        image_data = tf.gfile.FastGFile(image_filename, 'r').read()
        height, width = image_reader.read_image_dims(image_data)
        # Convert to tf example.
        example = build_data.image_seg_to_tfexample(
            image_data, filenames[i], height, width)
        tfrecord_writer.write(example.SerializeToString())
    sys.stdout.write('\n')
    sys.stdout.flush()


def main(unused_argv):
  dataset_splits = glob.glob(os.path.join(FLAGS.list_folder, '*.txt'))
  for dataset_split in dataset_splits:
    _convert_dataset(dataset_split)


if __name__ == '__main__':
  tf.app.run()
