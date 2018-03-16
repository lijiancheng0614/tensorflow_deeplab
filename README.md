# TensorFlow DeepLab

Forked from https://github.com/tensorflow/models/tree/master/research/deeplab


## Updates

### Add `gpu_allow_growth` parameter in `eval.py`

Add `gpu_allow_growth` parameter in `eval.py`, default value is `True` which means attempting to allocate only as much GPU memory based on runtime allocations.

Modified files:

- `eval.py`

### Add `gpu_allow_growth` parameter in `train.py`

Add `gpu_allow_growth` parameter in `train.py`, default value is `True` which means attempting to allocate only as much GPU memory based on runtime allocations.

Modified files:

- `train.py`
