import win32com.client

def get_last_50_emails():
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    inbox = outlook.GetDefaultFolder(6)  # 6 refers to the Inbox

    # Get all items and sort them by ReceivedTime in descending order
    messages = inbox.Items
    messages.Sort("[ReceivedTime]", True)  # True for descending order
    last_50_emails = messages.GetFirst()

    count = 0
    while last_50_emails and count < 50:
        print(f"Subject: {last_50_emails.Subject}, Received: {last_50_emails.ReceivedTime}")
        last_50_emails = messages.GetNext()
        count += 1

if __name__ == "__main__":
    get_last_50_emails()
