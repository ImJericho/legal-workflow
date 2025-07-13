import webbrowser
import tempfile


# Plaint Structure: 
# Organize the plaint with the following typical components: 
#     Court and Suit Details, 
#     Parties, 
#     Title of Suit, 
#     Averments ("Most Respectfully Showeth"),  
#     Cause of Action,
#     Jurisdiction, 
#     Valuation and Court Fee, 
#     Prayer, 
#     Signatures, and 
#     Verification.



plaint = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Plaint Format</title>
  <style>
    body { font-family: "Times New Roman", serif; margin: 1in; line-height: 1.5; }
    .center { text-align: center; }
    .parties-table { width: 100%; border-collapse: collapse; margin-top: 20px; margin-bottom: 20px; }
    .parties-table td { vertical-align: top; width: 45%; padding: 0 10px; }
    .parties-table .versus { width: 10%; text-align: center; font-weight: bold; font-size: 1.2em; }
    h1, h2 { text-transform: uppercase; margin: 0; }
    h1 { font-size: 1.2em; }
    h2 { font-size: 1em; margin-top: 1em; }
    ol { margin: 0 0 1em 1.5em; }
    .prayer ol { list-style-type: lower-alpha; }
    .prayer-block { display: flex; justify-content: space-between; margin-top: 2em; }
    .prayer-block .left { width: 45%; }
    .prayer-block .right { width: 45%; text-align: right; margin-right: 10em; }
    .prayer-block .right .center { text-align: right; margin-right: 5em;}
    .plaintiff_sign { text-align: right; margin-top: 1em; margin-right: 10em; }
    footer { margin-top: 2em; font-size: 0.9em; font-style: italic; }
  </style>
</head>
<body>

  <header class="center">
    <h1>In the Court of District Judge (District __________), Rohini Court, Delhi</h1>
    <p><strong>Suit No.</strong> ………….. of 20…</p>
    <p>(Suit under Order XXXVII of the Code of Civil Procedure, 1908)</p>
  </header>

  <parties>
    <table class="parties-table">
      <tr>
        <petitioner>
          <td>
            <strong>Plaintiff:</strong><br>
            <PLAINTIFF NAME HERE>
          </td>
        </petitioner>
        <td class="versus">VERSUS</td>
        <defendant>
          <td>
            <RESPONDENT NAME HERE>
          </td>
        </defendant>
      </tr>
    </table>
  </parties>

  <div class="center">
    <h2><TITLE HERE></h2>
  </div>

  <plaintContent>
    <h2>Most Respectfully Sheweth:</h2>
    <ol>
        <PLAINT HERE>
    </ol>
  </plaintContent>

  <prayer>
    <h2>Prayer:</h2>
    <div class="prayer">
      <ol>
        <PRAY HERE>
      </ol>
    </div>
    <div class="prayer-block">
      <div class="left">
        <p>Place: ________</p>
        <p>Date: ________</p>
      </div>
      <div class="right">
        <p>……………… Plaintiff</p>
        <div class="center"><p>Through</p></div>
        <p>Advocate</p>
      </div>
    </div>
  </prayer>

  <verification>
    <h2>Verification:</h2>
    <p>
<VERIFICATION HERE>  </p>
    
    <div class="plaintiff_sign">
      <p>Plaintiff Sign</p>
    </div>
  </verification>

  <footer>
    <b><u>Note:</u></b> The plaint must be supported by an affidavit. Ensure correct paragraph numbering and state jurisdictional details accurately.
  </footer>

</body>
</html>

'''


title = '''
  Suit for Recovery of Rs. 4,19,200/‑ under Order XXXVII CPC
'''

sheweth = '''
    <li>The Plaintiff is a Company constituted under the Companies Act having its registered office at B‑40, Safdarjung Enclave, New&nbsp;Delhi. Mr. P., Executive Director, is duly authorised to institute this suit.</li>
    <li>The Plaintiff carries on the business of construction, engineering and designing, and has earned a reputation as a builder of international repute.</li>
    <li>The Defendant is a Company incorporated under the Companies Act, having its registered office at Chandigarh.</li>
    <li>Just like this we will add from AI </li>
'''

sheweth2 = '''
<ol>\n<li>The Plaintiff, Ravindra Madhwan, is the rightful heir of the late Mr. Kamal Madhwan, who passed away on 15th November 2019, leaving behind the ancestral property situated at [Property Address] (hereinafter referred to as the "Property").</li>\n<li>The Defendant, Kishore Madhwan, is the Plaintiff's only sibling and has wrongfully taken possession of the Property following their father's demise.</li>\n<li>On 1st January 2020, the Plaintiff issued a legal notice to the Defendant, demanding that the Defendant vacate the Property and hand over possession to the Plaintiff, which the Defendant has failed to comply with.</li>\n</ol>
'''
pray = '''
    <li>Pass a decree for Rs.&nbsp;4,19,200/‑ with interest @18% p.a. from ……… (date) until filing of the suit.</li>
    <li>Award pendent­lite and future interest @18% p.a. on Rs.&nbsp;4,19,200/‑ from ……… (date) until payment.</li>
    <li>Award costs of the suit in favour of the Plaintiff.</li>
    <li>Pass any other order deemed fit and proper.</li>
    <li>Just like this we will add from AI </li>
'''

pray2 = '''
<ol>\n<li>A declaration that the Plaintiff is the rightful and legal owner of the Property.</li>\n<li>A declaration that the Defendant's occupation of the Property is illegal and wrongful.</li>\n<li>An order directing the Defendant to vacate and surrender peaceful possession of the Property to the Plaintiff forthwith.</li>\n<li>Compensation for damages suffered by the Plaintiff due to the wrongful occupation of the Property, including but not limited to loss of rent, utility expenses, and emotional distress.</li>\n<li>A perpetual injunction restraining the Defendant, his agents, servants, and/or anyone acting on his behalf, from interfering with the Plaintiff's peaceful possession and enjoyment of the Property.</li>\n<li>Any other relief deemed just and equitable by this Honourable Court.</li>\n</ol>'''

verification = '''
Verified at Delhi on this 1st day of January 20… that the contents of paras 1 to … are true to my knowledge and those of paras … to … are true on information and belief, and the last para is my prayer.
'''

plaintiff_name = '''
  M/s ABC&nbsp;Pvt.&nbsp;Ltd.,<br>
  A Company incorporated under the Companies Act,<br>
  Having its Registered Office at ………, New&nbsp;Delhi.<br>
  Through its Director Shri ……………………
'''

respondent_name = '''
  <strong>Defendant:</strong><br>
  M/s&nbsp;XYZ&nbsp;Ltd.,<br>
  A Company incorporated under the Companies Act,<br>
  Having its Registered Office at ………, Chandigarh.<br>
  Through its Director Shri ……………………
'''

plaint_final = plaint.replace(
    '<PLAINT HERE>',
    f'{sheweth2}'
).replace(
    '<PRAY HERE>',
    f'{pray2}'
).replace(
    '<TITLE HERE>',
    f'{title}'
).replace(
    '<VERIFICATION HERE>',
    f'{verification}'
).replace(
  '<PLAINTIFF NAME HERE>',
  f"{plaintiff_name}"
).replace(
    '<RESPONDENT NAME HERE>',
    f"{respondent_name}"
)

if __name__ == "__main__":
  with tempfile.NamedTemporaryFile('w', delete=False, suffix='.html') as f:
    f.write(plaint_final)
    temp_path = f.name

  webbrowser.open(f'file://{temp_path}')