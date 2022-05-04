import time
from flask import Flask
import json
from multiprocessing import Process
import RPi.GPIO as GPIO

# The GPIO pin number we have assigned to the door sensor.
door_sensor_pin = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(door_sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

app = Flask(__name__)

# Variables
is_open = False


# App routes
@app.route("/")
def index():
    return "It Works! Try interacting with /state instead"


@app.route("/state", methods=['GET'])
def state():
    return fetchState()


def fetchState():
    return json.dumps({"is_active": str(is_open).lower()}), 200


def record_loop():
    while True:
        global is_open
        is_open = GPIO.input(door_sensor_pin)
        time.sleep(1)


if __name__ == "__main__":
    p = Process(target=record_loop)
    p.start()
    app.run(host="0.0.0.0")
    p.join()
