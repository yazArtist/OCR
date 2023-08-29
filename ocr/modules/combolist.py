import re
from ocr.enums import DataTypes
import ocr.config as config
from ocr.utils import log_info, log_empty_line

compiled_patterns = {}
for data_type, pattern in config.data_patterns.items():
    compiled_patterns[data_type] = re.compile(pattern)

async def extract_sensitive_data(text):
    """
    Extracts sensitive data patterns from the given text using compiled regular expressions.

    Args:
        text (str): The input text from which sensitive data needs to be extracted.

    Returns:
        dict: A dictionary containing extracted sensitive data grouped by their data types.
    """
    sensitive_data = {}

    # Iterate through compiled data patterns and extract data based on each pattern
    for data_type, compiled_pattern in compiled_patterns.items():
        sensitive_data[data_type] = compiled_pattern.findall(text)

    return sensitive_data

async def find_pattern_functional(text):
    """
    Extracts and logs information about sensitive data patterns found in the given text.

    Args:
        text (str): The input text containing potential sensitive data.
    """
    # Extract sensitive data using compiled patterns
    sensitive_data = await extract_sensitive_data(text)

    grouped_data = {}
    for data_type, data_list in sensitive_data.items():
        for data in data_list:
            if data_type in grouped_data:
                grouped_data[data_type].append(data)
            else:
                grouped_data[data_type] = [data]

    # Placeholder values for constant values
    values = {
        "value": DataTypes.COMBOLIST,
        "type": DataTypes.COMBOLIST
    }

    for data_type, data_list in grouped_data.items():
        for data in data_list:
            log_info(f"Data: {data} - Type: {data_type}")
            log_info(f"Constant values: {values}")
            log_empty_line()
