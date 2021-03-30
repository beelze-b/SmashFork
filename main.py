"""
 * Copyright (C) 2021 - Simone Riva
 * Distributed under the terms of the GNU General Public License (GPL)
 * This file is part of scAEspy.

 * SMaSH is a free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License v3.0 as published by
 * the Free Software Foundation.
  
 * SMaSH is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU General Public License for more details.
"""

import warnings
warnings.simplefilter(action='ignore')

import argparse, os
import numpy as np
import pandas as pd
from pandas.api.types import is_string_dtype, is_numeric_dtype
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from smash.smash import SMaSH
from smash._version import __version__

def main():

    print("* SMaSH (v.%s): ..."%__version__)

    smash = SMaSH()

if __name__ == '__main__':
    main()
