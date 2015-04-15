"""
 Simple wrapper for the Hackpad API v1.0
 API Documentation: https://hackpad.com/Public-Hackpad-API-Draft-nGhsrCJFlP7
"""

import requests
import sys
import time

from requests_oauthlib import OAuth1Session
from urlparse import urljoin

class Hackpad(object):
  def __init__(self, sub_domain='', consumer_key='', consumer_secret=''):
    self.sub_domain = sub_domain
    self.consumer_key = consumer_key
    self.consumer_secret = consumer_secret
    return

  def create_blank_hackpad(self, asUser='', content_type='text/plain'):
    return self.create_hackpad('Hackpad Title', 'Auto-generated Hackpad contents.', 
                            asUser, content_type)

  def create_hackpad(self, title, content, asUser='', content_type='text/plain'):
    api_link = 'pad/create'
    params = {}
    if asUser != '':
      params['asUser'] = asUser
    return self.do_api_request(api_link, 'POST', params, '%s\n%s' % (title, content), content_type)

  def get_pad_content(self, padId, revision='', response_format='txt', asUser=''):
    api_link = 'pad/%s/content' % padId
    if revision != '':
      api_link += revision
    api_link += '.%s' % response_format
    params = {}
    if asUser != '':
      params['asUser'] = asUser
    return self.do_api_request(api_link, 'GET', params)

  def update_pad_content(self, padId, content='', asUser='', content_type='text/plain'):
    api_link = 'pad/%s/content' % padId
    params = {}
    if asUser != '':
      params['asUser'] = asUser
    return self.do_api_request(api_link, 'POST', params, content, content_type)

  def search_for_pads(self, q='', start=0, limit=10, asUser=''):
    api_link = 'search'
    params = {'q':q, 'start':start, 'limit':limit}
    if asUser != '':
      params['asUser'] = asUser
    return self.do_api_request(api_link, 'GET', params)

  def list_updated_pads(self, timestamp):
    api_link = 'edited-since%s' % timestamp
    params = {}
    return self.do_api_request(api_link, 'GET', params)

  def pad_revisions(self, padId, asUser=''):
    api_link = 'pad/%s/revisions' % padId
    params = {}
    if asUser != '':
      params['asUser'] = asUser
    return self.do_api_request(api_link, 'GET', params)

  def revert_pad(self, padId, revision, asUser=''):
    api_link = 'pad/%s/revert-to/%s' % (padId, revision)
    params = {}
    if asUser != '':
      params['asUser'] = asUser
    return self.do_api_request(api_link, 'POST', params)

  def revoke_access(self, padId, user, asUser=''):
    api_link = 'pad/%s/revoke-access/%s' % (padId, user)
    params = {}
    if asUser != '':
      params['asUser'] = asUser
    return self.do_api_request(api_link, 'POST', params)

  def pad_options(self, padId, asUser=''):
    api_link = 'pad/%s/options' % padId
    params = {}
    if asUser != '':
      params['asUser'] = asUser
    return self.do_api_request(api_link, 'GET', params)

  def set_pad_options(self, padId, settings={}, asUser=''):
    api_link = 'pad/%s/options' % padId
    params = {}
    if asUser != '':
      params['asUser'] = asUser
    for key in settings.keys():
      params[key] = settings[key]
    return self.do_api_request(api_link, 'POST', params)

  def user_settings(self, user, settings={}):
    api_link = 'user/%s/settings' % user
    params = {}
    for key in settings.keys():
      params[key] = settings[key]
    return self.do_api_request(api_link, 'POST', params)

  def user_deletion(self, user):
    api_link = 'user/%s/remove' % user
    return self.do_api_request(api_link, 'POST')

  def user_creation(self, name, email):
    api_link = 'user/create'
    params = {'email':email, 'name':name}
    return self.do_api_request(api_link, 'POST', params)

  def list_all(self):
    api_link = 'pads/all'
    return self.do_api_request(api_link, 'GET')

  def site_options(self):
    api_link = 'options'
    return self.do_api_request(api_link, 'GET')

  def do_api_request(self, path, method, post_data={}, body='', content_type='text/plain'):
    method = method.upper()
    hackpad = {}
    try:
      if self.sub_domain:
        path = urljoin('https://%s.hackpad.com/api/1.0/' % self.sub_domain, path)
      else:
        path = urljoin('https://hackpad.com/api/1.0/', path)

      params = {
        'client_key': self.consumer_key,
        'client_secret': self.consumer_secret
      }

      for key in post_data.keys():
        params[key] = post_data[key]
      
      hackpad_api = OAuth1Session(**params)

      if method == 'POST':

        r = hackpad_api.post(path, data=body)
        hackpad = r.json()
      else:
        r = hackpad_api.get(path)

        try:
            hackpad = r.json()
        except:
            hackpad = r.content
    except:
      print sys.exc_info()[0]

    return hackpad

