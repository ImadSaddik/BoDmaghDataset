#!/usr/bin/env python
import sys
import pandas as pd
import os


def check_for_nulls(file_path: str) -> bool:
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} does not exist", file=sys.stderr)
        return True
    try:
        df = pd.read_json(file_path)
        return df.isnull().sum().sum() > 0
    except Exception as e:
        print(f"Error reading or processing {file_path}: {e}", file=sys.stderr)
        return True


if __name__ == "__main__":
    script_directory = os.path.dirname(os.path.abspath(__file__))
    dataset_path = os.path.join(script_directory, '..', 'dataset.json')

    exit_code = 0
    if check_for_nulls(dataset_path):
        print(
            f"Error: Found null values or error processing {dataset_path}", file=sys.stderr)
        exit_code = 1
    else:
        print(f"No null values found in {dataset_path}.")

    sys.exit(exit_code)
