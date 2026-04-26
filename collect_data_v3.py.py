import RPi.GPIO as GPIO
import time
import csv

GPIO.setmode(GPIO.BCM)

IR_PINS = [4,17,27,22,5]

for p in IR_PINS:
    GPIO.setup(p, GPIO.IN)

file = open("ir_data_v3.csv", "w", newline="")
writer = csv.writer(file)

# Header
writer.writerow(["S1","S2","S3","S4","S5","Action"])

print("Press:")
print("f = Forward | l = Left | r = Right | q = Quit")

try:
    while True:
        ir = [GPIO.input(p) for p in IR_PINS]
        print("IR:", ir)

        key = input("Enter action: ")

        if key == 'f':
            writer.writerow(ir + ["Forward"])

        elif key == 'l':
            writer.writerow(ir + ["Left"])

        elif key == 'r':
            writer.writerow(ir + ["Right"])

        elif key == 'q':
            break

except KeyboardInterrupt:
    pass

file.close()
GPIO.cleanup()
print("Data saved to ir_data_v3.csv")