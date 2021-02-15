
from enum import Enum
from itertools import product
import time
from typing import Any, Dict, List, NamedTuple, Optional

import awswrangler as wr
import pyarrow
from pyarrow.parquet import ParquetDataset
from pyarrow import fs
import s3fs
from tqdm import tqdm

class Method(Enum):
    local = 'Local Filesystem'
    arrow_s3fs = 'PyArrow s3fs'
    s3fs = 'Dask s3fs'
    aws_data_wrangler = 'AWS Data Wrangler'


class BenchmarkParams(NamedTuple):
    num_files: int
    num_columns: Optional[int]
    method: Method


def get_files(num_files: int) -> List[str]:
    return [f'2018/{month:02}/data.parquet' for month in range(1, num_files + 1)]


def get_columns(num_columns: Optional[int]) -> Optional[List[str]]:
    file = './data/2018/01/data.parquet'
    all_columns = ParquetDataset(file).schema.names
    if num_columns is None:
        return None
    else:
        return all_columns[:num_columns]


def local_read(files: List[str], columns: Optional[List[str]]) -> pyarrow.Table:
    files = [f'data/{path}' for path in files]
    return ParquetDataset(files).read(columns=columns)


def arrow_s3fs_read(files: List[str], columns: Optional[List[str]], bucket: str) -> pyarrow.Table:
    files = [f'{bucket}/{path}' for path in files]
    s3 = fs.S3FileSystem()
    return ParquetDataset(files, filesystem=s3).read(columns=columns)


def s3fs_read(files: List[str], columns: Optional[List[str]], bucket: str) -> pyarrow.Table:
    files = [f's3://{bucket}/{path}' for path in files]
    s3 = s3fs.S3FileSystem()
    return ParquetDataset(files, filesystem=s3).read(columns=columns)


def datawrangler_read(files: List[str], columns: Optional[List[str]], bucket: str) -> pyarrow.Table:
    files = [f's3://{bucket}/{path}' for path in files]
    df = wr.s3.read_parquet(files, columns=columns)
    return pyarrow.Table.from_pandas(df)


def run_one(params: BenchmarkParams, bucket: str) -> pyarrow.Table:
    files = get_files(params.num_files)
    columns = get_columns(params.num_columns)

    if params.method == Method.local:
        return local_read(files, columns)
    elif params.method == Method.arrow_s3fs:
        return arrow_s3fs_read(files, columns, bucket)
    elif params.method == Method.s3fs:
        return s3fs_read(files, columns, bucket)
    elif params.method == Method.aws_data_wrangler:
        return datawrangler_read(files, columns, bucket)


def run_benchmark(files: List[int], columns: List[Optional[int]], bucket: str) -> pyarrow.Table:
    out = []
    params = product(files, columns, [Method.local, Method.arrow_s3fs, Method.aws_data_wrangler])
    for num_files, num_columns, method in tqdm(list(params)): 
        params = BenchmarkParams(num_files, num_columns, method)
        start = time.monotonic()
        result = run_one(params, bucket)
        end = time.monotonic()
        out.append({'runtime': end - start, 'out_size': result.nbytes, **params._asdict()})

    out_table = pyarrow.table(
        {
            'num_files': [r['num_files'] for r in out],
            'num_columns': [r['num_columns'] for r in out],
            'method': [r['method'].value for r in out],
            'runtime': [r['runtime'] for r in out],
            'out_size': [r['out_size'] for r in out],
        }
    )
    return out_table
