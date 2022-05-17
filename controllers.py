from flask import Flask, render_template

class Index():
  def index():
    return render_template('index.html')

class CalcController():
  def div(num1, num2):
    return f'Div = {int(num1) / int(num2)}'