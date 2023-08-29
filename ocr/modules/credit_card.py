async def luhn_algorithm(card_number):
    """
    Applies the Luhn algorithm to validate a credit card number.

    Args:
        card_number (str): The credit card number to be validated.

    Returns:
        bool: True if the credit card number is valid according to the Luhn algorithm, False otherwise.
    """
    card_number = card_number.replace("-", "").replace(" ", "")  # Remove dashes and spaces
    if not card_number.isdigit():
        return False

    total = 0
    num_digits = len(card_number)
    odd_indices = range(num_digits - 1, -1, -2)

    for i in range(num_digits):
        digit = int(card_number[i])
        if i in odd_indices:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit

    return (total % 10) == 0


async def identify_card_type(card_number):
    """
    Identifies the card type based on the first few digits of the card number.

    Args:
        card_number (str): The credit card number.

    Returns:
        str: The card type as a text, such as "Visa," "MasterCard," "American Express," or "Unknown."
    """
    first_digit = card_number[0]
    if first_digit == "4":
        return "Visa"
    elif first_digit == "5":
        return "MasterCard"
    elif first_digit == "3":
        return "American Express"
    else:
        return "Unknown"


async def validate_credit_card(card_number):
    """
    Validates a credit card number using the Luhn algorithm and identifies its type.

    Args:
        card_number (str): The credit card number to be validated.

    Returns:
        dict: A dictionary containing information about the credit card, including its number,
              validity status ("Valid" or "Not Valid"), and card type (e.g., "Visa").
    """
    valid = await luhn_algorithm(card_number)
    card_type = await identify_card_type(card_number)

    card_info = {
        "value": card_number,
        "validity": "Valid" if valid else "Not Valid",
        "type": card_type
    }

    return card_info
