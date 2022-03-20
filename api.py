# grab info from notion and GitHub
import json

class api:
  
  def __init__(self, **kwargs):
    if kwargs.get('notion_api_secret') and kwargs.get('notion_db'):
      self.notion_secret = kwargs.get('notion_api_secret')
      self.notion_db = kwargs.get('notion_db')


  def grab_info_from_notion():
    return ''

  def grab_stats_from_github():
    return ''

