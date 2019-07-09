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

class Locations(object):
    """Class to access Location API    
    """
    def __init__(self):
        pass

    def get(self, server, token, limit=None,order='asc', offset=None):
        """Get list of locations.
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            order {string} -- Display order of data (asc / desc default:{asc})
        
        Keyword Arguments:
            limit {string} -- Limit the number of data returned by the server (default: {50})
        
        Returns:
            string -- List of locations from the server, in JSON formatted
        """
        if limit is not None:
            self.uri = '/api/v1/locations?limit={0}'.format(str(limit))
            if offset is not None:
                self.uri = self.uri + '&offset={0}'.format(str(offset))
        else:
            self.uri = '/api/v1/locations'
            if offset is not None:
                self.uri = self.uri + '?offset={0}'.format(str(offset))
        self.server = server + self.uri
        headers = {'Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)
        return results.content

    def search(self, server, token, limit=None, order='asc', keyword=None):
        """Get list of locations based on search keyword
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
        
        Keyword Arguments:
            limit {string} -- Limit the number of data returned by the server (default: {50})
        
        Returns:
            string -- List of locations in JSON format.
        """
        if keyword is None:
            keyword = ""
        
        if limit is not None:
            self.uri = '/api/v1/locations?limit={0}&order={1}'.format(str(limit),order)
        else:
            self.uri = '/api/v1/locations?order={0}'.format(order)                  
        self.server = server + self.uri  + '&search={0}'.format(keyword)
        headers = {'Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)
        return results.content

    def create(self, server, token, payload):
        """Create new location data.
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            payload {string} -- Input parameters
        
        Returns:
            string -- Server response in JSON
        """
        self.uri = '/api/v1/locations'
        self.server = server + self.uri
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(token)}
        results = requests.post(self.server, headers=headers, data=payload)
        return json.dumps(results.json(),indent=4, separators=(',', ':'))

    def getDetailsByID(self, server, token, locationID):
        """Get detailed location information by ID.
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            locationID {string} -- Location ID to be searched
        
        Returns:
            string -- Detailed information of a location
        """
        self.uri = '/api/v1/locations/{0}'.format(locationID)
        self.server = server + self.uri
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)        
        return results.content

    def updateLocation(self, server, token, LocationID, payload):
        """Update location data information
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            LocationID {string} -- ID of the location to be updated
            payload {string} -- input parameters
        
        Returns:
            string -- response message for server in JSON
        """
        self.uri = '/api/v1/locations/{0}'.format(LocationID)
        self.server = server + self.uri
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(token)}
        results = requests.patch(self.server, headers=headers, data=payload)
        jsonData = json.loads(results.content)
        return jsonData['status']

    def delete(self, server, token, LocationID):
        """Delete a location based on its location ID
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            LocationID {string} -- Location ID to be deleted
        
        Returns:
            string -- response message for server in JSON
        """
        self.uri = '/api/v1/locations/{0}'.format(LocationID)
        self.server = server + self.uri
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(token)}
        results = requests.delete(self.server, headers=headers)
        jsonData = json.loads(results.content)
        return jsonData['status']
