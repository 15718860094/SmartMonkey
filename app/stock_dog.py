import sys
import os
sys.path.append(os.getcwd())
sys.path.append(os.path.join(os.getcwd(), 'utils'))
sys.path.append(os.path.join(os.getcwd(), '.'))

from utils.StockHandler import ChinaeseStock
from settings import *



print(ChinaeseStock().fetch_data_for_days('d_000683'))