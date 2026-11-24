import unittest

def grade(avg):
    if avg >= 90:
        return "S"
    elif avg >= 80:
        return "A"
    elif avg >= 65:
        return "B"
    elif avg >= 50:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"

class TestGrade(unittest.TestCase):
    def test_grades(self):
        self.assertEqual(grade(95), "S")
        self.assertEqual(grade(85), "A")
        self.assertEqual(grade(70), "B")
        self.assertEqual(grade(55), "C")
        self.assertEqual(grade(45), "D")
        self.assertEqual(grade(30), "F")

if __name__ == "__main__":
    unittest.main()