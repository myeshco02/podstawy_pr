import re

def read_email_content():
    try:
        with open('email.txt', 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print("Error: The file 'email.txt' was not found.")
        return None

def email_sender():
    email = read_email_content()
    if email:
        match = re.search(r"From: .* <(.+?)>", email)
        return match.group(1) if match else "No sender found"
    return None

def email_recipient():
    email = read_email_content()
    if email:
        match = re.search(r"To: .* <(.+?)>", email)
        return match.group(1) if match else "No recipient found"
    return None

def email_subject():
    email = read_email_content()
    if email:
        match = re.search(r"Subject: (.+)", email)
        return match.group(1) if match else "No subject found"
    return None

def email_body():
    email = read_email_content()
    if email:
        body = re.split(r"\n\n", email, 1)[1] if '\n\n' in email else 'No body content'
        return body.strip()
    return None

if __name__ == "__main__":
    print("Sender:", email_sender())
    print("Recipient:", email_recipient())
    print("Subject:", email_subject())
    print("Body:", email_body())
