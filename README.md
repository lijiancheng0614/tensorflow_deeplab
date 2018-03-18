# TensorFlow DeepLab

Forked from https://github.com/tensorflow/models/tree/master/research/deeplab

## Usage

1. Install dependencies by following the [installation instructions](g3doc/installation.md).

2. Add libraries to PYTHONPATH.

    ```
    git clone https://github.com/lijiancheng0614/tensorflow_deeplab deeplab
    export PYTHONPATH=$PYTHONPATH:`pwd`
    git clone https://github.com/tensorflow/models.git
    export PYTHONPATH=$PYTHONPATH:`pwd`/models/research/slim
    ```


## Updates

### Add `gpu_allow_growth` parameter in `eval.py`

Add `gpu_allow_growth` parameter in `eval.py`, default value is `True` which means attempting to allocate only as much GPU memory based on runtime allocations.

Modified files:

- `eval.py`

### Add `gpu_allow_growth` parameter in `train.py`

Add `gpu_allow_growth` parameter in `train.py`, default value is `True` which means attempting to allocate only as much GPU memory based on runtime allocations.

Modified files:

- `train.py`

### Add `max_to_keep` parameter in `train.py`

Add `max_to_keep` parameter in `train.py`, default value is `5` which means the 5 most recent checkpoint files are kept. If `0`, all checkpoint files are kept.

Modified files:

- `train.py`
