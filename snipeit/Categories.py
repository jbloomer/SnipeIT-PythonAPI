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

class Categories(object):
    def __init__(self):
        """Class to access categories API.
        """
        pass

    def get(self, server, token, limit=None, order='asc', offset=None):
        """Get list of categories
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            offset {string} -- Starting offset to get the data
        
        Keyword Arguments:
            limit {string} -- Limit the number of data returned by the server (default: {50})
        
        Returns:
            string -- List of categories in JSON format.
        """
        if limit is not None:
            self.uri = '/api/v1/categories?limit={0}'.format(str(limit))
            if offset is not None:
                self.uri = self.uri + '&offset={0}'.format(str(offset))
        else:
            self.uri = '/api/v1/categories'
            if offset is not None:
                self.uri = self.uri + '?offset={0}'.format(str(offset))        
        self.server = server + self.uri
        headers = {'Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)
        return results.content
        #return json.dumps(results.json(),indent=4, separators=(',', ':'))

    def search(self, server, token, limit=None, order='asc', keyword=None, offset=None):
        """Get list of categories based on search keyword
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            order {string} -- Display order of data (asc / desc default:{asc})
            offset {string} -- Starting offset to get the data
        
        Keyword Arguments:
            limit {string} -- Limit the number of data returned by the server (default: {50})
        
        Returns:
            string -- List of categories in JSON format.
        """
        if keyword is None:
            keyword = ""
        
        if limit is not None:
            self.uri = '/api/v1/categories?limit={0}&order={1}'.format(str(limit), order)
        else:
            self.uri = '/api/v1/categories?order={0}'.format(order)
        if offset is not None:
            self.uri = self.uri + '&offset={0}'.format(str(offset))     
        self.server = server + self.uri  + '&search={0}'.format(keyword)
        headers = {'Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)
        return results.content        

    def create(self, server, token, payload):
        """Create new categories data.
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            payload {string} -- Input parameters
        
        Returns:
            string -- server response in JSON format
        """
        self.uri = '/api/v1/categories'
        self.server = server + self.uri
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(token)}
        results = requests.post(self.server, headers=headers, data=payload)
        return json.dumps(results.json(),indent=4, separators=(',', ':'))

    def getDetailsByID(self, server, token, categoriesID):
        """Get detailed information of label by ID
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            categoriesID {string} -- ID of the categories
        
        Returns:
            string -- Detailed information of categories by ID
        """
        self.uri = '/api/v1/categories/{0}'.format(categoriesID)
        self.server = server + self.uri
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)                
        return results.content

    
    def delete(self, server, token, categoriesID):
        """Delete categories data
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            categoriesID {string} -- ID of the categories
        
        Returns:
            string -- server response in JSON format
        """
        self.uri = '/api/v1/categories/{0}'.format(categoriesID)
        self.server = server + self.uri
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(token)}
        results = requests.delete(self.server, headers=headers)
        jsonData = json.loads(results.content)
        return jsonData['status']

    def updatecategories(self, server, token, categoriesID, payload):
        """[summary]
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            categoriesID {string} -- ID of the categories
            payload {string} -- Input parameters
        
        Returns:
            string -- server response in JSON format
        """
        self.uri = '/api/v1/categories/{0}'.format(categoriesID)
        self.server = server + self.uri
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(token)}
        results = requests.patch(self.server, headers=headers, data=payload)
        jsonData = json.loads(results.content)
        return jsonData['status']
