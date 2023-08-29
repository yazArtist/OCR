import unittest
import asyncio
from unittest.mock import patch, Mock
from ocr.modules.id import extract_id_numbers_async


class TestIDModuleAsync(unittest.TestCase):

    @patch('ocr.modules.id.re.findall', Mock(return_value=['12345', '67890']))
    async def test_extract_id_numbers_async(self):
        """Test extracting identification numbers asynchronously using a mock regular expression."""
        text = "ID numbers: 12345 and 67890."
        country = "sample_country"

        result = await extract_id_numbers_async(text, country)
        expected_result = ['12345', '67890']
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
