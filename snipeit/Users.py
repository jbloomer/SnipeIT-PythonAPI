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

class Users(object):
    """Class to access users API.
    """
    def __init__(self):
        pass

    def get(self, server, token, limit=None, order='asc', offset=None):
        """Get list of user data.
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            order {string} -- Display order of data (asc / desc default:{asc})
        
        Keyword Arguments:
            limit {string} -- Limit the number of data returned by the server (default: {50})
        
        Returns:
            string -- list of user data in JSON format
        """
        if limit is not None:
            self.uri = '/api/v1/users?limit={0}&order={1}'.format(str(limit), order)
        else:
            self.uri = '/api/v1/users?order={0}'.format(order)
        if offset is not None:
            self.uri = self.uri + '&offset={0}'.format(str(offset))            
        self.server = server + self.uri
        headers = {'Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)
        return results.content

    def search(self, server, token, limit=None, order='asc', keyword=None, offset=None):
        """Get list of users based on search keyword
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
        
        Keyword Arguments:
            limit {string} -- Limit the number of data returned by the server (default: {50})
        
        Returns:
            string -- List of users in JSON format.
        """
        if keyword is None:
            keyword = ""
        
        if limit is not None:
            self.uri = '/api/v1/users?limit={0}&order={1}'.format(str(limit), order)
        else:
            self.uri = '/api/v1/users?order={0}'.format(order)
        if offset is not None:
            self.uri = self.uri + '&offset={0}'.format(str(offset))            
        self.server = server + self.uri  + '&search={0}'.format(keyword)
        headers = {'Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)
        return results.content
        
    def create(self, server, token, payload):
        """Create new user data.
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            payload {string} -- input parameters
        
        Returns:
            string -- server response in JSON format
        """
        self.uri = '/api/v1/users'
        self.server = server + self.uri
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(token)}
        results = requests.post(self.server, headers=headers, data=payload)
        return json.dumps(results.json(),indent=4, separators=(',', ':'))

    def getID(self, server, token, user_name):
        """[summary]
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            user_name {[type]} -- [description]
        
        Returns:
            [type] -- [description]
        """
        self.uri = '/api/v1/users?search={0}'.format(user_name)
        self.server = server + self.uri 
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)
        jsonData = json.loads(results.content)
        if len(jsonData['rows']) < 2 and jsonData['rows'][0]['id'] is not None:
            UserID = jsonData['rows'][0]['id']
        return UserID

    def updateUser(self, server, token, UserID, payload):
        """[summary]
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            UserID {[type]} -- [description]
            payload {[type]} -- [description]
        
        Returns:
            [type] -- [description]
        """
        self.uri = '/api/v1/users/{0}'.format(UserID)
        self.server = server + self.uri
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(token)}
        results = requests.patch(self.server, headers=headers, data=payload)
        jsonData = json.loads(results.content)
        return jsonData['status']

    def delete(self, server, token, UserID):
        """[summary]
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            UserID {[type]} -- [description]
        
        Returns:
            [type] -- [description]
        """
        self.uri = '/api/v1/users/{0}'.format(UserID)
        self.server = server + self.uri 
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(token)}
        results = requests.delete(self.server, headers=headers)
        jsonData = json.loads(results.content)
        return jsonData['status']

    def getDetailsByID(self, server, token, userID):
        """Get detailed information of user by ID
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            userID {string} -- ID of the user
        
        Returns:
            string -- Detailed information of user by ID
        """
        self.uri = '/api/v1/users/{0}'.format(userID)
        self.server = server + self.uri
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)                
        return results.content

    def getCheckedOutAssets(self, server, token, UserID):
        """Get list of assets checked out to the user
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            componentsID {string} -- ID of the user
        
        Returns:
            string -- list of assets in JSON format
        """
        self.uri = '/api/v1/users/{0}/assets'.format(UserID)
        self.server = server + self.uri
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)
        return results.content
    

    def getCheckedOutAccessories(self, server, token, UserID):
        """Get list of accessories checked out to the user
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            componentsID {string} -- ID of the user
        
        Returns:
            string -- list of accessories in JSON format
        """
        self.uri = '/api/v1/users/{0}/accessories'.format(UserID)
        self.server = server + self.uri
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)
        return results.content