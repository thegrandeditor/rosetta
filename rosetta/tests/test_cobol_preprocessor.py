import unittest
from rosetta.babel.cobol.frontend import CobolFrontend

class TestCobolPreprocessor(unittest.TestCase):
    def setUp(self):
        self.frontend = CobolFrontend()

    def test_line_endings_and_whitespace_stripping(self):
        input_code = "   IDENTIFICATION DIVISION.   \r\n  PROGRAM-ID. HELLO.   \r\tPROCEDURE DIVISION.\n"
        expected = "IDENTIFICATION DIVISION.\r\nPROGRAM-ID. HELLO.\r\nPROCEDURE DIVISION.\r\n"
        self.assertEqual(self.frontend.preprocess(input_code), expected)

    def test_non_breaking_spaces(self):
        # Test that non-breaking spaces (\xa0) are replaced by standard spaces
        input_code = "IDENTIFICATION\xa0DIVISION.\r\nPROGRAM-ID.\xa0HELLO.\r\n"
        expected = "IDENTIFICATION DIVISION.\r\nPROGRAM-ID. HELLO.\r\n"
        self.assertEqual(self.frontend.preprocess(input_code), expected)

if __name__ == "__main__":
    unittest.main()
