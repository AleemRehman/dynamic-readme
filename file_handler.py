import os
import pathlib
root = pathlib.Path(__file__).parent.resolve()

class File:
  def __init__(self):
    return
  
  def template_handler(self, template_name):
    # check if the template exists
    #   - duplicate the contents of the file if it does exist
    #   - return a success flag and the contents of the template
    path_name = root

    if type(template_name) == str:
      path_name = root + template_name

    if os.path.exists(path_name):
      with open(path_name,"r") as template_file:
        template = template_file.read()
        if '[[INSERT]]' in template:
          print("there's a dynamic placeholder")
        else:
          print("there's no dynamic placeholder in template")
    return

  def set_local_variables():
    with open("example_variables.json", "r") as variables:
      values = variables.read()
      json = json.loads(values)
      return json['NOTION_API_SECRET'], json['NOTION_DB']
      
  def write_new_readme(self, new_data):
    # write the new readme with data from the builder
    return



  