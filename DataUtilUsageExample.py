#!/usr/bin/env python

from snipeit import Assets, Users, Categories
from snipeit import DataUtil
import json
import ast
import pandas as pd

server='<your snipe-it server>'
token='<your token>'


A = Assets()
r = A.get(server, token) # Using default limit of 50 for results
jsondata = DataUtil.getjson(r)
print (DataUtil.prettyprint(r))


