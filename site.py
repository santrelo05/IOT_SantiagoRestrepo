from flask import Flask, render_template, jsonify, request
import sqlite3
import sys

db_path = 'Sensor_Database/sensorData.db'


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/creardb')
def creardb():
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS temperatura")
    cur.execute("CREATE TABLE temperatura (idsensor NUMERIC, timestamp DATETIME, temperatura NUMERIC, lat NUMERIC, lon NUMERIC)")
    cur.execute("DROP TABLE IF EXISTS humedad")
    cur.execute("CREATE TABLE humedad (idsensor NUMERIC, timestamp DATETIME, humedad NUMERIC, lat NUMERIC, lon NUMERIC)")
    con.commit()
    con.close()
    return "crear base de datos",201

@app.route('/send_temperatura', methods=['POST'])
def send_temperatura():
    values = request.data
    print(values)
    print(values.split(";")[0])
    print(values.split(";")[1])
    print(values.split(";")[2])
    print(values.split(";")[3])
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute("INSERT INTO temperatura VALUES(" + values.split(";")[0] + "," + "datetime('now')," + values.split(";")[1] + "," + values.split(";")[2] + "," + values.split(";")[3] + ")")
    con.commit()
    con.close()
    return "ok",201

@app.route("/temperatura")
def printempera():
    sensorID = []
    sensorTime = []
    sensorTemp = []
    sensorLat = []
    sensorLon = []
    con = sqlite3.connect(db_path)
    curs = con.cursor()
    for fila in curs.execute("SELECT * FROM temperatura"):
        sensorID.append(fila[0])
        sensorTime.append(fila[1])
        sensorTemp.append(fila[2])
        sensorLat.append(fila[3])
        sensorLon.append(fila[4])
    con.close()
    print(sensorID[0] +" "+ sensorTime[0]+" "+sensorTemp[0]+" "+sensorLat[0]+" "+sensorLon[0])
    leyenda = 'Temperatura sensor'
    etiquetas = sensorTime
    valores = sensorTemp
    return sensorID[0] +" "+ sensorTime[0]+" "+sensorTemp[0]+" "+sensorLat[0]+" "+sensorLon[0],201

@app.route('/send_humedad', methods=['POST'])
def send_humedad():
    values = request.data
    print(values)
    print(values.split(";")[0])
    print(values.split(";")[1])
    print(values.split(";")[2])
    print(values.split(";")[3])
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute("INSERT INTO humedad VALUES(" + values.split(";")[0] + "," + "datetime('now')," + values.split(";")[1] + "," + values.split(";")[2] + "," + values.split(";")[3] + ")")
    con.commit()
    con.close()
    return "ok",201

@app.route("/humedad")
def prinhumedad():
    sensorID = []
    sensorTime = []
    sensorTemp = []
    sensorLat = []
    sensorLon = []
    con = sqlite3.connect(db_path)
    curs = con.cursor()
    for fila in curs.execute("SELECT * FROM humedad"):
        sensorID.append(fila[0])
        sensorTime.append(fila[1])
        sensorTemp.append(fila[2])
        sensorLat.append(fila[3])
        sensorLon.append(fila[4])
    con.close()
    print(sensorID[0] +" "+ sensorTime[0]+" "+sensorTemp[0]+" "+sensorLat[0]+" "+sensorLon[0])
    leyenda = 'Temperatura sensor'
    etiquetas = sensorTime
    valores = sensorTemp
    return sensorID[0] +" "+ sensorTime[0]+" "+sensorTemp[0]+" "+sensorLat[0]+" "+sensorLon[0],201


if __name__ == '__main__':
        app.run(debug=True,host='0.0.0.0',port=80)
