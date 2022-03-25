# https://thingspeak.com/channels/1682626
import serial
import requests
from requests.exceptions import HTTPError

API_KEY = "SKANN5E6L75MDFV8"

def write_feed(field, feed):
        try:
            url = f"https://api.thingspeak.com/update?api_key={API_KEY}&{field}={feed}"
            response = requests.get(url)
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')

def start_feed(ser):
    try:
        while True:
            X = ser.readline().decode()
            Y = ser.readline().decode()
            print(X, Y)
            write_feed("field1", X)
            write_feed("field2", Y)
    finally:
        ser.close()

if __name__=="__main__":
    ser = serial.Serial('COM3', 9600, timeout=1000)
    start_feed(ser)
