import smtplib

def send_email(sendto, subject, text):
    username = "YOUR_GMAIL_EMAIL"  # Change this!
    app_password = "YOUR_APP_PASSWORD"  # Change this to your App Password

    for i in range(3):
        try:
            print("Sending Email to {} (trial {})...".format(sendto, i+1))
            
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            
            server.login(username, app_password)
            msg = 'Subject: {}\n\n{}'.format(subject, text)
            server.sendmail(username, sendto, msg)
            server.quit()
            
            print("Email sent!")
            break
        except Exception as e:
            print("Failed to send email due to Exception:")
            print(e)

# Example usage
send_email("recipient@example.com", "Test Subject", "This is a test email.")
