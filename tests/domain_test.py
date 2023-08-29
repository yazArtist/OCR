import unittest
from unittest.mock import patch, Mock
import asyncio
from ocr.modules.domain import extract_domains_async

class TestExtractDomainsAsync(unittest.TestCase):

    @patch('ocr.modules.domain.re.findall', Mock(return_value=[('http://example.com', 'example.com')]))
    def test_extract_domains_async(self):
        """Test extracting domains asynchronously using a mock regular expression."""
        async def run_test():
            text = "Visit http://example.com for more information."
            result = await extract_domains_async(text)

            expected_result = [
                {"value": "example.com", "type": "domain"}
            ]

            self.assertEqual(result, expected_result)

        asyncio.run(run_test())

    @patch('ocr.modules.domain.re.findall', Mock(return_value=[]))
    def test_extract_domains_async_none(self):
        """Test extracting domains asynchronously when no domains are found."""
        async def run_test():
            text = "No domains to extract here."
            result = await extract_domains_async(text)

            self.assertIsNone(result)

        asyncio.run(run_test())

if __name__ == '__main__':
    unittest.main()
