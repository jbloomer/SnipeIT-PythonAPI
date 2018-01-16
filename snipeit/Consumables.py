import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context
import requests
try:
    requests.packages.urllib3.disable_warnings()
except AttributeError:
    pass
else:
    requests.packages.urllib3.disable_warnings()
try:
    from .packages.urllib3.exceptions import ResponseError
except:
    pass

import json

class Consumables(object):
    def __init__(self):
        pass

    def get(self, server, token, limit=None):
        if limit is not None:
            self.uri = '/api/v1/consumables?limit=' + str(limit)
        else:
            self.uri = '/api/v1/consumables'
        self.server = server + self.uri
        headers = {'Authorization': 'Bearer ' + token}
        results = requests.get(self.server, headers=headers)
        return results.content

    def create(self, server, token, payload):
        self.uri = '/api/v1/consumables'
        self.server = server + self.uri
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer ' + token}
        results = requests.post(self.server, headers=headers, data=payload)
        return json.dumps(results.json(),indent=4, separators=(',', ':'))

    def getID(self, server, token, asset_name):
        self.uri = '/api/v1/consumables?search='
        self.server = server + self.uri + asset_name
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer ' + token}
        results = requests.get(self.server, headers=headers)
        jsonData = json.loads(results.content)
        if len(jsonData['rows']) < 2 and jsonData['rows'][0]['id'] is not None:
            ConsumableID = jsonData['rows'][0]['id']
        return ConsumableID

    def viewID(self, server, token, ConsumableID):
        self.uri = '/api/v1/consumables/'
        self.server = server + self.uri + ConsumableID
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer ' + token}
        results = requests.get(self.server, headers=headers)
        return results.content
