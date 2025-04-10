from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/suma/<int:num1>/<int:num2>')
def suma(num1,num2):
    return render_template('suma.html',num1=num1,num2=num2)

@app.route('/resta/<int:num1>/<int:num2>')
def resta(num1,num2):
    return render_template('resta.html',num1=num1,num2=num2)

@app.route('/multiplicacion/<int:num1>/<int:num2>')
def multiplicacion(num1,num2):
    return render_template('multiplicacion.html',num1=num1,num2=num2)

@app.route('/division/<int:num1>/<int:num2>')
def division(num1,num2):
    return render_template('division.html',num1=num1,num2=num2)
