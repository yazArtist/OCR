import re
import asyncio
from typing import List, Dict
from ocr.config import phone_number_regex
from ocr.enums import DataTypes


async def extract_phone_numbers_async(text: str) -> List[Dict[str, str]]:
    """
    Extracts phone numbers from the given text using regular expressions asynchronously.

    Args:
        text (str): The input text from which phone numbers need to be extracted.

    Returns:
        List[Dict[str, str]]: A list of dictionaries containing extracted phone number values along with their data types.
    """
    # Use regular expressions to find patterns that match phone numbers in the text
    phone_numbers = re.findall(phone_number_regex, text)

    phone_number_list = []
    for number in phone_numbers:
        await asyncio.sleep(0.1)  # Simulate an asynchronous operation if needed

        # Create a dictionary to store the extracted phone number value along with its data type
        value_info = {
            "value": number,
            "type": DataTypes.PHONE_NUMBER
        }
        phone_number_list.append(value_info)

    return phone_number_list
