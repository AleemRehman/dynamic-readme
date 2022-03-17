
class File:
  def __init__(self):
    return
  
  def template_handler(self, template_path):
    # check if the template exists
    #   - duplicate the contents of the file if it does exist
    #   - return a success flag and the contents of the template
    if os.path.exists(template_path):
      with open(template_path,"r") as template_file:
        template = template_file.read()
        if '[[INSERT]]' in template:
          print("there's a dynamic placeholder")
        else:
          print("there's no dynamic placeholder in template")
    return

  def write_new_readme(self, new_data):
    # write the new readme with data from the builder
    return



  