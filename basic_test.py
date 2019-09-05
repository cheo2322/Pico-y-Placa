from pico_y_placa import PicoYPlaca

def main(number, date, time):
    if PicoYPlaca(number, date, time):
        print("Not allowed to circulate!")
    else:
        print("No problem :)")

main(2178, "2019,9,5", "12:30")        
main(3478, "2019,9,12", "12:30")
main(2170, "2019,9,6", "17:30")
main(2170, "2019,9,7", "17:30")
