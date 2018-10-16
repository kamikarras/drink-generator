from model import db, connect_to_db
from server import app
import unittest


# this is the test file

class MyAppTest(unittest.TestCase):
    """tests for drink generator"""

    def setUp(self):
        """code to run before every test."""

        app.config['Testing'] = True
        self.client = app.test_client()


    def test_homepage_page(self):
        """can we reach the homepage"""

        result = self.client.get("/")
        self.assertIn(b"Generate your cocktail", result.data)

    


if __name__ == "__main__":
    unittest.main()
