import pandas as pd
from pathlib import Path


def load_csv(data_path: Path) -> pd.DataFrame:
    return pd.read_csv(data_path)


if __name__ == "__main__":
    # TODO: fix this data path using the pathlib library
    path = Path(__file__).parent.parent / "data" / "game.csv"
    print(path)