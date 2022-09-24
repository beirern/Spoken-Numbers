from flask import Flask, request
from flask_cors import cross_origin
from main import boxing_combination

app = Flask(__name__)

@app.route('/', methods=['GET'])
def health_check():
  return 'OK'

@app.route('/boxing', methods=['GET'])
@cross_origin()
def boxing():
  combos = request.args.get('combos', type=int)
  rounds = request.args.get('rounds', type=int)

  return boxing_combination(combos, rounds) 

if __name__ == '__main__':
  app.run(host='0.0.0.0')