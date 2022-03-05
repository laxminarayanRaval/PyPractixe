import smtplib
from email.message import EmailMessage

email = EmailMessage()

email['Subject'] = 'Testing SMTPLib'
email['From'] = 'your@gmail.com'
email['To'] = 'someone.elses@gmail.com'

email.set_content("""Dear Sir/Madam,

This is Testing Email...
don't mind it.

-- Tester""")

smtp_connector = smtplib.SMTP(host='smtp.gmail.com', port=587)
smtp_connector.starttls()
smtp_connector.login('your@gmail.com', 'your_secret_password')

smtp_connector.send_message(email)

smtp_connector.quit()
