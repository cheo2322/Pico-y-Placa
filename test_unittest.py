import pico_y_placa
import unittest

class Test_PicoYPlaca(unittest.TestCase):
    def test_pico_y_placa(self):
        self.assertFalse(pico_y_placa.PicoYPlaca(2178, "2019,9,5", "12:30"))
        self.assertTrue(pico_y_placa.PicoYPlaca(3478, "2019,9,12", "12:30"))
        self.assertTrue(pico_y_placa.PicoYPlaca(2170, "2019,9,6", "17:30"))
        self.assertFalse(pico_y_placa.PicoYPlaca(2170, "2019,9,7", "17:30"))
        self.assertFalse(pico_y_placa.PicoYPlaca(134, "1998,6,22", "4:20"))

if __name__ == '__main__':
    unittest.main()
