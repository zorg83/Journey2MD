# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 12:04:35 2024

@author: zorg83
"""

import json
import datetime
import os
from markdownify import markdownify as md
import glob

#-----USER INPUT-------
jsonfiles = glob.glob("D:\YOUR_JOURNEY_EXPORT_FOLDER\*.json")
savefolder = r'YOUR_SAVE_FOLDER'
#---USER INPUT ENDS----


for loadfile in jsonfiles:
    
    # Opening JSON file
    with open(loadfile, encoding='utf-8') as json_file:
        data = json.load(json_file)
        
        dt = data.get("date_journal")/1000
        date = datetime.datetime.utcfromtimestamp(dt).strftime('%Y-%m-%d')
    
    filename = str(date) + ".md"
    if len(data.get("tags")) == 0:
        savefile = os.path.join(savefolder, "No_Tag", filename)
    elif  str(data.get("tags")[0]) == 'tag':
        savefile = os.path.join(savefolder, "tag", filename)
    else:
        savefile = os.path.join(savefolder, "Others", filename)
    

    with open(savefile, 'a+', encoding="utf-8") as f:
        f.write('---\n')
        f.write('created: ' + datetime.datetime.utcfromtimestamp(dt).strftime('%Y-%m-%d %H:%M:%S')+'\n')
        f.write('timezone: '+ str(data.get("timezone"))+'\n')
        f.write('tags: ')
        for i in range(len(data.get("tags"))):
            f.write(str(data.get("tags")[i]))
        f.write(' diary\n')
        f.write('lat: '+ str(data.get("lat"))+'\n')
        f.write('long: '+ str(data.get("lon"))+'\n')
        f.write('---\n \n')
        f.write(md(data.get("text")))
