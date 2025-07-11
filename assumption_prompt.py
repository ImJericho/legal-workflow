prompt = f'''
Your client_info,{{ $('Webhook').item.json.body.client_info.client_name }} wants to file law suit against {{ $('Webhook').item.json.body.client_info.respondent_name }}.
Below are the details provided:

- client_info's request: {{ $('Webhook').item.json.body.client_info.request }}
- client_info's story: {{ $('Webhook').item.json.body.client_info.story }}

Additional context:
- Questions: {{ $('Webhook').item.json.body.additinal_info.questions }}
- Answers: {{ $('Webhook').item.json.body.additinal_info.answers }}

Assumptions: {{ $json.text }}


Rewrite the facts in chronological order as a concise narrative suitable for a plaint. Include all material facts previously gathered, phrased formally and clearly. Do not speculate or add new facts. Use neutral, objective language.”
(In law, facts should be stated sequentially to establish the case's timeline and context. This helps in understanding the sequence of events leading to the legal action.)
'''

system_prompt = '''
You are an experienced civil litigator preparing to interview a new client_info to clarify the facts and legal issues of their case.
'''