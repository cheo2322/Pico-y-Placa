from pico_y_placa import PicoYPlaca

assert(PicoYPlaca(2178, "2019,9,5", "12:30")==0)
assert(PicoYPlaca(3478, "2019,9,12", "12:30")==1)
assert(PicoYPlaca(2170, "2019,9,6", "17:30")==1)
assert(PicoYPlaca(2170, "2019,9,7", "17:30")==0)
assert(PicoYPlaca(134, "1998,6,22", "4:20")==0)
