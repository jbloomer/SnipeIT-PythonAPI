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

class Company(object):
    """Class to access Companies API
    """
    def __init__(self):
        pass

    def get(self, server, token):
        """Gets company list
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
        
        Returns:
            string -- List of companies from the server, in JSON formatted
        """
        self.uri = '/api/v1/companies'
        self.server = server + self.uri
        headers = {'Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)
        return results.content

    def create(self, server, token, payload):
        """Create new company data.
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            payload {string} -- Company Name
        
        Returns:
            string -- Status data from the server, in JSON formatted
        """
        self.uri = '/api/v1/companies'
        self.server = server + self.uri
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(token)}
        results = requests.post(self.server, headers=headers, data=payload)
        return json.dumps(results.json(),indent=4, separators=(',', ':'))

    def getDetailsByID(self, server, token, companiesID):
        """Gets company details by ID
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            companiesID {[type]} -- [description]
        
        Returns:
            string -- Detailed information of company from the server, in JSON formatted
        """
        self.uri = '/api/v1/companies/{0}'.format(str(companiesID))
        self.server = server + self.uri 
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)        
        return results.content

    def delete(self, server, token, CompanyID):
        """Delete company information
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            CompanyID {[type]} -- [description]
        
        Returns:
            string -- Response message from the server, in JSON formatted
        """
        self.uri = '/api/v1/companies/{0}'.format(CompanyID)
        self.server = server + self.uri 
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(token)}
        results = requests.delete(self.server, headers=headers)
        jsonData = json.loads(results.content)
        return jsonData['status']

    def updateCompany(self, server, token, CompanyID, payload):
        """Updates company name.
        
        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            CompanyID {string} -- ID of company to be updated
            payload {string} -- Company name to be updated
        
        Returns:
            string -- Response message from the server, in JSON formatted
        """
        self.uri = '/api/v1/companies/{0}'.format(CompanyID)
        self.server = server + self.uri
        headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(token)}
        results = requests.patch(self.server, headers=headers, data=payload)
        jsonData = json.loads(results.content)
        return jsonData['status']
