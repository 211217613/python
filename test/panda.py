#! /usr/bin/python3 

import os
import numpy as np
import pandas as pd

import geonamescache

from lxml import html

data_dir = os.path.expanduser('~')
gc = geonamescache.GeonamesCache()

url ='http://www.bloomberg.com/visual-data/best-and-worst/highest-paid-software-engineers-countries'
tree = html.parse(url)
print(tree)