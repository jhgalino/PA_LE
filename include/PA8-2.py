import unittest


def engg(s: str):
    if len(s) < 4:
        return "false"
    else:
        s = list(s)
        if (s[0] == "e" or s[0] == "E") and s[1] == "N" :
            s.pop(0)
            while s[0] == "N":
                s.pop(0)
            s = "".join(s)
            if s == "GG":
                return "true"
            else:
                return engg(s)
        else:
            return "false"


class Tester(unittest.TestCase):
    def test_func(self):
        self.assertEqual("false", engg("ENGGENGG"))
        self.assertEqual("false", engg("EnGG"))
        self.assertEqual("false", engg("EeNGG"))
        self.assertEqual("false", engg("E"))
        self.assertEqual("false", engg("EGG"))
        self.assertEqual("false", engg("GG"))
        self.assertEqual("false", engg("ENGGEE"))
        self.assertEqual("false", engg("ENEE"))
        self.assertEqual("false", engg("NGG"))
        self.assertEqual("false", engg("eNGGee"))
        self.assertEqual("false", engg("eNee"))


if __name__ == "__main__":
    unittest.main()
