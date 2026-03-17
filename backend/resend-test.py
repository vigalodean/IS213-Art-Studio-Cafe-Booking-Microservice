import os
from dotenv import load_dotenv
import resend 

load_dotenv()
resend.api_key = os.getenv("RESEND_API_KEY")

def send_email(to_email: str, username: str):
    params = {
        "from": "artcafe@nicholassang.com",  # must be verified in Resend dashboard
        "to": [to_email],
        "subject": "Art Cafe Transaction Receipt",
        "html": f"""
        <h1>Hello {username}</h1>
        <p>Attached is your transaction receipt. Thank you for choosing us!</p>
        """
    }
    response = resend.Emails.send(params)
    print("Email sent:", response)

# Example usage
send_email("nicholasang.sg@gmail.com", "Nicholas")