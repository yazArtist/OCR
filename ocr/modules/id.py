import re
import asyncio
from ocr.config import country_patterns


async def extract_id_numbers_async(text, country):
    """
    Extracts identification numbers based on the specified country's pattern from the given text
    asynchronously.

    Args:
        text (str): The input text from which identification numbers need to be extracted.
        country (str): The country for which the identification number pattern is used.

    Returns:
        list[str]: A list of identification numbers extracted from the text based on the specified country's pattern.
    """
    # Check if the specified country has a pattern defined in the configuration
    if country not in country_patterns:
        return []

    # Retrieve the identification number pattern for the specified country
    id_number_pattern = country_patterns[country]

    # Use regular expression to find identification numbers in the text based on the country's pattern
    id_numbers = re.findall(id_number_pattern, text)

    if id_numbers:
        await asyncio.sleep(0.1)  # Simulate an asynchronous operation if needed

    return id_numbers
