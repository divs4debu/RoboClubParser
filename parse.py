import os
import xmltodict

project_path = os.getcwd()+"/ProjectDetails"
project_list = ["/AutoBuggy"]

project_details = open(project_path+project_list[0]+"/details.xml").read()
project_dict = xmltodict.parse(project_details)
print(project_dict['project']['thumb'])
