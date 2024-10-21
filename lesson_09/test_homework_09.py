import unittest


from lesson_09.homework_09 import get_only_string, reverse_string, calculating_function, get_unique_elements, \
    word_with_specific_letter


class TestHomeworks(unittest.TestCase):

    def test_calculating_function_positive(self):
        result = calculating_function(1, 2)
        self.assertEqual(result, 3)
        result = calculating_function(1.1, 2.0)
        self.assertAlmostEqual(result, 3, delta=0.2)

    def test_calculating_function_negative(self):
        result = calculating_function(-50, -100)
        self.assertEqual(result, -150)

    def test_get_only_string_positive(self):
        boolean_result = get_only_string([5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'])
        self.assertTrue(boolean_result)

    def test_get_only_string_negative(self):
        boolean_result = get_only_string([1, 2, 7, 8.0])
        self.assertTrue(not boolean_result)

    def test_reverse_string_mean_positive(self):
        result = reverse_string("My name is Alex")
        self.assertEqual(result, "xelA si eman yM", msg=f"The test failed. The result {result} is not valid.")

    def test_reverse_string_mean_negative(self):
        with self.assertRaises(TypeError):
            reverse_string(1000)

    def test_get_unique_elements_positive(self):
        boolean_result = get_unique_elements("My name is Alexandr")
        self.assertTrue(boolean_result)

    def test_get_unique_elements_negative(self):
        boolean_result = get_unique_elements(["My name is Alexandr"])
        self.assertTrue(not boolean_result)

    def test_word_with_specific_letter_positive(self):
        boolean_result = word_with_specific_letter("Honor")
        self.assertTrue(not boolean_result)

    def test_word_with_specific_letter_is_none(self):
        result = word_with_specific_letter("Honor")
        self.assertIsNone(result)


if __name__ == "__name__":
    unittest.main()
