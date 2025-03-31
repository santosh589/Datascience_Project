from dataclasses import dataclass
from pathlib import Path

@dataclass   ## here we dont use self keyword as in normal class. Here there is no functions are assigned as normal class, so we use dataclass.
class DataIngestionconfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path



@dataclass
class DataValidationConfig:
    root_dir:Path
    STATUS_FILE:str
    unzip_data_dir:Path
    all_schema:dict

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path