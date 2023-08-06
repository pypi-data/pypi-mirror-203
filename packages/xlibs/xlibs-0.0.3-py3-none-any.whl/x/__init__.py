# -*- coding: utf-8 -*-
"""
x: the everything pkg
"""

#%% imports 

import os
import sys
import numpy as np
import pandas as pd
import pyarrow as pa
import thelogger as tl

from icecream import ic
from ._ver import __version__

#%% fns

def env():
    return sys.executable