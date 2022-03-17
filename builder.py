import json
import re
import os

class Builder:
  # build the dynamic content
  def set_local_variables():
    with open("example_variables.json", "r") as variables:
      values = variables.read()
      json = json.loads(values)
      return json['NOTION_API_SECRET'], json['NOTION_DB']

  def load_template():
    if os.path.exists("template-readme.md"):
      with open("template-readme.md","r") as template_file:
        template = template_file.read()
        if '[[INSERT]]' in template:
          print("there's a dynamic placeholder")
        else:
          print("there's no dynamic placeholder in template")

    print('load the template and ensure it has a dynamic tag')
  
  def create_table(self, data):
    #convert dict into a markdown table
    if type(data) == dict:
      # do stuff
      print('were in')
    else:
      print('fail')
      # fail

  def create_link(self, url):
    # create a md link from a url
    return('')