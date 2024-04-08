%cd ../..

import os
print(os.getcwd())


import numpy as np
import matplotlib.pyplot as plt

import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly_white"
import timesynth as ts
import pandas as pd
np.random.seed()

from src.synthetic_ts.autoregressive import AutoRegressive