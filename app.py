from flask import Flask, render_template, request
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)   # Vercel expects this variable name

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

@app.route("/", methods=["GET", "POST"])
def index():
    status = None
    form_data = {
        "sender_name": "",
        "gmail": "",
        "app_password": "",
        "subject": "",
        "message": "",
        "recipients": ""
    }

    if request.method == "POST":
        form_data["sender_name"] = request.form["sender_name"]
        form_data["gmail"] = request.form["gmail"]
        form_data["app_password"] = request.form["app_password"]
        form_data["subject"] = request.form["subject"]
        form_data["message"] = request.form["message"]
        form_data["recipients"] = request.form["recipients"]

        recipients = form_data["recipients"].splitlines()
        sent_count, fail_count = 0, 0

        for recipient in recipients:
            recipient = recipient.strip()
            if not recipient:
                continue
            try:
                msg = MIMEMultipart()
                msg["From"] = f"{form_data['sender_name']} <{form_data['gmail']}>"
                msg["To"] = recipient
                msg["Subject"] = form_data["subject"]
                msg.attach(MIMEText(form_data["message"], "plain"))

                context = ssl.create_default_context()
                with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
                    server.login(form_data["gmail"], form_data["app_password"])
                    server.sendmail(form_data["gmail"], recipient, msg.as_string())
                sent_count += 1
            except Exception as e:
                print(f"Failed to {recipient}: {e}")
                fail_count += 1

        status = f"✅ Sent: {sent_count}, ❌ Failed: {fail_count}"

    return render_template("index.html", status=status, form_data=form_data)
