import pandas as pd

def get_sample_data():
    data = {
        "Name": ["Alice", "Bob", "Charlie"],
        "Role": ["Developer", "Analyst", "Manager"],
        "Score": [90, 85, 95]
    }
    return pd.DataFrame(data)
