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
    """Class to access consumables API    
    """    
    def __init__(self):
        pass

    def get(self, server, token, limit=None, order='asc', offset=None):
        """Get list of consumables
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            
        
        Keyword Arguments:
            limit {string} -- Limit the number of data returned by the server (default: {50})
            order {string} -- Display order of data (asc / desc default:{asc})
        
        Returns:
            [string] -- List of consumables from the server, in JSON formatted
        """
        if limit is not None:
            self.uri = '/api/v1/consumables?limit={0}&order={1}'.format(str(limit),order)
        else:
            self.uri = '/api/v1/consumables?order={0}'.format(order)
        if offset is not None:
            self.uri = self.uri + '&offset={0}'.format(str(offset))            
        self.server = server + self.uri 
        headers = {'Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)
        return results.content


    def getConsumablesByOrder(self, server, token, orderNumber, limit=None, order='asc', offset=None):
        """Get list of consumables
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            orderNumber {string} -- Order Number to be used as filter
        
        Keyword Arguments:
            limit {string} -- Limit the number of data returned by the server (default: {50})
            order {string} -- Display order of data (asc / desc default:{asc})
        
        Returns:
            [string] -- List of consumables from the server, in JSON formatted
        """
        if limit is not None:
            self.uri = '/api/v1/consumables?limit={0}&order={1}'.format(str(limit), order)
        else:
            self.uri = '/api/v1/consumables?order={0}'.format(order)
        if offset is not None:
            self.uri = self.uri + '&offset={0}'.format(str(offset))            
        self.server = server + self.uri 
        headers = {'Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)
        return results.content

    def getConsumablesByCategory(self, server, token, categoryID, limit=None, order='asc', offset=None):
        """Get list of consumables
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            categoryID {string} -- Category ID to be used as filter
        
        Keyword Arguments:
            limit {string} -- Limit the number of data returned by the server (default: {50})
            order {string} -- Display order of data (asc / desc default:{asc})
        
        Returns:
            [string] -- List of consumables from the server, in JSON formatted
        """
        if limit is not None:
            self.uri = '/api/v1/consumables?limit={0}&order={1}'.format(str(limit), order)
        else:
            self.uri = '/api/v1/consumables?order={0}'.format(order)
        if offset is not None:
            self.uri = self.uri + '&offset={0}'.format(str(offset))            
        self.server = server + self.uri +'&category_id={0}'.format(categoryID)
        headers = {'Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)
        return results.content

    def getConsumablesByCompany(self, server, token, companyID, limit=None, order='asc', offset=None):
        """Get list of consumables
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            companyID {string} -- Company ID to be used as filter
            
        
        Keyword Arguments:
            limit {string} -- Limit the number of data returned by the server (default: {50})
            order {string} -- Display order of data (asc / desc default:{asc})
        
        Returns:
            [string] -- List of consumables from the server, in JSON formatted
        """
        if limit is not None:
            self.uri = '/api/v1/consumables?limit={0}&order={1}'.format(str(limit), order)
        else:
            self.uri = '/api/v1/consumables?order={0}'.format(order)
        if offset is not None:
            self.uri = self.uri + '&offset={0}'.format(str(offset))            
        self.server = server + self.uri + '&company_id={0}'.format(companyID)
        headers = {'Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)
        return results.content

    def getConsumablesByManufacturer(self, server, token, manufacturerID, limit=None, order='asc', offset=None):
        """Get list of consumables filtered by manufacturer ID
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            manufacturerID {string} -- Manufacturer ID to be used as filter
        
        Keyword Arguments:
            limit {string} -- Limit the number of data returned by the server (default: {50})
            order {string} -- Display order of data (asc / desc default:{asc})
        
        Returns:
            [string] -- List of consumables from the server, in JSON formatted
        """
        if limit is not None:
            self.uri = '/api/v1/consumables?limit={0}&order={1}'.format(str(limit),order)
        else:
            self.uri = '/api/v1/consumables?order={0}'.format(order)
        if offset is not None:
            self.uri = self.uri + '&offset={0}'.format(str(offset))            
        self.server = server + self.uri +'&manufacturer_id={0}'.format(manufacturerID)
        headers = {'Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)
        return results.content

    def search(self, server, token, limit=None, order='asc', keyword=None, offset=None):
        """Get list of consumables based on search keyword
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
        
        Keyword Arguments:
            limit {string} -- Limit the number of data returned by the server (default: {50})
        
        Returns:
            string -- List of consumables in JSON format.
        """
        if keyword is None:
            keyword = ""
        
        if limit is not None:
            self.uri = '/api/v1/consumables?limit={0}&order={1}'.format(str(limit),order)
        else:
            self.uri = '/api/v1/consumables?order={0}'.format(order)
        if offset is not None:
            self.uri = self.uri + '&offset={0}'.format(str(offset))            
        self.server = server + self.uri  + '&search={0}'.format(keyword)
        headers = {'Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)
        return results.content

    def create(self, server, token, payload):
        """Create new consumable data.
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            payload {string} -- consumable name
        
        Returns:
            [type] -- [description]
        """
        self.uri = '/api/v1/consumables'
        self.server = server + self.uri
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(token)}
        results = requests.post(self.server, headers=headers, data=payload)
        return json.dumps(results.json(),indent=4, separators=(',', ':'))

    def getDetailsByID(self, server, token, consumableID):
        """Get detailed information of consumables by ID.
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            consumableID {string} -- Consumable ID to be checked
        
        Returns:
            string -- detailed information of consumable in JSON
        """
        self.uri = '/api/v1/consumables/{0}'.format(consumableID)
        self.server = server + self.uri
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)        
        return results.content
