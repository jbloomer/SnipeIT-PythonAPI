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

class Manufacturers(object):
    def __init__(self):
        """Class to access manufacturers API.
        """
        pass

    def get(self, server, token):
        """Get list of manufacturers
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
        
        Keyword Arguments:
            limit {string} -- Limit the number of data returned by the server (default: {50})
        
        Returns:
            string -- List of manufacturers in JSON format.
        """       
        self.uri = '/api/v1/manufacturers'  
        self.server = server + self.uri
        headers = {'Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)
        return results.content
        #return json.dumps(results.json(),indent=4, separators=(',', ':'))

    def create(self, server, token, payload):
        """Create new manufacturers data.
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            payload {string} -- Input parameters
        
        Returns:
            string -- server response in JSON format
        """
        self.uri = '/api/v1/manufacturers'
        self.server = server + self.uri
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(token)}
        results = requests.post(self.server, headers=headers, data=payload)
        return json.dumps(results.json(),indent=4, separators=(',', ':'))

    def getDetailsByID(self, server, token, manufacturersID):
        """Get detailed information of label by ID
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            manufacturersID {string} -- ID of the manufacturers
        
        Returns:
            string -- Detailed information of manufacturers by ID
        """
        self.uri = '/api/v1/manufacturers/{0}'.format(manufacturersID)
        self.server = server + self.uri
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)                
        return results.content

    
    def delete(self, server, token, manufacturersID):
        """Delete manufacturers data
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            manufacturersID {string} -- ID of the manufacturers
        
        Returns:
            string -- server response in JSON format
        """
        self.uri = '/api/v1/manufacturers/{0}'.format(manufacturersID)
        self.server = server + self.uri
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(token)}
        results = requests.delete(self.server, headers=headers)
        jsonData = json.loads(results.content)
        return jsonData['status']

    def updatemanufacturers(self, server, token, manufacturersID, payload):
        """[summary]
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            manufacturersID {string} -- ID of the manufacturers
            payload {string} -- Input parameters
        
        Returns:
            string -- server response in JSON format
        """
        self.uri = '/api/v1/manufacturers/{0}'.format(manufacturersID)
        self.server = server + self.uri
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(token)}
        results = requests.patch(self.server, headers=headers, data=payload)
        jsonData = json.loads(results.content)
        return jsonData['status']
