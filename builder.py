import json
import re
import os

class Builder:
  # build the dynamic content

  def __init__(self, **kwargs):
    if kwargs.get('notion_api_secret') and kwargs.get('notion_db'):
      self.notion_secret = kwargs.get('notion_api_secret')
      self.notion_db = kwargs.get('notion_db')

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