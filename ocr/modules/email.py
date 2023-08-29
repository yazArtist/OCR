import re
import asyncio
from ocr.config import data_patterns
from ocr.enums import DataTypes


async def extract_emails_async(text: str) -> list[dict[str, str]]:
    """
    Extracts email addresses from the given text using regular expressions asynchronously.

    Args:
        text (str): The input text from which email addresses need to be extracted.

    Returns:
        list[dict[str, str]]: A list of dictionaries containing extracted email address values
                              along with their data types.
    """
    # Get the email pattern from data_patterns dictionary
    email_pattern = data_patterns[DataTypes.EMAIL]

    # Use regular expressions to find patterns that match email addresses in the text
    email_addresses = re.findall(email_pattern, text, re.IGNORECASE)

    email_values = []
    for email in email_addresses:
        await asyncio.sleep(0.1)  # Simulate an asynchronous operation if needed

        # Create a dictionary to store the extracted email address value along with its data type
        value_info = {
            "value": email,
            "type": DataTypes.EMAIL,
        }
        email_values.append(value_info)

    return email_values