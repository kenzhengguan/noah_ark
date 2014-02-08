# -*- coding: utf-8 -*-

import simplejson as json

from flask import Flask
from flask import request
from flask import Response

from models import Ark, Candidate

app = Flask(__name__)

# restful route

# ark route

@app.route("/arks", methods=["GET", "POST"])
def arks():
  # create a new ark
  if request.method == "POST":
    pass
  # ark list
  elif request.method == "GET":
    pass

@app.route("/arks/<string:ark_id>", methods=["PUT", "DELETE", "GET"])
def ark_action(ark_id):
  # update ark
  if request.method == "PUT":
    pass
  # delete ark
  elif request.method == "DELETE":
    pass
  # get ark detail
  elif request.method == "GET":
    pass

# get ark passenger list
# get passenger info through url /candidates/:candidate_id
@app.route("/arks/<string:ark_id>/passengers", methods=["GET"])
def ark_passenger(ark_id):
  pass

# candidate route

@app.route("/candidates", methods=["GET", "POST"])
def candidates():
  # create a new candidate
  if request.method == "POST":
    pass
  # candidate list
  elif request.method == "GET":
    pass

@app.route("/candidates/<string:candidate_id>", methods=["PUT", "DELETE", "GET"])
def candidate_action(candidate_id):
  # update candidate
  if request.method == "PUT":
    pass
  # delete candidate
  elif request.method == "DELETE":
    pass
  # get candidate detail
  elif request.method == "GET":
    pass

# candiadate actions

# order ticket
@app.route("/candidates/<string:candidate_id>/order", method=["POST"])
def order_ticket(candidate_id):
  pass

# cancel order
@app.route("/candidates/<string:candidate_id>/orders/<string:order_id>/cancel", method=["POST"])
def order_ticket(candidate_id):
  pass


if __name__ == "__main__":
  app.run()
