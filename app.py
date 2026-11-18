from flask import Flask, render_template_string
import base64
import os

app = Flask(__name__)

def get_profile_image():
    for p in ['profile.jpeg', 'static/profile.jpeg']:
        if os.path.exists(p):
            with open(p, "rb") as f:
                return f"data:image/jpeg;base64,{base64.b64encode(f.read()).decode('utf-8')}"
    return ""

HTML_CODE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Zeeshan Arif | Portfolio</title>
  <style>
    :root {
      --bg: #0f172a;
      --surface: #1e293b;
      --primary: #38bdf8;
      --text: #f8fafc;
      --muted: #94a3b8;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: radial-gradient(circle at top right, #1e293b, #0f172a 70%);
      color: var(--text);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
      padding: 1.5rem;
    }
    .card {
      background: var(--surface);
      border: 1px solid #334155;
      border-radius: 20px;
      padding: 2.5rem 2rem;
      width: 100%;
      max-width: 480px;
      text-align: center;
      box-shadow: 0 20px 40px rgba(0,0,0,0.5);
    }
    .avatar-container {
      width: 140px;
      height: 140px;
      margin: 0 auto 1.5rem auto;
      border-radius: 50%;
      padding: 4px;
      background: linear-gradient(135deg, var(--primary), #10b981);
      box-shadow: 0 0 25px rgba(56, 189, 248, 0.35);
      overflow: hidden;
    }
    .avatar {
      width: 100%;
      height: 100%;
      border-radius: 50%;
      object-fit: cover;
      display: block;
    }
    .badge {
      display: inline-block;
      padding: 0.3rem 0.8rem;
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--primary);
      background: rgba(56, 189, 248, 0.1);
      border: 1px solid rgba(56, 189, 248, 0.3);
      border-radius: 999px;
      margin-bottom: 1rem;
    }
    h1 { font-size: 1.85rem; font-weight: 700; margin-bottom: 0.4rem; }
    .role { color: var(--primary); font-size: 0.95rem; font-weight: 600; margin-bottom: 0.75rem; }
    .location { color: var(--muted); font-size: 0.9rem; margin-bottom: 1.5rem; }
    .btn {
      display: inline-block;
      background: var(--primary);
      color: #0f172a;
      font-weight: 600;
      padding: 0.75rem 1.5rem;
      border-radius: 10px;
      text-decoration: none;
      transition: background 0.2s;
    }
    .btn:hover { background: #7dd3fc; }
  </style>
</head>
<body>
  <div class="card">
    <div class="avatar-container">
      {% if profile_img %}
        <img src="{{ profile_img }}" alt="Zeeshan Arif" class="avatar">
      {% endif %}
    </div>
    <div class="badge">Application & Systems Engineer</div>
    <h1>Zeeshan Arif</h1>
    <div class="role">IT & Network Engineer @ Mosanada Logistics</div>
    <p class="location">📍 Jeddah, Saudi Arabia</p>
    <a href="https://www.linkedin.com/in/zeeshan-arif-001058250" target="_blank" class="btn">Connect on LinkedIn</a>
  </div>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_CODE, profile_img=get_profile_image())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    from flask import Flask, render_template_string

app = Flask(__name__)

HTML_CODE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Zeeshan Arif | Portfolio</title>
  <style>
    :root {
      --bg: #0f172a;
      --surface: #1e293b;
      --primary: #38bdf8;
      --text: #f8fafc;
      --muted: #94a3b8;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: radial-gradient(circle at top right, #1e293b, #0f172a 70%);
      color: var(--text);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
      padding: 1.5rem;
    }
    .card {
      background: var(--surface);
      border: 1px solid #334155;
      border-radius: 20px;
      padding: 2.5rem 2rem;
      width: 100%;
      max-width: 480px;
      text-align: center;
      box-shadow: 0 20px 40px rgba(0,0,0,0.5);
    }
    .avatar-container {
      width: 140px;
      height: 140px;
      margin: 0 auto 1.5rem auto;
      border-radius: 50%;
      padding: 4px;
      background: linear-gradient(135deg, var(--primary), #10b981);
      box-shadow: 0 0 25px rgba(56, 189, 248, 0.35);
      overflow: hidden;
    }
    .avatar {
      width: 100%;
      height: 100%;
      border-radius: 50%;
      object-fit: cover;
      display: block;
    }
    .badge {
      display: inline-block;
      padding: 0.3rem 0.8rem;
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--primary);
      background: rgba(56, 189, 248, 0.1);
      border: 1px solid rgba(56, 189, 248, 0.3);
      border-radius: 999px;
      margin-bottom: 1rem;
    }
    h1 { font-size: 1.85rem; font-weight: 700; margin-bottom: 0.4rem; }
    .role { color: var(--primary); font-size: 0.95rem; font-weight: 600; margin-bottom: 0.75rem; }
    .location { color: var(--muted); font-size: 0.9rem; margin-bottom: 1.5rem; }
    .btn {
      display: inline-block;
      background: var(--primary);
      color: #0f172a;
      font-weight: 600;
      padding: 0.75rem 1.5rem;
      border-radius: 10px;
      text-decoration: none;
      transition: background 0.2s;
    }
    .btn:hover { background: #7dd3fc; }
  </style>
</head>
<body>
  <div class="card">
    <div class="avatar-container">
      <img src="https://raw.githubusercontent.com/Zeeshan-Arif-Networks/New-Portfolio/main/static/profile.jpeg" alt="Zeeshan Arif" class="avatar">
    </div>
    <div class="badge">Application & Systems Engineer</div>
    <h1>Zeeshan Arif</h1>
    <div class="role">IT & Network Engineer @ Mosanada Logistics</div>
    <p class="location">📍 Jeddah, Saudi Arabia</p>
    <a href="https://www.linkedin.com/in/zeeshan-arif-001058250" target="_blank" class="btn">Connect on LinkedIn</a>
  </div>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_CODE)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
