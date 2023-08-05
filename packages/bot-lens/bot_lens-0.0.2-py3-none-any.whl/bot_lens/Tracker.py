import random
import json
import time
import requests
from fastapi import FastAPI, Header

class Tracker:
	DEFAULT_HOST = '34.221.241.220'
    
	def __init__(self, token, host=DEFAULT_HOST):  
		self.token = token
		self.host = host
		print(f"token is {self.token} host is {host}")
	
	
	"""
	Headers({'host': 'chatgpt-lugin.timtully1.repl.co', 
 'user-agent': 'Python/3.9 aiohttp/3.8.4', 'accept': '*/*', 
 'accept-encoding': 'gzip, deflate', 'accept-language': 
 'en-US,en;q=0.9', 'content-type': 'application/json', 
 'openai-conversation-id': '679569e4-b3e6-52d6-be2d-0328761f6322', 
 'openai-ephemeral-user-id': '6599caa6-01e3-51e7-9e3b-e968cac26ef6', 
 'openai-subdivision-1-iso-code': 'US-CA', 
 'traceparent': '00-00000000000000004912ceeb977bc42b-8633e24135d6067e-01', 
 'tracestate': 'dd=s:1;t.dm:-1', 
 'x-datadog-parent-id': '9670321594598557310', 
 'x-datadog-sampling-priority': '1', 
 'x-datadog-tags': '_dd.p.dm=-1', 
 'x-datadog-trace-id': '5265498425603638315', 
 'x-forwarded-for': '23.102.140.113', 
 'x-forwarded-proto': 'https'})
 	"""
	def log_event(self, event_name="", username="", http_header:Header=None):
		print(f"will log {event_name}")
		ts = int(time.time()) 
		openai_conv_id = http_header['openai-conversation-id']
		openai_ephemeral_id = http_header['openai-ephemeral-user-id']
		ip = http_header['x-forwarded-for']
		ddog_parent = http_header['x-datadog-parent-id']
		plugin_hostname = http_header['host']
		iso_code = http_header['openai-subdivision-1-iso-code']
		payload = [
				{
					"event_time":ts,
					"developer_id":self.token,
					"user_id":openai_conv_id,
					"user_name":username,
     				"event_name":event_name,
					"ip_address":ip,
					"unique_conversation_id":openai_conv_id,
     				"ephemeral_user_id":openai_ephemeral_id,
         			"plugin_hostname":plugin_hostname,
					"os_version":1.2,
					"os":"mac",
					"subdivision-1-iso-code":iso_code,
     				"datadog-parent-id":ddog_parent,
					"chatgpt_id":"1.2.3.4"
				}
		]
		
		print(f"payload is {payload}")
		uri = f"http://{self.host}/log_events"
		print(uri)
		r = requests.post(url = uri, json=payload)
		print(r)
		pass



	
		