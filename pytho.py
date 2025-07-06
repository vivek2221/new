import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
sender_email = "vshekhawat136@gmail.com"
receiver_email = "shekhawatvivek391@example.com"
app_password = "wata qvgp hdkn naqr"  
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Hello from Python"
body = "This is a test email sent using Python!"
message.attach(MIMEText(body, "plain"))
try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("✅ Email sent successfully!")
except Exception as e:
        print(f"❌ Error: {e}")
finally:
        server.quit()