import json
from jsonpath_ng import jsonpath
from jsonpath_ng.ext import parse

"""
This is a helper class for working with PropertySync documents.
"""

class Document:
    def __init__(self, json_string=None):
        
        self._json = json_string
        self.subdivisionlegals = []

        if "tags" in self._json["json"]:
            self.tags = self._json["json"]["tags"]
        else:
            self.tags = []

        if "id" in self._json:
            self.id = self._json["id"]
        else:
            self.id = None

        if "subdivisionLegal" in self._json["json"]:
            for legal in self._json["json"]["subdivisionLegal"]:
                self.subdivisionlegals.append(legal)

    # use magic methods to make the document properties accessible as attributes
    def __getattr__(self, name):
        if name in self._json["json"]:
            return self._json["json"][name]
        else:
            return None

    # serialize the doc to json    
    def get_json(self):
        return self._json
        
    # return subdivisionlegals where parcel matches a value
    def subdivisionlegals_with_parcel(self, parcel):
        return [legal for legal in self.subdivisionlegals if legal["parcel"] == parcel]
    
    def __str__(self):
        return json.dumps(self._json, indent=4)
    
    # replace  with "value" in "json_path" for this document 
    def replace(self, json_path, value):
        jsonpath_expr = parse(json_path)
        jsonpath_expr.find(self._json["json"])
        jsonpath_expr.update(self._json["json"], value)
                
    # find all nodes in the document that have a specific value
    def find(self, json_path):
        jsonpath_expr = parse(json_path)
        matches = jsonpath_expr.find(self._json["json"])
        if len(matches) > 0:
            return matches
            
        return False
    