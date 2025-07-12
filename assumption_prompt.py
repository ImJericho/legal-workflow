prompt = f'''
Your client_info, {{ $json.body.client_info.client_name }} wants to file law suit against {{ $json.body.client_info.respondent_name}}.
Below are the details provided:

- client_info's request: {{ $json.body.client_info.request }}
- client_info's story: {{ $json.body.client_info.story }}
- client_info's prayer: {{ $json.body.client_info.prayer }}

Additional context:
- Questions: {{ $json.body.aditional_info.questions }}
- Answers: {{ $json.body.aditional_info.answers }}

List any assumptions you are making due to missing or unclear information. 
Put all the assumptions (e.g. about a date, sum, or fact) in a bullet point format.
'''

system_prompt = '''
You are an experienced civil litigator preparing to interview a new client_info to clarify the facts and legal issues of their case.
'''