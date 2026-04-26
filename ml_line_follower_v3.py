import RPi.GPIO as GPIO
import time
import joblib
import pandas as pd
from collections import deque

GPIO.setmode(GPIO.BCM)

# -------- IR PINS --------
IR_PINS = [4,17,27,22,5]

# -------- MOTOR PINS --------
IN1, IN2, ENA = 6,13,18
IN3, IN4, ENB = 19,26,16

for p in IR_PINS:
    GPIO.setup(p, GPIO.IN)

GPIO.setup([IN1,IN2,ENA,IN3,IN4,ENB], GPIO.OUT)

pwmL = GPIO.PWM(ENA,1000)
pwmR = GPIO.PWM(ENB,1000)

pwmL.start(0)
pwmR.start(0)

# -------- SPEED --------
RUN_SPEED = 34
TURN_SPEED = 30
TURN_TIME = 0.15

# -------- LOAD MODEL --------
model = joblib.load("line_model_v3.pkl")

# -------- FILTER --------
action_buffer = deque(maxlen=3)

# -------- MOTOR FUNCTIONS --------
def forward():
    GPIO.output(IN1,1)
    GPIO.output(IN2,0)
    GPIO.output(IN3,0)
    GPIO.output(IN4,1)
    pwmL.ChangeDutyCycle(RUN_SPEED)
    pwmR.ChangeDutyCycle(RUN_SPEED)

def left():
    GPIO.output(IN1,0)
    GPIO.output(IN2,0)
    GPIO.output(IN3,0)
    GPIO.output(IN4,1)
    pwmL.ChangeDutyCycle(0)
    pwmR.ChangeDutyCycle(TURN_SPEED)

def right():
    GPIO.output(IN1,1)
    GPIO.output(IN2,0)
    GPIO.output(IN3,0)
    GPIO.output(IN4,0)
    pwmL.ChangeDutyCycle(TURN_SPEED)
    pwmR.ChangeDutyCycle(0)

def stop():
    pwmL.ChangeDutyCycle(0)
    pwmR.ChangeDutyCycle(0)

print("ML Line Follower Running (v3 Stable)")

try:
    while True:
        ir = [GPIO.input(p) for p in IR_PINS]

        print("IR:", ir)

        # ❌ NO LINE → STOP (prevents random turning)
        if ir == [1,1,1,1,1]:
            stop()
            continue

        X = pd.DataFrame([ir], columns=["S1","S2","S3","S4","S5"])
        action = model.predict(X)[0]

        action_buffer.append(action)

        # Majority decision (noise filtering)
        if action_buffer.count(action) >= 2:

            if action == 0:
                forward()

            elif action == 1:
                left()
                time.sleep(TURN_TIME)

            elif action == 2:
                right()
                time.sleep(TURN_TIME)

        time.sleep(0.03)

except KeyboardInterrupt:
    stop()
    GPIO.cleanup()