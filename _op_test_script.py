"""
    Objective Partitioning
    --Test Script

    Fluvio L Lobo Fenoglietto
    03/06/2017
"""

from _op_functions_module import _browse_data_file
from _op_functions_module import _parse_data

# browse data file
target_file, file_path, file_dir, file_name, raw_data = _browse_data_file()

# split raw daat into lines

data = _parse_data(file_name, raw_data)

