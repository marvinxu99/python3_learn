import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('letter.html').read_text())

email = EmailMessage()
email['from'] = 'Marvin Xu'
email['to'] = " email addess here"
email['subject'] = "this is a test email"

#email.set_content('I am a Python Master!')
email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('winnpysoft@gmail.com', 'password xxxxxxx')
    smtp.send_message(email)

    print('all good boss')
