from flask import Flask
from controllers import CalcController, Index

app = Flask('app')

@app.route('/')
def index():
  return Index.index()

@app.route('/div/<num1>/<num2>')
def div(num1, num2):
  return CalcController.div(num1, num2)
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81)