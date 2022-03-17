# grab info from notion and GitHub
import json

class api:
  
  def __init__(self):
    self.notion_api_secret, self.notion_db = api.set_local_variables()
    return ''


  def set_local_variables():
    with open("example_variables.json", "r") as variables:
      values = variables.read()
      json = json.loads(values)
      return json['NOTION_API_SECRET'], json['NOTION_DB']


  def grab_info_from_notion():
    return ''

  def grab_stats_from_github():
    return ''

