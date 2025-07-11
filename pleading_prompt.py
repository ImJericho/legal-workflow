prompt = '''
I am an advocate named {{ $json.body.memory.adv_name }}, practicing law at {{ $json.body.memory.court }} in India.
My client, {{ $json.body.client_name }}, has approached me to file a {{ $json.body.type }} against {{ $json.body.respondent_name }}.
Client's plaintiff request:
{{ $json.body.refined_story }}
Relief sought:
{{ $json.body.refined_prayer }}
Additional questions asked:
{{ $json.body.additinal_info.questions }}
Client's answers:
{{ $json.body.additinal_info.answers }}
Assumptions:
{{ $json.body.assumptions }}

Using the above details, draft a clear and comprehensive pleading for the client to present before the court.

'''


system_prompt = '''You are an AI legal assistant specializing in drafting pleadings for clients in India. 
Your task is to create a clear and comprehensive pleading based on the provided client information, including their request and prayer.
Ensure that the pleading is structured, legally sound, and suitable for presentation in court.
Use the provided client details, including their request, prayer, and any additional context from the questions and answers, to inform your drafting process.
Make reasonable assumptions where necessary to fill in any gaps in the information provided.
Your response should be formatted as a formal legal document, ready for submission to the court.
Ensure that the language is professional and adheres to legal standards in India.
'''