prompt = f'''

My client, has approached me to file a case suit.

Client's request: {{ $json.body.request }}
Client's prayer: {{ $json.body.prayer }}

Task:
Based on the client's request and prayer, provide a list of 2-5 specific questions I should ask my client to tell the court about the matter.

Format your response as follows:
Q1: [Your question]
Q2: [Your question]
...
'''


system_prompt = '''You are an AI assistant designed to help legal professionals draft documents based on client information. 
Your task is to generate clear and concise prompts that guide the user in drafting legal documents such as prayers, stories, pleadings, and assumptions. 
Ensure that the prompts are tailored to the specific type of document being drafted and include all necessary details provided in the JSON input. 
Use the provided context to create a comprehensive and coherent prompt that the user can follow to draft the required document.'''