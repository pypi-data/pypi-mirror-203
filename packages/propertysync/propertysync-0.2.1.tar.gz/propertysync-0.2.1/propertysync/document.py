import json
from jsonpath_ng import jsonpath, parse

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
        
    # return subdivisionlegals where parcel matches a value
    def subdivisionlegals_with_parcel(self, parcel):
        return [legal for legal in self.subdivisionlegals if legal["parcel"] == parcel]
    
    def __str__(self):
        return json.dumps(self._json, indent=4)
    
    # replace "find" with "replace" in "json.node" for this document 
    def replace(self, find, replace, json_node):
        jsonpath_expr = parse(json_node)
        matches = jsonpath_expr.find(self._json["json"])
        for match in matches:
            if match.value == find:
                match.value = replace

                
        
    # find all nodes in the document that have a specific value
    def find(self, find, json_node):
#         expression = json_node + "[?(@== '" + find + "')]"

        print (json_node)

        jsonpath_expr = parse(expression)
        matches = jsonpath_expr.find(self._json["json"])
        if len(matches) > 0:
            return True
        else:
            return False
        

       