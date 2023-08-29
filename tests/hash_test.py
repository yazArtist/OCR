import unittest
from unittest.mock import patch, Mock
import asyncio
from ocr.modules.hash import extract_hashes_async, hash_data_async

class TestHashesAsync(unittest.TestCase):

    @patch('ocr.modules.hash.re.findall', Mock(return_value=['hash1', 'hash2']))
    def test_extract_hashes_async(self):
        """Test extracting hash values asynchronously using a mock regular expression."""
        text = "Hashes: hash1 and hash2."
        result = asyncio.run(extract_hashes_async(text))

        expected_result = [
            {"value": "hash1", "type": "HASH"},
            {"value": "hash2", "type": "HASH"}
        ]

        self.assertEqual(result, expected_result)

    async def run_test(self, coro):
        loop = asyncio.get_event_loop()
        return await coro

    async def test_hash_data_async_md5(self):
        """Test generating a hash value using the MD5 algorithm asynchronously."""
        data = "test_data"
        algorithm = "md5"
        result = await self.run_test(hash_data_async(data, algorithm))

        expected_result = "cc03e747a6afbbcbf8be7668acfebee5"
        self.assertEqual(result, expected_result)

    async def test_hash_data_async_sha256(self):
        """Test generating a hash value using the SHA-256 algorithm asynchronously."""
        data = "test_data"
        algorithm = "sha256"
        result = await self.run_test(hash_data_async(data, algorithm))

        expected_result = "532eaabd9574880dbf76b9b8cc00832c20a6ec113d682299550d7a6e0f345e25"
        self.assertEqual(result, expected_result)

    async def test_hash_data_async_invalid_algorithm(self):
        """Test generating a hash value with an invalid algorithm asynchronously."""
        data = "test_data"
        algorithm = "invalid_algorithm"
        result = await self.run_test(hash_data_async(data, algorithm))

        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
