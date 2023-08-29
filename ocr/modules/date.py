import re
import asyncio
from ocr.config import data_patterns
from ocr.enums import DataTypes

async def extract_dates_async(text: str) -> list[dict[str, str]]:
    """
    Extracts dates from a given text using regular expressions asynchronously.

    Args:
        text (str): The input text from which dates need to be extracted.

    Returns:
        list[dict[str, str]]: A list of dictionaries containing extracted date values
                              along with their data types.
    """
    date_pattern = data_patterns[DataTypes.DATE]
    dates = re.findall(date_pattern, text)

    date_values = []
    for date in dates:
        await asyncio.sleep(0.1)  # Simulate an asynchronous operation if needed

        value_info = {
            "value": date,
            "type": DataTypes.DATE,
        }
        date_values.append(value_info)

    return date_values

