
from bot_lens.Tracker import Tracker

#t = Tracker("asdfadsf", "localhost:3000")
t = Tracker("asdfadsf")
t.log_event("tim test", "tim", {'host': 'chatgpt-lugin.timtully1.repl.co', 'user-agent': 'Python/3.9 aiohttp/3.8.4', 'accept': '*/*', 'accept-encoding': 'gzip, deflate', 'accept-language': 'en-US,en;q=0.9', 'content-type': 'application/json', 'openai-conversation-id': '679569e4-b3e6-52d6-be2d-0328761f6322', 'openai-ephemeral-user-id': '6599caa6-01e3-51e7-9e3b-e968cac26ef6', 'openai-subdivision-1-iso-code': 'US-CA', 'traceparent': '00-00000000000000004912ceeb977bc42b-8633e24135d6067e-01', 'tracestate': 'dd=s:1;t.dm:-1', 'x-datadog-parent-id': '9670321594598557310', 'x-datadog-sampling-priority': '1', 'x-datadog-tags': '_dd.p.dm=-1', 'x-datadog-trace-id': '5265498425603638315', 'x-forwarded-for': '23.102.140.113', 'x-forwarded-proto': 'https', 'x-replit-user-bio': '', 'x-replit-user-id': '', 'x-replit-user-name': '', 'x-replit-user-profile-image': '', 'x-replit-user-roles': '', 'x-replit-user-teams': '', 'x-replit-user-url': ''})



"""
		-  `event_time: timestamp`
		- `developer_id: str`
		- `user_id: str`
		- `event_name: str`
		- `ip_address: str`
		- `unique_conversation_id: str`
		- `ephemeral_user_id: str`
		- `plugin_hostname: str`
		- `os_version: str`
		- `os: str`
		- `subdivision-1-iso-code: str`
		- `datadog-parent-id: str`
		- `chatgpt_ip: str`
		"""
  
  