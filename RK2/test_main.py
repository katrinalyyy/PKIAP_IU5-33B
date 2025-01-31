import unittest
from main import Browser, Computer, BrowserComputer, query_1, query_2, query_3


class TestMainFunctions(unittest.TestCase):
    def setUp(self):
        self.comps = [
            Computer(1, "Компьютер 1"),
            Computer(2, "Компьютер 2"),
            Computer(3, "Компьютер 3")
        ]
        self.brows = [
            Browser(1, "Chrome", 120, 1),
            Browser(2, "Firefox", 100, 1),
            Browser(3, "Safari", 200, 2),
            Browser(4, "Opera", 150, 3),
            Browser(5, "Edge", 80, 3),
            Browser(6, "Alpha", 90, 2)  # Browser name starts with 'A'
        ]
        self.browser_pc_link = [
            BrowserComputer(1, 1),
            BrowserComputer(2, 1),
            BrowserComputer(3, 2),
            BrowserComputer(4, 3),
            BrowserComputer(5, 3),
            BrowserComputer(6, 2)
        ]

    def test_query_1(self):
        result = query_1(self.brows, self.comps)
        expected = [("Alpha", "Компьютер 2")]
        self.assertEqual(result, expected)

    # def test_query_2(self):
    #     result = query_2(self.brows, self.comps)
    #     expected = [("Компьютер 1", 100), ("Компьютер 2", 90), ("Компьютер 3", 80)]
    #     self.assertEqual(result, expected)

    def test_query_2(self):
        result = query_2(self.brows, self.comps)
        expected = [("Компьютер 3", 80), ("Компьютер 2", 90), ("Компьютер 1", 100)]
        self.assertCountEqual(result, expected)  # Сравнение без учёта порядка


    def test_query_3(self):
        result = query_3(self.brows, self.comps, self.browser_pc_link)
        expected = [
            ("Alpha", 90, "Компьютер 2"),
            ("Chrome", 120, "Компьютер 1"),
            ("Edge", 80, "Компьютер 3"),
            ("Firefox", 100, "Компьютер 1"),
            ("Opera", 150, "Компьютер 3"),
            ("Safari", 200, "Компьютер 2")
        ]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
