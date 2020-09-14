import json

def prettyprint(resp_data):
    """format json response data into good indented format
    
    Arguments:
        resp_data {string} -- response data in JSON format - use getjson first
    """
    resp_data = resp_data.decode("utf-8").replace("'",'"')
    parsed = json.loads(resp_data)
    prettystring = json.dumps(parsed, indent=4, sort_keys=True)
    return prettystring

def getjson(resp_data):
    """Converts response data from binary to string json format
    
    Arguments:
        resp_data {string} -- response data returned by requests api
    """
    resp_data = resp_data.decode("utf-8").replace("'",'"')
    parsed = json.loads(resp_data)    
    return parsed

def gettotaldata(resp_data):
    """Gets the total data from response data
    
    Arguments:
        resp_data {string} -- response data in JSON format - use getjson first
    """
    # totaldata = getjson(resp_data)
    return resp_data["total"]