# Email-Sender
A simple Python method to send email to anyone directly.
You can use this Python method to:
1. Send email to anyone.


## Installation
1. Create a new GMail account just for this purpose (You may use your current GMail but not it's not recommended because you will need to turn off 2 Factor Authentication, which makes your account less secure).
2. Login to your new GMail account and go to, https://www.google.com/settings/security/lesssecureapps.
3. Toggle "Allow less secure apps" to be "ON":
![img](instruction-screenshot.png)
4. Copy the Python method in [send_email.py](send_email.py) and paste it in your code.:
5. Remember to change `YOUR_NEW_EMAIL` and `YOUR_NEW_EMAIL_PASSWORD` to your newly registered email credentials.
6. Call the method like so:
```
send_email("recipient@example.com", "Test Subject", "This is a test email.")

```
