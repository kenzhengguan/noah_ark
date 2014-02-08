# -*- coding: utf-8 -*-

from pymongo import MongoClient
from bson.objectid import ObjectId

# from .models import Ark, Candidate

client = MongoClient('mongodb://localhost:27017/')
db = client.test_database

def get_ark_collection():
  return db.arks

def get_candidate_collection():
  return db.candidates

# ArkManager = db.arks

# CandidateManager = db.candidates

if __name__ == '__main__':
  for ark in ArkManager.find():
    print ark