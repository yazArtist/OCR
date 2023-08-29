import unittest
import asyncio
from unittest.mock import patch, Mock
from ocr.modules.plate import extract_license_plates_async

class TestPlateModuleAsync(unittest.TestCase):

    @patch('ocr.modules.plate.re.match', Mock(return_value=True))
    def test_extract_license_plates_async(self):
        """Test extracting license plate numbers asynchronously using a mock regular expression."""
        plate_numbers = ["ABC123", "DEF456", "GHI789"]
        result = asyncio.run(extract_license_plates_async(plate_numbers))

        expected_result = [
            {"value": "ABC123", "type": "Plate"},
            {"value": "DEF456", "type": "Plate"},
            {"value": "GHI789", "type": "Plate"}
        ]
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
