from pathlib import Path

from src.winequalitymlops.utils.common import create_directories, read_yaml

d = read_yaml(Path("schema.yaml"))
print(d.COLUMNS.keys())
