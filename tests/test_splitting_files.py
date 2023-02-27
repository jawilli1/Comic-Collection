import unittest
from src.split_files import remove_placeholders_map, file_name_to_dict, FIELDS


class TestCalculations(unittest.TestCase):
    files = [
        "Mad_EC_1_%35_July_1958.jpg",
        "Detective Comics_DC_1_1_Sep_1940.jpg",
        "Mad___110_Sep_1966.jpg",
        "Mad_ _ _110_Sep_1966.jpg",
        "Mad_     _     _110_Sep_1966.jpg",
        "Detective Comics___4__1953.jpg",
        "Mad___250.jpg",
        "Simpsons Shenanigans_Bongo.jpg",
    ]

    dict_list = file_name_to_dict(files)

    def test_remove_placeholders_map(self):
        # placeholders start with %
        expected = ["hey", "test", "", "swag"]
        initial_list = ["hey", "test", "%yolo", "swag"]
        output = list(map(remove_placeholders_map, initial_list))
        self.assertEqual(output, expected)

    def test_file_name_to_dict_length(self):
        self.assertEqual(len(self.dict_list), len(FIELDS))


if __name__ == "__main__":
    unittest.main()
