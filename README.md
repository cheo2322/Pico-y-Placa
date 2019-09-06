# Pico-y-Placa
This program predict whether a car could or not circulate using the Pico y Placa (Hoy no circula) system of Quito. The inputs are a license plate number (the full number, not the last digit), a date (as a String), and a time, and the program return whether or not that car can be on the road.

Rules:

A car is not allowed to circulate under the next conditions:

- Depending on the day and the last number of the plate:

Monday:     1,2

Tuesday:    3,4

Wednesday:  5,6

Thursday:   7,8

Friday:     9,0

- Before September 9th, 2019 the next schedule rules:

Morning:   7:00 - 9:30

Afternoon: 16:00 - 19:30

- From September 9th, 2019:

Everyday: 5:00 - 20:00

In the 'basic_test' script we test the program with some basic examples entered
manually.

In the 'manual_test.py' script the console asks for the inputs, then process 
it and returns the respective message (Not integrated).

In the 'automated_test.py' file we have several automatic test for this program (not integrated).
