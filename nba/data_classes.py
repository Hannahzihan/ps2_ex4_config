# TODO: define your data classes here
from pydantic import BaseModel
from pathlib import Path
from typing import List

class DataConfig(BaseModel):
    table: str
    data_path: Path
    features_columns: List[str]

class ParamConfig(BaseModel):
    max_iter: int
    random_state: int

class ModelConfig(BaseModel):
    name: str
    type: str
    params: ParamConfig

class Config(BaseModel):
    data: DataConfig
    model: ModelConfig
