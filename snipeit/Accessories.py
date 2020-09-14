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

class Accessories(object):
    """Class to access accessories API.    
    """
    def __init__(self):
        pass

    def get(self, server, token, limit=None, offset=None):
        """Get list of accessories
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            offset {string} -- Starting offset to get the data
        
        Keyword Arguments:
            limit {string} -- Limit the number of data returned from the server (default: {50})
        
        Returns:
            string -- List of accessories from the server, in JSON formatted
        """
        if limit is not None:
            self.uri = '/api/v1/accessories?limit={0}'.format(str(limit))
            if offset is not None:
                self.uri = self.uri + '&offset={0}'.format(str(offset))
        else:
            self.uri = '/api/v1/accessories'
            if offset is not None:
                self.uri = self.uri + '?offset={0}'.format(str(offset))            
        self.server = server + self.uri
        headers = {'Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)
        return results.content
        
    def search(self, server, token, limit=None, order='asc', keyword=None):
        """Get list of accessories based on search keyword
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
        
        Keyword Arguments:
            limit {string} -- Limit the number of data returned by the server (default: {50})
        
        Returns:
            string -- List of accessories in JSON format.
        """
        if keyword is None:
            keyword = ""
        
        if limit is not None:
            self.uri = '/api/v1/accessories?limit={0}&order={1}'.format(str(limit),order)            
        else:
            self.uri = '/api/v1/accessories?order={0}'.format(order)               
        self.server = server + self.uri  + '&search={0}'.format(keyword)
        headers = {'Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)
        return results.content

    def create(self, server, token, payload):
        """Create new accessories data.
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            payload {string} -- Accessories input parameters
        
        Returns:
            string -- data creation result
        """
        self.uri = '/api/v1/accessories'
        self.server = server + self.uri
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(token)}
        results = requests.post(self.server, headers=headers, data=payload)
        return json.dumps(results.json(),indent=4, separators=(',', ':'))

    def getDetailsByID(self, server, token, accessoriesID):
        """Get the details of accessory data.
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            accessories_ID {integer} -- ID of the accessories to be found
        
        Returns:
            string -- Detailed information of an accessory
        """
        self.uri = '/api/v1/accessories/'
        self.server = server + self.uri + str(accessoriesID)
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)        
        return results.content
   
