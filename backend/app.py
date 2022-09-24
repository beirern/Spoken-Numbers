from flask import Flask, request
from main import boxing_combination

app = Flask(__name__)

@app.route('/boxing', methods=['GET'])
def boxing():
  combos = request.args.get('combos', type=int)
  rounds = request.args.get('rounds', type=int)
  boxing_combination(combos, rounds)
  return "Hi!"
