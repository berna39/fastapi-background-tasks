import requests
from dotenv import dotenv_values

ENV = dotenv_values()

def do_send_mail(to: str, subject: str, message: str):
    print("Mail being sent!")
    res = requests.post(ENV["APP_MAILGUN_LINK"],
                            auth=("api", ENV["APP_MAIL_KEY"]),
                            data={  "from": ENV["APP_MAIL_FROM"],
                                    "to": to,
                                    "subject": subject,
                                    "text": message })
