import json
from .document import Document

"""
This is a helper class for working with PropertySync batches.
"""

class Batch:
    
    def __init__(self, json_string=None):
        self.documents = []
        self._json = json_string

        if "id" in self._json:
            self.id = self._json["id"]
        else:
            self.id = None        

        for doc in self._json["documents"]:
            self.documents.append(Document(doc))

    # serialize the doc to json
    def __str__(self):
        return json.dumps(self._json, indent=4)
    
    def __len__(self):
        return len(self.documents)
    
    def get_json(self):
        return self._json

    def documents_with_tags(self, tags):
        return [doc for doc in self.documents if set(tags).issubset(set(doc.tags))]
    
    def documents_without_tags(self, tags):
        return [doc for doc in self.documents if not set(tags).issubset(set(doc.tags))]
    
    # get documents with a specific instrumentType value
    def documents_with_instrument_type(self, instrument_type):
        return [doc for doc in self.documents if doc.instrumentType == instrument_type]
    
    # get all of the instrumentNumbers for a given instrumentType, or all instrumentNumbers if no instrumentType is specified
    def instrument_numbers(self, instrument_type_filter = None):
        if instrument_type_filter:
            return [doc.instrumentNumber for doc in self.documents if doc.instrumentType == instrument_type_filter]
        else:
            return [doc.instrumentNumber for doc in self.documents]
        
    # replace "find" with "replace" in "json.node" for all documents in the batch
    def replace(self, find, replace, json_node):
        for doc in self.documents:
            doc.replace(find, replace, json_node)

    # find all documents in the batch that have a specific value in a specific json node
    def find(self, find, json_node):
        return [doc for doc in self.documents if doc.find(find, json_node)]