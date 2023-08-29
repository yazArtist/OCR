import re
import asyncio
from ocr.config import data_patterns
from ocr.enums import DataTypes


async def extract_domains_async(text: str) -> list[dict[str, str]] | None:
    """
    Extracts domains from the given text using regular expressions asynchronously.

    Args:
        text (str): The input text from which domains need to be extracted.

    Returns:
        list[dict[str, str]] | None: A list of dictionaries containing extracted domain values
                                     along with their data types, or None if no domains are found.
    """
    # Get the domain pattern from data_patterns dictionary
    domain_pattern = data_patterns[DataTypes.DOMAIN]

    # Use regular expression to find domains in the text
    domains = re.findall(domain_pattern, text)
    domain_infos = []

    for domain in domains:
        await asyncio.sleep(0.1)  # Simulate an asynchronous operation if needed

        # Create dictionaries to store extracted domain values along with their data types
        domain_info = {
            "value": domain[1],
            "type": DataTypes.DOMAIN,
        }
        domain_infos.append(domain_info)

    # If no domains are found, return None; otherwise, return the list of domain information
    return domain_infos if domain_infos else None