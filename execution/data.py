import pandas as pd

def load_data():
    data = {
        "open": [100, 103, 107],
        "high": [105, 108, 110],
        "low": [99, 101, 106],
        "close": [103, 107, 109],
        "volume": [900000, 1200000, 1300000],
    }
    return pd.DataFrame(data)
