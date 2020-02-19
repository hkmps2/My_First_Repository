import flask
import serial
from time import sleep
import sys

COM_PORT = 'COM3'  # 請自行修改序列埠名稱
BAUD_RATES = 115200
ser = serial.Serial(COM_PORT, BAUD_RATES)

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    print('connected')
    return "<h1>Hello</h1>"

@app.route('/red', methods=['GET'])
def turn():
    ser.write(b'scr1e')                  #ser的write (b'scr1e')的b是變成byte                      
    return "<h1>Red On</h1>"

@app.route('/red10ms', methods=['GET'])
def red10ms():
    ser.write(b'sdr010e')
    return "<h1>red10ms</h1>"

@app.route('/red5ms', methods=['GET'])
def red5ms():
    ser.write(b'sdr005e')
    return "<h1>red5ms</h1>"

@app.route('/yellow', methods=['GET'])
def yellow():
    ser.write(b'scy1e')
    return "<h1>yellow ON</h1>"

@app.route('/yellow10ms', methods=['GET'])
def yellow10ms():
    ser.write(b'sdy010e')
    return "<h1>yellow10ms</h1>"

@app.route('/yellow5ms', methods=['GET'])
def yellow5ms():
    ser.write(b'sdy005e')
    return "<h1>yellow5ms</h1>"

@app.route('/blue', methods=['GET'])
def blue():
    ser.write(b'scb1e')
    return "<h1>blue On</h1>"

@app.route('/blue10ms', methods=['GET'])
def blue10ms():
    ser.write(b'sdb010e')
    return "<h1>blue10ms</h1>"

@app.route('/blue5ms', methods=['GET'])
def blue5ms():
    ser.write(b'sdb005e')
    return "<h1>blue5ms</h1>"

@app.route('/redoff', methods=['GET'])
def redoff():
    ser.write(b'scr0e')
    return "<h1>redoff</h1>"

@app.route('/yellowoff', methods=['GET'])
def yellowoff():
    ser.write(b'scy0e')
    return "<h1>yellowoff</h1>"

@app.route('/blueoff', methods=['GET'])
def blueoff():
    ser.write(b'scb0e')
    return "<h1>blueoff</h1>"

                                             

@app.route('/zino', methods=['GET'])
def zino():
    return '{"success":"true","result":{"resource_id":"O-A0003-001","fields":[{"id":"lat","type":"Double"}]}'

app.run(host="0.0.0.0", port=8090)