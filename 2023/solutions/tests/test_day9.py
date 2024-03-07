import unittest

# Import the functions you want to test
from solutions.day9 import add_one_to_either_end_of_sequence, get_previous_number, get_next_number


class TestSequenceFunctions(unittest.TestCase):

    def test_add_one_to_either_end_of_sequence(self):
        # Test with an empty sequence
        input_sequence = []
        expected_output = [0, 1]
        self.assertEqual(add_one_to_either_end_of_sequence([input_sequence]), [expected_output])

        # Test with a sequence of one element
        input_sequence = [1]
        expected_output = [0, 1, 2]
        self.assertEqual(add_one_to_either_end_of_sequence([input_sequence]), [expected_output])

        # Test with a sequence of multiple elements
        input_sequence = [1, 2, 3]
        expected_output = [0, 1, 2, 3, 4]
        self.assertEqual(add_one_to_either_end_of_sequence([input_sequence]), [expected_output])

    def test_get_previous_number(self):
        # Test with a sequence with no zeros
        sequence = [1, 2, 3]
        self.assertEqual(get_previous_number(sequence), 0)

        # Test with a sequence with zeros
        sequence = [0, 0, 0, 0]
        self.assertEqual(get_previous_number(sequence), 0)

        # Test with a sequence with a mix of zeros and non-zeros
        sequence = [0, 1, 0, 2, 0, 3]
        self.assertEqual(get_previous_number(sequence), 0)

    def test_get_next_number(self):
        # Test with a sequence with no zeros
        sequence = [1, 2, 3]
        self.assertEqual(get_next_number(sequence), 4)

        # Test with a sequence with zeros
        sequence = [0, 0, 0, 0]
        self.assertEqual(get_next_number(sequence), 0)

        # Test with a sequence with a mix of zeros and non-zeros
        sequence = [0, 1, 0, 2, 0, 3]
        self.assertEqual(get_next_number(sequence), 4)

    # You can add more tests for other functions here


if __name__ == '__main__':
    unittest.main()