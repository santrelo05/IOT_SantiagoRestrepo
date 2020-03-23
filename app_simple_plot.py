from flask import Flask
from flask import render_template
from datetime import time
 
app = Flask(__name__)
 
 
@app.route("/simple_plot")
def chart():
    leyenda = 'Meses'
    etiquetas = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto","Septiembre", "Octubre", "Noviembre", "Diciembre"]
    valores = [10, 9, 8, 7, 6, 4, 7, 8, 5, 4, 8, 1]
    return render_template('chart.html', values=valores, labels=etiquetas, legend=leyenda)
 
 
if __name__ == "__main__":
    app.run(debug=True)