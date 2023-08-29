import re
import asyncio
from typing import List, Dict
from ocr.config import plate_number_regex


async def extract_license_plates_async(plate_numbers: List[str]) -> List[Dict[str, str]]:
    """
    Extracts license plate numbers from a list of strings using regular expressions asynchronously.

    Args:
        plate_numbers (List[str]): A list of strings containing potential license plate numbers.

    Returns:
        List[Dict[str, str]]: A list of dictionaries containing extracted license plate values along with their data types.
    """
    license_plate_list = []
    for plate in plate_numbers:
        await asyncio.sleep(0.1)  # Simulate an asynchronous operation if needed

        # Check if the input is a string and if it matches the license plate pattern
        if isinstance(plate, str) and re.match(plate_number_regex, plate):
            value_info = {
                "value": plate,
                "type": "Plate"
            }
            license_plate_list.append(value_info)
    return license_plate_list