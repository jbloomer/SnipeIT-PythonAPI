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

class Models(object):
    def __init__(self):
        """Class to access models API.
        """
        pass

    def get(self, server, token, limit=None, order='asc', offset=None):
        """Get list of models
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            order {string} -- Display order of data (asc / desc default:{asc})
        
        Keyword Arguments:
            limit {string} -- Limit the number of data returned by the server (default: {50})
        
        Returns:
            string -- List of models in JSON format.
        """
        if limit is not None:
            self.uri = '/api/v1/models?limit={0}&order={1}'.format(str(limit), order)
        else:
            self.uri = '/api/v1/models?order={0}'.format(order) 
        if offset is not None:
            self.uri = self.uri + '&offset={0}'.format(str(offset))
        self.server = server + self.uri
        headers = {'Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)
        return results.content
        #return json.dumps(results.json(),indent=4, separators=(',', ':'))

    def search(self, server, token, limit=None, order='asc', keyword=None, offset=None):
        """Get list of models based on search keyword
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            order {string} -- Display order of data (asc / desc default:{asc})
        
        Keyword Arguments:
            limit {string} -- Limit the number of data returned by the server (default: {50})
        
        Returns:
            string -- List of models in JSON format.
        """
        if keyword is None:
            keyword = ""
        
        if limit is not None:
            self.uri = '/api/v1/models?limit={0}&order={1}'.format(str(limit), order)
        else:
            self.uri = '/api/v1/models?order={0}'.format(order)
        if offset is not None:
            self.uri = self.uri + '&offset={0}'.format(str(offset))
        self.server = server + self.uri  + '&search={0}'.format(keyword)
        headers = {'Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)
        return results.content

    def create(self, server, token, payload):
        """Create new model data.
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            payload {string} -- Input parameters
        
        Returns:
            string -- server response in JSON format
        """
        self.uri = '/api/v1/models'
        self.server = server + self.uri
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(token)}
        results = requests.post(self.server, headers=headers, data=payload)
        return json.dumps(results.json(),indent=4, separators=(',', ':'))

    def getDetailsByID(self, server, token, modelsID):
        """Get detailed information of label by ID
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            modelsID {string} -- ID of the model
        
        Returns:
            string -- Detailed information of modelsID by ID
        """
        self.uri = '/api/v1/models/{0}'.format(modelsID)
        self.server = server + self.uri
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)                
        return results.content

    
    def delete(self, server, token, companyID):
        """Delete model data
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            ModelsID {string} -- ID of the model
        
        Returns:
            string -- server response in JSON format
        """
        self.uri = '/api/v1/models/{0}'.format(companyID)
        self.server = server + self.uri
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(token)}
        results = requests.delete(self.server, headers=headers)
        jsonData = json.loads(results.content)
        return jsonData['status']

    def updateModel(self, server, token, companyID, payload):
        """[summary]
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            ModelsID {string} -- ID of the model
            payload {string} -- Input parameters
        
        Returns:
            string -- server response in JSON format
        """
        self.uri = '/api/v1/models/{0}'.format(companyID)
        self.server = server + self.uri 
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(token)}
        results = requests.patch(self.server, headers=headers, data=payload)
        jsonData = json.loads(results.content)
        return jsonData['status']
