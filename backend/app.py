from flask import Flask, request
from main import boxing_combination

app = Flask(__name__)

@app.route('/boxing', methods=['GET'])
def boxing():
  combos = request.args.get('combos', type=int)
  rounds = request.args.get('rounds', type=int)
  return boxing_combination(combos, rounds)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)