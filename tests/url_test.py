import unittest
from unittest.mock import patch, Mock
import asyncio
from ocr.modules.url import extract_urls_async

class TestURLModuleAsync(unittest.TestCase):

    @patch('ocr.modules.url.re.findall', Mock(return_value=['http://example.com', 'https://example.org']))
    async def test_extract_urls_async(self):
        """Test extracting URLs asynchronously using a mock regular expression."""
        text = "Here are some URLs: http://example.com and https://example.org."
        result = await extract_urls_async(text)

        expected_result = [
            {"value": "http://example.com", "type": "URL"},
            {"value": "https://example.org", "type": "URL"}
        ]
        self.assertEqual(result, expected_result)

    async def run_test(self, coro):
        loop = asyncio.get_event_loop()
        return await coro

if __name__ == '__main__':
    unittest.main()
