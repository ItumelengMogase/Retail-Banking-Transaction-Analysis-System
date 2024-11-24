import pandas as pd

def load_csv(file_path):
    return pd.read_csv(file_path)

# Example usage
customers = load_csv('datasets/customers.csv')
