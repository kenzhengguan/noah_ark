# -*- coding: utf-8 -*-

from pymongo import MongoClient
from bson.objectid import ObjectId

import managers


client = MongoClient('mongodb://localhost:27017/')
db = client.noah_database

managers.db = db

__all__ = ["Ark", "Candidate"]

class AttrNotFound(Exception):
  def __init__(self, class_name, attr_name):
    self.msg = """{class_name} object has no Attribute {attr}.""".format(
      class_name=class_name, 
      attr=attr_name
    )

  def __str__(self):
    return self.msg

class InitMixin(object):
  """docstring for InitMixin"""
  def __init__(self, **kwargs):
    self._update_attrs(kwargs)

  def _update_attrs(self, obj_dict):
    for key, val in obj_dict.iteritems():
      if key not in self._attrs:
        raise AttrNotFound(self.__class__.__name__, key)
      setattr(self, key, val)

  @property
  def id(self):
    return getattr(self, "_id", None)

  @id.setter
  def id(self, value):
    self._id = value

  def save(self):
    data = self._to_dict()
    obj_id = self.table.save(data)
    self.id = obj_id

  def _to_dict(self):
    _dict = {}
    for key in self._attrs:
      attr = key != "_id" and key or "id"
      val = getattr(self, attr, None)
      if val:
        _dict[key] = val
    return _dict
    

class Ark(InitMixin):
  table = managers.get_ark_collection()
  _attrs = ["_id", "load", "ark_type", "description"]

class Candidate(InitMixin):
  table = managers.get_candidate_collection()
  _attrs = ["_id", "name", "age", ]
    

if __name__ == '__main__':
  ark_demos = [{
      "load": 700, 
      "ark_type": "human", 
      "description": "human 1"
    }, {
      "load": 700, 
      "ark_type": "human", 
      "description": "human 2"
    }, {
      "load": 1000, 
      "ark_type": "animal", 
      "description": "animal 1"
    }, {
      "load": 1000, 
      "ark_type": "animal", 
      "description": "animal 2"
    }, {
      "load": 700, 
      "ark_type": "human", 
      "description": "human 3"
    }
  ]
  for ark_demo in ark_demos:
    try:
      ark = Ark(**ark_demo)
      print ark.load, ark.ark_type, ark.description
      # ark.save()
    except AttrNotFound, e:
      raise e
  arks = Ark.table.find()

  # for ark in arks:
  #   print ark
    # print db.arks.find_one(spec_or_id=ark["_id"])
    # db.arks.remove(ark)
  for ark in Ark.table.find():
    print ark