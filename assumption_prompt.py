prompt = f'''
Your client wants to file law suit against {{ $json.body.client_details.respondent_name }}
Below are the details provided:

- client's request: {{  $json.body.client_details.client_request }}
- client's story: {{ $json.body.client_details.client_story }}
- client's prayer: {{ $json.body.client_details.client_prayer }}

Additional context:
- Questions: {{ $json.body.qna.questions }}
- Answers: {{ $json.body.qna.answers }}

List any assumptions you are making due to missing or unclear information. 
Put all the assumptions (e.g. about a date, sum, or fact) in a bullet point format.


Output should only consist of assumptions nothing else.
example
```
The respondent is your real brother. 
Your father died without writing any will.
You already have given them legal notice.
```
'''

system_prompt = '''
You are an experienced litigator preparing to interview a new client_info to clarify the facts and legal issues of their case.
'''