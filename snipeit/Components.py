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

class Components(object):
    """Class to access components API  
    """
    def __init__(self):
        pass

    def get(self, server, token, limit=None, order='asc', expand=True, offset=None):
        """Get list of component data
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            order {string} -- Display order of data (asc / desc default:{asc})
            expand {boolean} -- Include detailed information or just text name (False)
        
        Keyword Arguments:
            limit {string} -- Limit the number of data returned by the server (default: {50})
        
        Returns:
            string -- List of components from the server, in JSON formatted
        """
        if limit is not None:
            self.uri = '/api/v1/components?limit={0}&order={1}'.format(str(limit),order)
        else:
            self.uri = '/api/v1/components?order={0}'.format(order)
        if offset is not None:
            self.uri = self.uri + '&offset={0}'.format(str(offset))            
        self.server = server + self.uri + '&expand={0}'.format(str(expand).lower())
        print(self.server)
        headers = {'Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)
        return results.content
        
    def search(self, server, token, limit=None, order='asc', keyword=None, offset=None):
        """Get list of components based on search keyword
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
        
        Keyword Arguments:
            limit {string} -- Limit the number of data returned by the server (default: {50})
        
        Returns:
            string -- List of components in JSON format.
        """
        if keyword is None:
            keyword = ""
        
        if limit is not None:
            self.uri = '/api/v1/components?limit={0}&order={1}'.format(str(limit),order)
        else:
            self.uri = '/api/v1/components?order={0}'.format(order)
        if offset is not None:
            self.uri = self.uri + '&offset={0}'.format(str(offset))            
        self.server = server + self.uri  + '&search={0}'.format(keyword)
        headers = {'Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)
        return results.content

    def create(self, server, token, payload):
        """create new component data
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            payload {string} -- name of the component
        
        Returns:
            string -- server response in JSON format
        """
        self.uri = '/api/v1/components'
        self.server = server + self.uri
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(token)}
        results = requests.post(self.server, headers=headers, data=payload)
        return json.dumps(results.json(),indent=4, separators=(',', ':'))

    def getDetailsByID(self, server, token, componentsID):
        """Get detailed information of component by ID
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            componentsID {string} -- ID of the component
        
        Returns:
            string -- Detailed information of component by ID
        """
        self.uri = '/api/v1/components/{0}'.format(componentsID)
        self.server = server + self.uri 
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)                
        return results.content

