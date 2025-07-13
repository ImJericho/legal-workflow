prompt = '''
Your client,{{ $json.client_details.client_name }} wants to file law suit against {{ $json.client_details.respondent_name }}.
Below are the details provided:

- client_info's request: {{ $json.client_details.client_request }}
- client_info's story: {{ $json.client_details.client_story }}

Additional context:
- Questions: {{ $json.qna.questions }}
- Answers: {{  $json.qna.answers }}

Assumptions: {{ $json.assumptions }}

Analyse all the information and Write all the facts in chronological order as a narrative suitable for a plaint. 
'''


system_prompt = '''You are a skilled litigation draftsman. Organize facts clearly'''