import pandas as pd

def load_trajectory_data(file_path):
    """Load trajectory data from CSV."""
    df = pd.read_csv(file_path, names=['ped_id', 'frame', 'x', 'y'])
    return df.groupby('ped_id').apply(lambda x: x[['x', 'y']].values).to_dict()
