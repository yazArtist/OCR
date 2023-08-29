import unittest
from unittest.mock import patch, Mock
import asyncio
from ocr.modules.credit_card import luhn_algorithm, identify_card_type, validate_credit_card

class TestLuhnAlgorithm(unittest.TestCase):

    def test_luhn_algorithm_valid(self):
        """Test the Luhn algorithm with a valid credit card number."""
        valid_card_number = "4532015112830366"
        result = asyncio.run(luhn_algorithm(valid_card_number))
        self.assertTrue(result)

    def test_luhn_algorithm_invalid(self):
        """Test the Luhn algorithm with an invalid credit card number."""
        invalid_card_number = "4532015112830365"
        result = asyncio.run(luhn_algorithm(invalid_card_number))
        self.assertFalse(result)

class TestIdentifyCardType(unittest.TestCase):

    def test_identify_card_type_visa(self):
        """Test identifying a Visa card based on its first digit."""
        visa_card_number = "4532015112830366"
        result = asyncio.run(identify_card_type(visa_card_number))
        self.assertEqual(result, "Visa")

    def test_identify_card_type_mastercard(self):
        """Test identifying a MasterCard based on its first digit."""
        mastercard_card_number = "5532015112830366"
        result = asyncio.run(identify_card_type(mastercard_card_number))
        self.assertEqual(result, "MasterCard")

    def test_identify_card_type_amex(self):
        """Test identifying an American Express card based on its first digit."""
        amex_card_number = "3532015112830366"
        result = asyncio.run(identify_card_type(amex_card_number))
        self.assertEqual(result, "American Express")

    def test_identify_card_type_unknown(self):
        """Test identifying a card of unknown type based on its first digit."""
        unknown_card_number = "6011015112830366"
        result = asyncio.run(identify_card_type(unknown_card_number))
        self.assertEqual(result, "Unknown")

class TestValidateCreditCard(unittest.TestCase):

    @patch('ocr.modules.credit_card.luhn_algorithm', Mock(return_value=True))
    @patch('ocr.modules.credit_card.identify_card_type', Mock(return_value="Visa"))
    def test_validate_credit_card_valid(self):
        """Test validating a credit card as valid with a specific type."""
        valid_card_number = "4532015112830366"
        result = asyncio.run(validate_credit_card(valid_card_number))
        expected_result = {
            "value": valid_card_number,
            "validity": "Valid",
            "type": "Visa"
        }
        self.assertEqual(result, expected_result)

    @patch('ocr.modules.credit_card.luhn_algorithm', Mock(return_value=False))
    @patch('ocr.modules.credit_card.identify_card_type', Mock(return_value="MasterCard"))
    def test_validate_credit_card_invalid(self):
        """Test validating a credit card as invalid with a specific type."""
        invalid_card_number = "5532015112830366"
        result = asyncio.run(validate_credit_card(invalid_card_number))
        expected_result = {
            "value": invalid_card_number,
            "validity": "Not Valid",
            "type": "MasterCard"
        }
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
