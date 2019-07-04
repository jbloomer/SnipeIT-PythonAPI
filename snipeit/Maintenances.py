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

class Maintenances(object):
    def __init__(self):
        """Class to access maintenances API.
        """
        pass

    def get(self, server, token, limit=None, order='asc'):
        """Get list of maintenances
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
        
        Keyword Arguments:
            limit {string} -- Limit the number of data returned by the server (default: {50})
        
        Returns:
            string -- List of maintenances in JSON format.
        """
        if limit is not None:
            self.uri = '/api/v1/maintenances?limit=' + str(limit)
        else:
            self.uri = '/api/v1/maintenances'
        self.server = server + self.uri
        headers = {'Authorization': 'Bearer ' + token}
        results = requests.get(self.server, headers=headers)
        return results.content
        #return json.dumps(results.json(),indent=4, separators=(',', ':'))

    def search(self, server, token, limit=None, order='asc', keyword=None):
        """Get list of maintenances based on search keyword
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            order {string} -- Display order of data (asc / desc default:{asc})
        
        Keyword Arguments:
            limit {string} -- Limit the number of data returned by the server (default: {50})
        
        Returns:
            string -- List of maintenances in JSON format.
        """
        if keyword is None:
            keyword = ""
        
        if limit is not None:
            self.uri = '/api/v1/maintenances?limit=' + str(limit) + '&order=' + order 
        else:
            self.uri = '/api/v1/maintenances'  + '?order=' + order 
        self.server = server + self.uri  + '&search=' + keyword
        headers = {'Authorization': 'Bearer ' + token}
        results = requests.get(self.server, headers=headers)
        return results.content        

    def getMaintenanceByID(self, server, token, limit=None, order='asc', assetID=None):
        """Get maintenances information by asset ID
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            order {string} -- Display order of data (asc / desc default:{asc})
            assetID {string} -- Asset ID to be find

        
        Keyword Arguments:
            limit {string} -- Limit the number of data returned by the server (default: {50})
        
        Returns:
            string -- List of maintenances in JSON format.
        """
        if limit is not None:
            self.uri = '/api/v1/maintenances?limit=' + str(limit) + '&order=' + order
        else:
            self.uri = '/api/v1/maintenances' + '?order=' + order
        self.server = server + self.uri + '&asset_id=' + assetID
        headers = {'Authorization': 'Bearer ' + token}
        results = requests.get(self.server, headers=headers)
        return results.content
        #return json.dumps(results.json(),indent=4, separators=(',', ':'))

    def create(self, server, token, payload):
        """Create new maintenances data.
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            payload {string} -- Input parameters
        
        Returns:
            string -- server response in JSON format
        """
        self.uri = '/api/v1/maintenances'
        self.server = server + self.uri
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer ' + token}
        results = requests.post(self.server, headers=headers, data=payload)
        return json.dumps(results.json(),indent=4, separators=(',', ':'))
