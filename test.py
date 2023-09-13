import unittest
from unittest.mock import patch, Mock
from main import perform_search


class TestGetDataFromAPI(unittest.TestCase):
    @patch("main.requests.get")
    def test_successful_request(self, mock_get):
        # Configure the mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        result = perform_search("https://api.example.com/data")
        self.assertEqual(result, 200)
        mock_get.assert_called_once_with("https://api.example.com/data")


if __name__ == "__main__":
    unittest.main()
