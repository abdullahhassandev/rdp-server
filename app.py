# Minimal RDP-like server using Flask.
from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# HTML template for RDP-like login form
LOGIN_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>RDP Login</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #0078D4;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .login-container {
            background-color: white;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            width: 350px;
        }
        h2 {
            color: #0078D4;
            margin-bottom: 20px;
            text-align: center;
        }
        input[type="text"], input[type="password"] {
            width: 100%;
            padding: 12px;
            margin: 8px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
        }
        button {
            background-color: #0078D4;
            color: white;
            padding: 12px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            width: 100%;
            font-size: 16px;
            margin-top: 10px;
        }
        button:hover {
            background-color: #005a9e;
        }
        .error {
            color: red;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h2>Remote Desktop Connection</h2>
        {% if error %}
        <div class="error">{{ error }}</div>
        {% endif %}
        <form method="POST" action="/login">
            <input type="text" name="username" placeholder="Username" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">Connect</button>
        </form>
    </div>
</body>
</html>
'''

SUCCESS_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Connected</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #0078D4;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .success-container {
            background-color: white;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        h2 {
            color: #0078D4;
        }
    </style>
</head>
<body>
    <div class="success-container">
        <h2>Connected Successfully!</h2>
        <p>Welcome, {{ username }}!</p>
        <p>RDP session established.</p>
    </div>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(LOGIN_TEMPLATE, error=None)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Dummy authentication - accepts any non-empty credentials
    if username and password:
        return render_template_string(SUCCESS_TEMPLATE, username=username)
    else:
        return render_template_string(LOGIN_TEMPLATE, error='Invalid credentials')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
