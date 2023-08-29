import unittest
from unittest.mock import patch, Mock
import asyncio
from ocr.modules.date import extract_dates_async

class TestExtractDatesAsync(unittest.TestCase):

    @patch('ocr.modules.date.re.findall', Mock(return_value=['2023-08-29', '2023-08-30']))
    def test_extract_dates_async(self):
        """Test extracting dates asynchronously using a mock regular expression."""
        async def run_test():
            text = "Sample text with dates 2023-08-29 and 2023-08-30."
            result = await extract_dates_async(text)

            expected_result = [
                {"value": "2023-08-29", "type": "DATE"},
                {"value": "2023-08-30", "type": "DATE"}
            ]

            self.assertEqual(result, expected_result)

        asyncio.run(run_test())

if __name__ == '__main__':
    unittest.main()
