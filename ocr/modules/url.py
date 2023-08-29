import re
import asyncio
from typing import List, Dict
from ocr.config import url_pattern_regex


async def extract_urls_async(text: str) -> List[Dict[str, str]]:
    """
    Extracts URLs from the given text using regular expressions asynchronously.

    Args:
        text (str): The input text from which URLs need to be extracted.

    Returns:
        List[Dict[str, str]]: A list of dictionaries containing extracted URL values along with their data types.
    """
    # Use regular expressions to find patterns that match URLs in the text
    urls = re.findall(url_pattern_regex, text)

    url_list = []
    for url in urls:
        await asyncio.sleep(0.1)  # Simulate an asynchronous operation if needed

        # Create a dictionary to store the extracted URL value along with its data type
        value_info = {
            "value": url,
            "type": "URL"
        }
        url_list.append(value_info)

    return url_list
