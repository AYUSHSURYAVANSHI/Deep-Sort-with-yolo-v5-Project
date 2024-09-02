__version__ = '0.8.0'
git_version = '6455a4c68d4d1bd2a78962527104aab8d286e19f'
from torchvision.extension import _check_cuda_version
if _check_cuda_version() > 0:
    cuda = _check_cuda_version()
