prompt = f'''
Your client, has approached me to file a case suit.

Client's name: {{ $json.body.client_details.client_name }}
Client's request: {{ $json.body.client_details.client_request }}
Client's story: {{ $json.body.client_details.client_story }}
Client's prayer: {{ $json.body.client_details.client_prayer }}

Based on the above information, list specific 2-4 follow-up questions to clarify the case (e.g. dates of each event, supporting documents, witnesses, amounts involved, and exact injuries or losses). Ensure questions cover all details needed to establish the cause of action and jurisdiction.

Output should only consist of question nothing else.
example
```
What's your relationship with respondent? 
Where is the disputed land located?
How much money you are claiming?
```

I am {{ $json.body.client_details.client_name }}
I have a request: {{$json.body.client_details.client_request}}
Here's my story: {{$json.body.client_details.client_story}}.
prayer: {{ $json.body.client_details.client_prayer }}

'''


system_prompt = '''
You are a experienced litigation lawyer practicing in India preparing to interview a new client to clarify their case.
You are master in writing plaints and pleading.
A client has come up to you with some request, based on his information, list few questions (each in a single paragraph only) to clarify the case. Ensure questions cover all details needed to establish the cause of action and jurisdiction.
Output should only consist of list of questions nothing else.
'''
