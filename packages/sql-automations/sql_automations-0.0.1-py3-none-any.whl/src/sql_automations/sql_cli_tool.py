"""
Script to read a external .sql file from a GCP connection CLI tool & return as pandas df

$ output-data --run=sample 
$ sql_to_df --run=sample --dir=models

"""

#!/usr/bin/env python3 
import argparse
from . big_query import execute_sql as ex
from . data_cleaning import read_data as rd

def run_sql():
    cli_parser = argparse.ArgumentParser()

    cli_parser.add_argument('--run', help="Name of sql file")
    cli_parser.add_argument('--dir', help="Diff folders", default="models")
    args = cli_parser.parse_args()

    sqlfile = args.run
    dirname = args.dir

    filepath = rd.read_data(f"./{dirname}/{sqlfile}.sql") 
    df = ex.execute_sql(filepath)

    return df
 
if __name__ == '__main__':
    run_sql()