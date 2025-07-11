prompt = '''
Your client_info,{{ $('Webhook').item.json.body.client_info.client_name }} wants to file law suit against {{ $('Webhook').item.json.body.client_info.respondent_name }}.
Below are the details provided:

- client_info's request: {{ $('Webhook').item.json.body.client_info.request }}
- client_info's story: {{ $('Webhook').item.json.body.client_info.story }}

Additional context:
- Questions: {{ $('Webhook').item.json.body.additinal_info.questions }}
- Answers: {{ $('Webhook').item.json.body.additinal_info.answers }}

Assumptions: {{ $json.text }}


Write all the facts in chronological order as a narrative suitable for a plaint. Use all the information ie: story, request, assumptions, question & answers.
'''


system_prompt = '''You are a skilled civil litigation draftsman. Organize facts clearly'''