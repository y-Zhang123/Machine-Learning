import importlib.util
import sys

spec = importlib.util.find_spec('torch')
if spec is None:
    print('NOT INSTALLED')
    sys.exit(0)
import torch
print('INSTALLED', torch.__version__)
print('CUDA available:', torch.cuda.is_available())
