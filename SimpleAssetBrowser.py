#!/usr/bin/env python
'''
this script uses pandas. please install beforehand
'''

from snipeit import Assets, Categories, DataUtil
import html
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg
import pandas as pd

server='<your snipe-it server>'
token='<your token value'

A = Assets()
C = Categories()

def asset_browser():    
    categories = C.get(server, token)
    cat_jsondata = DataUtil.getjson(categories)        
    catdf = pd.DataFrame(cat_jsondata["rows"], columns=['name'])
    catdflist = catdf.values.tolist()
    catdflist = [item for sublist in catdflist for item in sublist]
    
    for cat in catdflist:
        if isinstance(cat,dict):
            cat = str(cat)
        catdflist[catdflist.index(cat)] = html.unescape(cat)
    
    next_offset=0    
    firstdata = display_data(next_offset,"3")

    layout = [[sg.Text("Categories "),sg.InputCombo(catdflist, key='categories', enable_events=True)],
              [sg.Table(values=firstdata[0], 
                        headings=firstdata[1], 
                        display_row_numbers=False,
                        auto_size_columns=True, 
                        key='mytable',
                        num_rows=min(25,len(firstdata[0])))],
              [sg.Text(firstdata[2], key='total')],
              [sg.Button('Next offset')]]

    window = sg.Window('Table', grab_anywhere=False)

    while True:
        event, values = window.Layout(layout).Read()
        
        if event is None:
            break
        else:
            if (event == 'Next offset'):
                next_offset +=100
                selectedID = getCategoryID(values['categories'])
                next_data = display_data(next_offset, selectedID)
                
                # print(next_data)
                window.Element('mytable').Update(next_data[0])
                window.Element('total').Update(str(next_data[2]) + "/" + str(firstdata[2]))
            elif(event == 'categories'):
                selectedID = getCategoryID(values['categories'])
                sortedAssets = getAssetbyID(selectedID)
                
                window.Element('mytable').Update(sortedAssets[0])
                window.Element('total').Update(sortedAssets[2])

            else:                
                pass

    sys.exit(69)

def getCategoryID(category_name):
    # print("category name = {0}".format(category_name))
    result = C.search(server,token,keyword=category_name)
    resulted = DataUtil.getjson(result)       
    df = pd.DataFrame(resulted["rows"], columns=['id'])
    resulted = [item for sublist in df.values for item in sublist]    
    return(resulted[0])
    

def getAssetbyID(id):
    result = A.getAssetsByCategory(server, token, id)
    populated_data=populateData(result)
    return (populated_data)

def display_data(next_offset, categoryID):
    r = A.getAssetsByCategory(server, token, limit=100, offset = next_offset, categoryID=categoryID)
    populated_data=populateData(r)
    return (populated_data)

def populateData(resp_data):
    data = []
    header_list = []
    try:
        jsondata = DataUtil.getjson(resp_data)        
        df = pd.DataFrame(jsondata["rows"], columns=['id','asset_tag','model','assigned_to','location','last_checkout'])          
        try:
            if (df['model'].dropna().empty is not True):
                df = pd.concat([df.drop(['model'],axis=1), df['model'].apply(pd.Series)['name']],axis=1)        
                df.rename(columns={'name':'device name'}, inplace=True)
            
            if (df['assigned_to'].dropna().empty is not True):
                df = pd.concat([df.drop(['assigned_to'],axis=1), df['assigned_to'].apply(pd.Series)['name']],axis=1)                
                df.rename(columns={'name':'assignee'}, inplace=True)
            
            if (df['location'].dropna().empty is not True):
                df = pd.concat([df.drop(['location'],axis=1), df['location'].apply(pd.Series)['name']],axis=1)        
                df.rename(columns={'name':'location'}, inplace=True)

            if (df['last_checkout'].dropna().empty is not True):
                df = pd.concat([df.drop(['last_checkout'],axis=1), df['last_checkout'].apply(pd.Series)['formatted']],axis=1)        
                df.rename(columns={'formatted':'checkout date'}, inplace=True)                
            # print(df)
        
            df = df.where((pd.notnull(df)), None)
            
            total = jsondata["total"]
            for header in df.columns:
                header_list.append(header)
            data = df.values.tolist()               # read everything else into a list of rows
            # header_data = df.head()            
            return(data, header_list,total)
        except:
            df = None
    except:
        pass
    
    
        
asset_browser()