import win32com.client           # pip install pywin32
from xhtml2pdf import pisa
import os
from datetime import datetime, timedelta


# Directory to save PDFs
# save_dir = "C:/SavedEmails/"
save_dir = "D:/dDev/Python/python3_learn/Email_playground/AutoSaveToPDF/SavedEmails"
os.makedirs(save_dir, exist_ok=True)


def save_email_as_pdf(email):
    subject = email.Subject.replace(":", "-").replace("\\", "").replace("/", "")
    file_path = os.path.join(save_dir, f"{subject}.pdf")

    # Extract the HTML body of the email
    html_body = email.HTMLBody
    # Fallback to plain text if HTML body is not available
    if not html_body:
        html_body = f"<pre>{email.Body}</pre>"  # Wrap plain text in <pre> to preserve formatting

    # Create the complete HTML content with the subject at the top
    pdf_content = f"""
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; }}
            .subject {{ font-size: 18px; font-weight: bold; margin-bottom: 20px; }}
        </style>
    </head>
    <body>
        <div class="subject">Subject: {subject}</div>
        {html_body}
    </body>
    </html>
    """

    with open(file_path, "wb") as pdf_file:
        pisa_status = pisa.CreatePDF(pdf_content, dest=pdf_file)
        if pisa_status.err:
            print("Error converting HTML to PDF")
        else:
            print(f"PDF saved to: {file_path}")


def parse_sender(sender):
    """
    Parse the sender information to extract a readable name or email.
    """
    if "@" in sender:  # Looks like an email address
        return sender
    if "/CN=" in sender:  # Looks like a Distinguished Name (Exchange format)
        cn_index = sender.find("/CN=")
        return sender[cn_index + 4:].replace("-", " ")  # Extract after /CN= and make it more readable
    return sender  # Return as-is if no known patterns match


def process_inbox():
    # Connect to Outlook application
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    inbox = outlook.GetDefaultFolder(6)  # 6 refers to the Inbox

    # Define the time range (last 24 hours)
    now = datetime.now()
    past_24_hours = now - timedelta(hours=24*4)   # last 4 days

    # Restrict to emails received in the last 24 hours
    date_filter = f"[ReceivedTime] >= '{past_24_hours.strftime('%m/%d/%Y %H:%M %p')}'"
    messages = inbox.Items.Restrict(date_filter)

    count = 0
    for message in messages:
        if message.UnRead:  # Optionally, process only unread emails
            save_email_as_pdf(message)

            # Save attachments
            for attachment in message.Attachments:
                file_path = os.path.join(save_dir, attachment.FileName)
                attachment.SaveAsFile(file_path)
                print(f"Saved attachment: {file_path}")

            message.UnRead = False  # Mark as read after processing
            count += 1
    
    print(f"Emails processed: {count}.")


if __name__ == "__main__":
    process_inbox()