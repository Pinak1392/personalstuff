from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
cors = CORS(app)

games = {}

@app.route("/", methods=['GET','POST'])
def data():
  li = []
  for x in sorted(games):
    li.append(x)

  return json.dumps(li)

@app.route("/give", methods=['GET','POST'])
def give():
  send = request.values.get('q')
  y = json.loads(send)
  
  userKey = "ae80182d58acf6c5238e3b1bfd74bf2b"
  game = y['Game']

  resp = requests.post("https://api-v3.igdb.com/games/", headers={"user-key":userKey},data=f"search \"{game}\"; fields rating, summary; limit 1;")
  respPy = resp.json()[0]
  
  desc = respPy['summary']
  rating = round(respPy['rating']/10)

  return jsonify({"Score":rating, "Description":desc})

@app.route("/add", methods=['GET','POST'])
def addKey():
  add = json.loads(request.values.get('q'))
  for a in add:
    games[a] = add[a]
  
  return jsonify(result = '200')


@app.route("/req", methods=['GET','POST'])
def req():
  get = request.values.get('q')
  return json.dumps(games[get])



if __name__ == '__main__':
  app.run(debug=True)