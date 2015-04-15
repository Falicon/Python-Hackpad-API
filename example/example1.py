import os
from hackpad_api.hackpad import Hackpad

hackpad = Hackpad(os.getenv('team') ,consumer_key = os.getenv('consumer_key'), consumer_secret = os.getenv('consumer_secret'))

print(hackpad.do_api_request('pads/all', 'GET'))

