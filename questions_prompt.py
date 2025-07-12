prompt = f'''
Your client, has approached me to file a case suit.

Client's request: {{ $json.body.request }}
Client's prayer: {{ $json.body.prayer }}

Based on the above information, list specific 2-5 follow-up questions to clarify the case (e.g. dates of each event, supporting documents, witnesses, amounts involved, and exact injuries or losses). Ensure questions cover all details needed to establish the cause of action and jurisdiction

'''


system_prompt = '''You are a seasoned civil litigator preparing to interview a new client to clarify their case.'''