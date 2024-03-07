import unittest
from solutions.day5 import get_translated_ids, find_items_for_items, get_data_from_file, \
    get_seed_id_ranges_from_seed_numbers, get_translated_id_ranges, find_item_ranges_for_item_ranges, \
    find_minimum_id


class TestSequenceFunctions(unittest.TestCase):

    def test_get_translated_ids(self):
        translations = [
            {"source_range": range(1, 4), "translation_amount": 10},
            {"source_range": range(5, 8), "translation_amount": 20}
        ]
        source_ids = [1, 2, 5]
        expected_output = [11, 12, 25]
        self.assertEqual(get_translated_ids(source_ids, translations), expected_output)

        # Test with empty source_ids
        source_ids = []
        expected_output = []
        self.assertEqual(get_translated_ids(source_ids, translations), expected_output)

        # Test with empty translations
        translations = []
        source_ids = [1, 2, 5]
        expected_output = [1, 2, 5]
        self.assertEqual(get_translated_ids(source_ids, translations), expected_output)

    def test_find_items_for_items(self):
        elf_maps = {
            "seed": {"destination": "location", "translations": [
                {"source_range": range(1, 4), "translation_amount": 10}
            ]}
        }
        source = "seed"
        destination = "location"
        ids = [1, 2, 3]
        expected_output = [11, 12, 13]
        self.assertEqual(find_items_for_items(source, destination, ids, elf_maps), expected_output)

        # Test when source and destination are the same
        source = "seed"
        destination = "seed"
        ids = [1, 2, 3]
        expected_output = [1, 2, 3]
        self.assertEqual(find_items_for_items(source, destination, ids, elf_maps), expected_output)

        # Test with empty ids
        source = "seed"
        destination = "location"
        ids = []
        expected_output = []
        self.assertEqual(find_items_for_items(source, destination, ids, elf_maps), expected_output)

    def test_get_seed_id_ranges_from_seed_numbers(self):
        seed_numbers = [1, 3, 5, 2]
        expected_output = [range(1, 4), range(5, 7)]
        self.assertEqual(get_seed_id_ranges_from_seed_numbers(seed_numbers), expected_output)

        # Test with empty seed_numbers
        seed_numbers = []
        expected_output = []
        self.assertEqual(get_seed_id_ranges_from_seed_numbers(seed_numbers), expected_output)

    def test_get_translated_id_ranges(self):
        translations = [{"source_range": range(1, 4), "translation_amount": 10}]
        source_id_ranges = [range(1, 4), range(5, 7)]
        expected_output = [range(11, 14), range(5, 7)]
        self.assertEqual(list(get_translated_id_ranges(source_id_ranges, translations)), list(expected_output))

        # Test with empty source_id_ranges
        translations = [{"source_range": range(1, 4), "translation_amount": 10}]
        source_id_ranges = []
        expected_output = []
        self.assertEqual(list(get_translated_id_ranges(source_id_ranges, translations)), expected_output)

    def test_find_item_ranges_for_item_ranges(self):
        elf_maps = {
            "seed": {"destination": "location", "translations": [
                {"source_range": range(1, 4), "translation_amount": 10}
            ]}
        }
        source = "seed"
        destination = "location"
        id_ranges = [range(1, 4), range(5, 7)]
        expected_output = [range(11, 14), range(5, 7)]
        self.assertEqual(list(find_item_ranges_for_item_ranges(source, destination, id_ranges, elf_maps)), list(expected_output))

        # Test when source and destination are the same
        source = "seed"
        destination = "seed"
        id_ranges = [range(1, 4), range(5, 7)]
        expected_output = [range(1, 4), range(5, 7)]
        self.assertEqual(list(find_item_ranges_for_item_ranges(source, destination, id_ranges, elf_maps)), list(expected_output))

        # Test with empty id_ranges
        source = "seed"
        destination = "location"
        id_ranges = []
        expected_output = []
        self.assertEqual(list(find_item_ranges_for_item_ranges(source, destination, id_ranges, elf_maps)), expected_output)

    def test_find_minimum_id(self):
        id_ranges = [range(1, 4), range(5, 7)]
        self.assertEqual(find_minimum_id(id_ranges), 1)

        # Test with empty id_ranges
        id_ranges = []
        self.assertIsNone(find_minimum_id(id_ranges))

if __name__ == '__main__':
    unittest.main()
