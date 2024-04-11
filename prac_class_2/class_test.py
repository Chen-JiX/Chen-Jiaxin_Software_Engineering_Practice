import numpy as np
import cv2
import unittest


class Frame:
    def __init__(self):
        pass


class Table:
    def __init__(self, frame):
        self.table = frame

    def getRowNum(self):
        return len(self.table[0])

    def getColNum(self):
        return len(self.table[0][0])


class Recogniser:
    def __init__(self):
        pass

    def MakePhoto(self):
        pass

    def Recognise(self, frame):
        t = Table(frame)
        return t


class TestRecogniser(unittest.TestCase):
    def setUp(self):
        pass

    def test_check_empty_frame_recognition(self):
        r = Recogniser()
        size = 200, 100, 3
        f = np.zeros(size, dtype=np.uint8)
        t = r.Recognise(f)

        self.assertEqual(t.getRowNum(), 100)
        self.assertEqual(t.getColNum(), 3)

    def test_check_empty_table_recognition(self):
        r = Recogniser()
        f = cv2.imread('empty_table_10_10.jpg')  # Output pixel data
        t = r.Recognise(f)

        self.assertEqual(t.getColNum(), 3)
        self.assertEqual(t.getRowNum(), 1115)


if __name__ == "__main__":
    unittest.main()
