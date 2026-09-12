<!DOCTYPE html>
<html>
<head>
    <title>Bulk Mail Sender</title>
    <style>
        body { font-family: Arial; background: #222; color: #eee; text-align: center; }
        input, textarea { width: 80%; padding: 10px; margin: 5px; }
        button { padding: 10px 20px; background: green; color: white; border: none; cursor: pointer; }
        button:disabled { background: gray; cursor: not-allowed; }
        .status { margin-top: 20px; font-weight: bold; }
    </style>
    <script>
        function disableButton() {
            const btn = document.getElementById("sendBtn");
            btn.disabled = true;
            btn.innerText = "Sending...";
        }
        function enableButton() {
            const btn = document.getElementById("sendBtn");
            btn.disabled = false;
            btn.innerText = "Send All";
        }
    </script>
</head>
<body>
    <h1>Bulk Mail Sender</h1>
    <form method="POST" onsubmit="disableButton()">
        <input type="text" name="sender_name" placeholder="Sender Name" value="{{ form_data.sender_name }}"><br>
        <input type="email" name="gmail" placeholder="Your Gmail" value="{{ form_data.gmail }}"><br>
        <input type="password" name="app_password" placeholder="16-digit App Password" value="{{ form_data.app_password }}"><br>
        <input type="text" name="subject" placeholder="Email Subject" value="{{ form_data.subject }}"><br>
        <textarea name="message" placeholder="Message Body (Plain Text)" rows="6">{{ form_data.message }}</textarea><br>
        <textarea name="recipients" placeholder="Recipients (one per line)" rows="6">{{ form_data.recipients }}</textarea><br>
        <button id="sendBtn" type="submit">Send All</button>
    </form>
    {% if status %}
        <div class="status">{{ status }}</div>
        <script>enableButton();</script>
    {% endif %}
</body>
</html>
