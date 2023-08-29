import unittest
from unittest.mock import patch, Mock
import asyncio
from ocr.modules.phone_num import extract_phone_numbers_async


class TestPhoneNumberModuleAsync(unittest.TestCase):

    @patch('ocr.modules.phone_num.re.findall', Mock(return_value=['123-456-7890', '987-654-3210']))
    async def test_extract_phone_numbers_async(self):
        """Test extracting phone numbers asynchronously using a mock regular expression."""
        text = "Phone numbers: 123-456-7890 and 987-654-3210."

        result = await extract_phone_numbers_async(text)
        expected_result = [
            {"value": "123-456-7890", "type": "PHONE_NUMBER"},
            {"value": "987-654-3210", "type": "PHONE_NUMBER"}
        ]
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
