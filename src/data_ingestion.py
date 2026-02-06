from config import config
import pandas as pd
import numpy as np

def data_ingestion():
    df = pd.read_csv(config.filepath)
    return df