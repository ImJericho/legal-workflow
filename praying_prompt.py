prompt = '''
Your client_info,{{ $('Webhook').item.json.body.client_info.client_name }} wants to file law suit against {{ $('Webhook').item.json.body.client_info.respondent_name }}.
Below are the details provided:

- client_info's request: {{ $('Webhook').item.json.body.client_info.request }}
- client_info's story: {{ $('Webhook').item.json.body.client_info.story }}

Additional context:
- Questions: {{ $('Webhook').item.json.body.additinal_info.questions }}
- Answers: {{ $('Webhook').item.json.body.additinal_info.answers }}

Assumptions: {{ $json.text }}

Based on the client’s objectives and any additional potential remedies, draft a detailed prayer for relief. Clearly specify the exact remedies sought (e.g., monetary compensation, injunction, costs), referencing relevant legal provisions or sections (e.g., ‘under Section X of Act Y’). Ensure the relief is stated specifically, as required by legal rules.

'''


system_prompt = '''You are an experienced advocate drafting the relief section of a plaint.

Your task is to create a clear and comprehensive prayer based on the provided client information, including their story and prayer sought.
Ensure that the prayer is structured, legally sound, and suitable for presentation in court.
''' 