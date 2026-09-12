from flask import Flask, render_template, request
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

@app.route("/", methods=["GET", "POST"])
def index():
    status = None
    if request.method == "POST":
        sender_name = request.form["sender_name"]
        sender_email = request.form["gmail"]
        app_password = request.form["app_password"]
        subject = request.form["subject"]
        message_body = request.form["message"]
        recipients = request.form["recipients"].splitlines()

        sent_count, fail_count = 0, 0

        for recipient in recipients:
            recipient = recipient.strip()
            if not recipient:
                continue
            try:
                msg = MIMEMultipart()
                msg["From"] = f"{sender_name} <{sender_email}>"
                msg["To"] = recipient
                msg["Subject"] = subject
                msg.attach(MIMEText(message_body, "plain"))

                context = ssl.create_default_context()
                with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
                    server.login(sender_email, app_password)
                    server.sendmail(sender_email, recipient, msg.as_string())
                sent_count += 1
            except Exception as e:
                print(f"Failed to {recipient}: {e}")
                fail_count += 1

        status = f"✅ Sent: {sent_count}, ❌ Failed: {fail_count}"

    return render_template("index.html", status=status)

if __name__ == "__main__":
    app.run(debug=True)
