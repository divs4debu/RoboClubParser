import xmltodict
from os import listdir
import json

project_path = "/home/divy/Work/ProjectWork/Roboclub/ProjectDetails" 
project_list  = list()
[project_list.append("/{}".format(dirnames)) for dirnames in listdir(project_path)]
#print(project_list)
for project in project_list:
    try:
        project_details = open(project_path+project+"/details.xml").read()
    except FileNotFoundError:
        pass
    project_dict = xmltodict.parse(project_details)
    try:
        json_file = open("json.txt","a")
        json_file.write(json.dumps(project_dict,indent=5))
    except KeyError:
        pass
    
        
