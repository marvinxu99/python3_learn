import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

def send_email_report(sender_email, receiver_email, subject, body, smtp_server, smtp_port, login, password, attachment_path=None):
    # Create the email object
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Add the body of the email
    msg.attach(MIMEText(body, 'plain'))

    # Check if there's an attachment to send
    if attachment_path and os.path.exists(attachment_path):
        with open(attachment_path, 'rb') as attachment_file:
            attachment = MIMEApplication(attachment_file.read(), Name=os.path.basename(attachment_path))
        attachment['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment_path)}"'
        msg.attach(attachment)

    # Connect to the SMTP server and send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade to secure connection
            server.login(login, password)  # Login to the email server
            server.sendmail(sender_email, receiver_email, msg.as_string())  # Send the email
            print(f"Email sent successfully to {receiver_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    # Set up email details
    sender_email = "marvinxu99@gmail.com"
    receiver_email = "marvinxu99@hotmail.com"
    subject = "Daily Report"
    body = "This is your daily report from mxFHIR server. Please find the attached file."
    smtp_server = "smtp.gmail.com"  # Replace with your SMTP server
    smtp_port = 587  # Commonly used port for TLS
    login = "marvinxu99@gmail.com"
    password = "xxxxxxxxxxxxxxxx"  # 16-byte App password from google acount - Use environment variables or a secure method to store this

    # Optional attachment (set to None if you don't have one)
    attachment_path = "/path/to/your/report.pdf"  # Change this path to the report file

    # Send the email
    send_email_report(sender_email, receiver_email, subject, body, smtp_server, smtp_port, login, password, attachment_path)

