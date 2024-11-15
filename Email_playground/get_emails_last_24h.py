import win32com.client
from datetime import datetime, timedelta

def get_emails_last_24_hours():
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    inbox = outlook.GetDefaultFolder(6)  # 6 refers to the Inbox

    # Define the time range (last 24 hours)
    now = datetime.now()
    past_24_hours = now - timedelta(hours=24)

    # Restrict to emails received in the last 24 hours
    date_filter = f"[ReceivedTime] >= '{past_24_hours.strftime('%m/%d/%Y %H:%M %p')}'"
    messages = inbox.Items.Restrict(date_filter)

    for message in messages:
        print(f"Subject: {message.Subject}, Received: {message.ReceivedTime}")

if __name__ == "__main__":
    get_emails_last_24_hours()
