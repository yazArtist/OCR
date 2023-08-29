import re
import hashlib
import asyncio
from ocr.config import data_patterns
from ocr.enums import DataTypes


async def extract_hashes_async(text: str) -> list[dict[str, str]]:
    """
    Extracts hash values from the given text using regular expressions and categorizes them by algorithm
    asynchronously.

    Args:
        text (str): The input text from which hash values need to be extracted.

    Returns:
        list[dict[str, str]]: A list of dictionaries containing extracted hash values along with their
                              data types and hash algorithm information.
    """
    # Use regular expressions to find patterns that match hash values in the text
    md5_hashes = re.findall(data_patterns[DataTypes.HASH], text)
    sha256_hashes = re.findall(data_patterns[DataTypes.HASH], text)

    hash_values = []
    # Create dictionaries to store extracted hash values along with their data types and algorithm information
    for hash_value in md5_hashes:
        await asyncio.sleep(0.1)  # Simulate an asynchronous operation if needed

        value_info = {
            "value": hash_value,
            "type": DataTypes.HASH,
        }
        hash_values.append(value_info)

    for hash_value in sha256_hashes:
        await asyncio.sleep(0.1)  # Simulate an asynchronous operation if needed

        value_info = {
            "value": hash_value,
            "type": DataTypes.HASH,
        }
        hash_values.append(value_info)

    return hash_values


async def hash_data_async(data: str, algorithm: str) -> str:
    """
    Generates a hash value for the given data using the specified algorithm asynchronously.

    Args:
        data (str): The data to be hashed.
        algorithm (str): The hash algorithm to be used ("md5" or "sha256").

    Returns:
        str: The hash value of the data using the specified algorithm.
             Returns None if the algorithm is not recognized.
    """
    if algorithm == "md5":
        hasher = hashlib.md5()
    elif algorithm == "sha256":
        hasher = hashlib.sha256()
    else:
        return None

    hasher.update(data.encode())
    await asyncio.sleep(0.1)  # Simulate an asynchronous operation if needed
    return hasher.hexdigest()


#validators kütüphane date parser