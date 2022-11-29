import os
import smtplib
from email.message import EmailMessage


def auto_email():
    login = "Enter your login here"
    user = input("Please enter your name: ")
    email = input("Please enter your email: ")
    message = EmailMessage()
    message.set_content(
        f"""Dear {user},
        Welcome to Python!"""
    )
    message["Subject"] = "Enter subject here"
    message["From"] = login
    message["To"] = email
    s = smtplib.SMTP("smtp.office365.com", 587)
    s.starttls()
    s.login(login, "Enter your password here")
    s.send_message(message)
    s.quit()
    print("Email sent!")


auto_email()
