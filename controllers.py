from flask import Flask, render_template

class Index():
  def index():
    return render_template('index.html')

class CalcController():
  def div(num1, num2):
    if int(num2) == 0:
      return 'Divisão por zero!'
    else:
      return f'Div = {int(num1) / int(num2)}'