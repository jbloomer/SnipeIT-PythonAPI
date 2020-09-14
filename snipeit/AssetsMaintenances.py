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


class AssetsMaintenances(object):
    def __init__(self):
        pass

    def get(self, server, token, limit=None, order='asc'):
        """Get list of assets
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            
        
        Keyword Arguments:
            limit {string} -- Limit the number of data returned by the server (default: {50})
            order {string} -- Display order of data (asc / desc default:{asc})
        
        Returns:
            [string] -- List of assets from the server, in JSON formatted
        """
        if limit is not None:
            self.uri = '/api/v1/hardware?limit={0}&order={1}'.format(str(limit), order)
        else:
            self.uri = '/api/v1/hardware?order={0}'.format(order)
        self.server = server + self.uri 
        headers = {'Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)
        return results.content
        #return json.dumps(results.json(),indent=4, separators=(',', ':'))

    def search(self, server, token, limit=None, order='asc', keyword=None):
        """Get list of assets based on search keyword
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
        
        Keyword Arguments:
            limit {string} -- Limit the number of data returned by the server (default: {50})
            order {string} -- Display order of data (asc / desc default:{asc})
        
        Returns:
            string -- List of assets in JSON format.
        """
        if keyword is None:
            keyword = ""
        
        if limit is not None:
            self.uri = '/api/v1/hardware?limit={0}&order={1}'.format(str(limit), order)
        else:
            self.uri = '/api/v1/hardware?order={0}'.format(order)
        self.server = server + self.uri  + '&search={0}'.format(keyword)
        headers = {'Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)
        return results.content
    
    def getAssetsByModel(self, server, token, modelID, limit=None, order='asc'):
        """Get list of assets
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            modelID {string} -- Model ID to be limited to            
        
        Keyword Arguments:
            limit {string} -- Limit the number of data returned by the server (default: {50})
            order {string} -- Display order of data (asc / desc default:{asc})
        
        Returns:
            [string] -- List of assets from the server, in JSON formatted
        """
        if limit is not None:
            self.uri = '/api/v1/hardware?limit={0}&order={1}'.format(str(limit), order)
        else:
            self.uri = '/api/v1/hardware?order={0}'.format(order)
        self.server = server + self.uri 
        headers = {'Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)
        return results.content

    def getAssetsByCategory(self, server, token, categoryID, limit=None, order='asc'):
        """Get list of assets
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            categoryID {string} -- Category ID to be limited to            
        
        Keyword Arguments:
            limit {string} -- Limit the number of data returned by the server (default: {50})
            order {string} -- Display order of data (asc / desc default:{asc})
        
        Returns:
            [string] -- List of assets from the server, in JSON formatted
        """
        if limit is not None:
            self.uri = '/api/v1/hardware?limit={0}&order={1}'.format(str(limit), order)
        else:
            self.uri = '/api/v1/hardware?order={0}'.format(order)
        self.server = server + self.uri + '&category_id={0}'.format(categoryID)
        headers = {'Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)
        return results.content

    def getAssetsByManufacturer(self, server, token, manufacturerID, limit=None, order='asc'):
        """Get list of assets
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            manufacturerID {string} -- Manufacturer ID to be limited to            
        
        Keyword Arguments:
            limit {string} -- Limit the number of data returned by the server (default: {50})
            order {string} -- Display order of data (asc / desc default:{asc})
        
        Returns:
            [string] -- List of assets from the server, in JSON formatted
        """
        if limit is not None:
            self.uri = '/api/v1/hardware?limit={0}&order={1}'.format(str(limit), order)
        else:
            self.uri = '/api/v1/hardware?order={0}'.format(order)
        self.server = server + self.uri + '&manufacturer_id={0}'.format(manufacturerID)
        headers = {'Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)
        return results.content

    def getAssetsByCompany(self, server, token, companyID, limit=None, order='asc'):
        """Get list of assets
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API            
            companyID {string} -- CompanyID to be limited to
        
        Keyword Arguments:
            limit {string} -- Limit the number of data returned by the server (default: {50})
            order {string} -- Display order of data (asc / desc default:{asc})
        
        Returns:
            [string] -- List of assets from the server, in JSON formatted
        """
        if limit is not None:
            self.uri = '/api/v1/hardware?limit={0}&order={1}'.format(str(limit), order)
        else:
            self.uri = '/api/v1/hardware?order={0}'.format(order)
        self.server = server + self.uri + '&company_id={0}'.format(companyID)
        headers = {'Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)
        return results.content        

    def getAssetsByLocation(self, server, token, locationID, limit=None, order='asc'):
        """Get list of assets
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API            
            locationID {string} -- Location ID to be limited to
        
        Keyword Arguments:
            limit {string} -- Limit the number of data returned by the server (default: {50})
            order {string} -- Display order of data (asc / desc default:{asc})
        
        Returns:
            [string] -- List of assets from the server, in JSON formatted
        """
        if limit is not None:
            self.uri = '/api/v1/hardware?limit={0}&order={1}'.format(str(limit), order)
        else:
            self.uri = '/api/v1/hardware?order={0}'.format(order)
        self.server = server + self.uri + '&location_id={0}'.format(locationID)
        headers = {'Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)
        return results.content

    def getAssetsByStatus(self, server, token, status, limit=None, order='asc'):
        """Get list of assets
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API            
            status {string} -- Status types (RTD, Deployed, Undeployable, Deleted, Archived, Requestable)
        
        Keyword Arguments:
            limit {string} -- Limit the number of data returned by the server (default: {50})
            order {string} -- Display order of data (asc / desc default:{asc})
        
        Returns:
            [string] -- List of assets from the server, in JSON formatted
        """
        if limit is not None:
            self.uri = '/api/v1/hardware?limit={0}&order={1}'.format(str(limit), order)
        else:
            self.uri = '/api/v1/hardware?order={0}'.format(order)
        self.server = server + self.uri + '&status={0}'.format(status)
        headers = {'Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)
        return results.content  

    def getAssetsByStatusLabel(self, server, token, statusLabelID, limit=None, order='asc'):
        """Get list of assets
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API            
            statusLabelID {string} -- Status label ID
        
        Keyword Arguments:
            limit {string} -- Limit the number of data returned by the server (default: {50})
            order {string} -- Display order of data (asc / desc default:{asc})
        
        Returns:
            [string] -- List of assets from the server, in JSON formatted
        """
        if limit is not None:
            self.uri = '/api/v1/hardware?limit={0}&order={1}'.format(str(limit), order)
        else:
            self.uri = '/api/v1/hardware?order={0}'.format(order)
        self.server = server + self.uri + '&status_id={0}'.format(statusLabelID)
        headers = {'Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)
        return results.content

    def getDetailsByID(self, server, token, AssetID):
        """Get asset details by ID
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            AssetID {string} -- Asset ID             
        
        Returns:
            [string] -- Asset details from the server, in JSON formatted
        """
        self.uri = '/api/v1/hardware/{0}'.format(str(AssetID))
        self.server = server + self.uri
        headers = {'Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)
        return results.content

    def getDetailsByTag(self, server, token, AssetTAG):
        """Get asset details by ID
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            AssetTAG {string} -- Asset TAG             
        
        Returns:
            [string] -- Asset details from the server, in JSON formatted
        """
        self.uri = '/api/v1/hardware/bytag/{0}'.format(str(AssetTAG))
        self.server = server + self.uri
        headers = {'Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)
        return results.content


    def getDetailsBySerial(self, server, token, AssetSerial):
        """Get asset details by Serial Number
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            AssetSerial {string} -- Asset Serial Number             
        
        Returns:
            [string] -- List of assets from the server, in JSON formatted
        """
        self.uri = '/api/v1/hardware/byserial/{0}'.format(str(AssetSerial))
        self.server = server + self.uri
        headers = {'Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)
        return results.content

    def create(self, server, token, payload):
        """Create new asset data
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            payload {string} -- Asset data
        
        Returns:
            [string] -- Server response in JSON formatted
        """
        self.uri = '/api/v1/hardware'
        self.server = server + self.uri
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(token)}
        results = requests.post(self.server, headers=headers, data=payload)
        return json.dumps(results.json(),indent=4, separators=(',', ':'))

    def getID(self, server, token, asset_name):
        """search asset ID by its name
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            asset_name {string} -- Asset name
        
        Returns:
            [string] -- Server response in JSON formatted
        """                
        self.uri = '/api/v1/hardware?search={0}'.format(asset_name)
        self.server = server + self.uri
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)
        jsonData = json.loads((results.content).decode('utf-8').replace("'",'"'))
        #print(jsonData)
        if len(jsonData['rows']) < 2 and jsonData['rows'][0]['id'] is not None:
            AssetID = jsonData['rows'][0]['id']
        return AssetID
    
    def delete(self, server, token, DeviceID):
        """Delete asset data
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            DeviceID {string} -- Asset ID to be deleted
        
        Returns:
            [string] -- Server response in JSON formatted
        """        
        self.uri = '/api/v1/hardware/{0}'.format(DeviceID)
        self.server = server + self.uri
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(token)}
        results = requests.delete(self.server, headers=headers)
        jsonData = json.loads(results.content)
        return jsonData['status']

    def updateDevice(self, server, token, DeviceID, payload):
        """Update asset data
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            DeviceID {string} -- Asset ID
            payload {string} -- Asset data
        
        Returns:
            [string] -- Server response in JSON formatted
        """
        self.uri = '/api/v1/hardware/{0}'.format(DeviceID)
        self.server = server + self.uri
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(token)}
        results = requests.patch(self.server, headers=headers, data=payload)
        jsonData = json.loads(results.content)
        return jsonData['status']
