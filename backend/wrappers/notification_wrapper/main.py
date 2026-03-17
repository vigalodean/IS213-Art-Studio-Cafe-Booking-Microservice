import resend 

async def send_email_notification_wrapper(to_email: str, username: str):
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
    print(response)