import unittest
from unittest.mock import patch, Mock
import asyncio
from ocr.modules.email import extract_emails_async

class TestExtractEmailsAsync(unittest.TestCase):

    @patch('ocr.modules.email.re.findall', Mock(return_value=['example@example.com', 'test@test.com']))
    def test_extract_emails_async(self):
        """Test extracting email addresses asynchronously using a mock regular expression."""
        async def run_test():
            text = "Contact us at example@example.com or test@test.com for more information."
            result = await extract_emails_async(text)

            expected_result = [
                {"value": "example@example.com", "type": "email"},  # Use 'email' instead of 'EMAIL'
                {"value": "test@test.com", "type": "email"}         # Use 'email' instead of 'EMAIL'
            ]

            self.assertEqual(result, expected_result)

        asyncio.run(run_test())

if __name__ == '__main__':
    unittest.main()
