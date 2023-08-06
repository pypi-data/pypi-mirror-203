import random

import numpy as np
import torch


def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def check(input):
    output = torch.from_numpy(input) if type(input) == np.ndarray else input
    return output


def check_v2(input, use_half=False, tpdv=None):
    output = torch.from_numpy(input) if type(input) == np.ndarray else input
    if tpdv:
        output = output.to(**tpdv)
    if use_half:
        output = output.half()
    return output


def _t2n(x):
    return x.detach().cpu().numpy()
