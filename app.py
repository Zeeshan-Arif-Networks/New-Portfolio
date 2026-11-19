from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Zeeshan Arif | Portfolio</title>
  <style>
    :root {
      --bg: #0f172a;
      --surface: #1e293b;
      --surface-hover: #273549;
      --border: #334155;
      --primary: #38bdf8;
      --primary-glow: rgba(56, 189, 248, 0.35);
      --accent: #10b981;
      --text: #f8fafc;
      --muted: #94a3b8;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
      background: radial-gradient(circle at top right, #1e293b, #0f172a 70%);
      color: var(--text);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 2.5rem 1rem;
    }
    .container { width: 100%; max-width: 960px; }
    header { text-align: center; margin-bottom: 2.5rem; }

    /* Profile Image Styling */
    .profile-img-container {
      width: 140px;
      height: 140px;
      margin: 0 auto 1.25rem auto;
      border-radius: 50%;
      padding: 4px;
      background: linear-gradient(135deg, var(--primary), var(--accent));
      box-shadow: 0 0 25px var(--primary-glow);
    }
    .profile-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      border-radius: 50%;
      display: block;
    }

    .badge {
      display: inline-block; padding: 0.35rem 0.9rem; font-size: 0.8rem;
      letter-spacing: 0.08em; text-transform: uppercase; color: var(--primary);
      background: rgba(56, 189, 248, 0.1); border: 1px solid rgba(56, 189, 248, 0.3);
      border-radius: 999px; margin-bottom: 0.9rem;
    }
    h1 { font-size: 2.5rem; font-weight: 700; letter-spacing: -0.02em; }
    .subtitle { color: var(--muted); margin-top: 0.5rem; font-size: 1.05rem; }

    /* Prominent Header Resume Button */
    .header-actions {
      margin-top: 1.35rem;
      display: flex;
      justify-content: center;
      gap: 0.75rem;
      flex-wrap: wrap;
    }
    .btn-resume-hero {
      display: inline-flex;
      align-items: center;
      gap: 0.55rem;
      padding: 0.75rem 1.5rem;
      border-radius: 999px;
      font-weight: 700;
      font-size: 0.95rem;
      color: #0f172a;
      background: linear-gradient(135deg, var(--primary), #7dd3fc);
      border: none;
      cursor: pointer;
      box-shadow: 0 8px 24px var(--primary-glow);
      transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .btn-resume-hero:hover {
      transform: translateY(-2px);
      box-shadow: 0 12px 28px rgba(56, 189, 248, 0.5);
    }

    .options-grid {
      display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 1.25rem; margin-bottom: 2rem;
    }
    .option-card {
      background: var(--surface); border: 1px solid var(--border);
      border-radius: 16px; padding: 1.6rem; text-align: left; color: inherit;
      cursor: pointer; transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease, background 0.2s ease;
      display: flex; flex-direction: column; justify-content: space-between;
    }
    .option-card:hover { transform: translateY(-4px); background: var(--surface-hover); border-color: var(--primary); }
    .option-card.active { border-color: var(--primary); box-shadow: 0 0 0 3px var(--primary-glow); background: #1e324a; }
    .card-index { font-size: 0.75rem; font-weight: 700; color: var(--primary); letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 0.6rem; }
    .card-title { font-size: 1.35rem; font-weight: 700; margin-bottom: 0.45rem; }
    .card-preview { color: var(--muted); font-size: 0.92rem; line-height: 1.45; }
    .card-action { margin-top: 1.2rem; font-size: 0.85rem; font-weight: 600; color: var(--primary); display: inline-flex; align-items: center; gap: 0.35rem; }
    .detail-panel {
      background: var(--surface); border: 1px solid var(--border);
      border-radius: 18px; padding: 2rem; box-shadow: 0 20px 40px rgba(0, 0, 0, 0.35);
    }
    .panel-header {
      display: flex; flex-wrap: wrap; justify-content: space-between;
      align-items: center; gap: 1rem; border-bottom: 1px solid var(--border);
      padding-bottom: 1.2rem; margin-bottom: 1.5rem;
    }
    .panel-header h2 { font-size: 1.65rem; }
    .status-pill {
      display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.4rem 0.9rem;
      border-radius: 999px; font-size: 0.85rem; font-weight: 600;
      background: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.35);
    }
    .dot { width: 8px; height: 8px; border-radius: 50%; background: #10b981; box-shadow: 0 0 8px #10b981; }
    .panel-body p { color: #cbd5e1; line-height: 1.65; margin-bottom: 1.25rem; }
    .tags { display: flex; flex-wrap: wrap; gap: 0.6rem; margin-bottom: 1.5rem; }
    .tag { background: #0f172a; border: 1px solid var(--border); padding: 0.45rem 0.85rem; border-radius: 8px; font-size: 0.85rem; color: #e2e8f0; }
    .list-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem; margin-bottom: 1.25rem; }
    .info-box { background: #0f172a; border: 1px solid var(--border); border-radius: 12px; padding: 1.1rem; }
    .info-box h4 { color: var(--primary); font-size: 0.9rem; margin-bottom: 0.4rem; }
    .info-box p { margin: 0; font-size: 0.9rem; color: var(--muted); }
    .btn-group { display: flex; flex-wrap: wrap; gap: 0.8rem; margin-top: 1rem; }
    .btn { padding: 0.65rem 1.25rem; border-radius: 10px; font-weight: 600; font-size: 0.9rem; text-decoration: none; cursor: pointer; border: 1px solid transparent; transition: all 0.2s ease; display: inline-flex; align-items: center; gap: 0.4rem; }
    .btn-primary { background: var(--primary); color: #0f172a; }
    .btn-primary:hover { background: #7dd3fc; }
    .btn-outline { background: transparent; border-color: var(--border); color: var(--text); }
    .btn-outline:hover { border-color: var(--primary); color: var(--primary); }

    /* Resume Modal Popup */
    .modal-backdrop {
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(15, 23, 42, 0.85);
      backdrop-filter: blur(6px);
      z-index: 1000;
      align-items: center;
      justify-content: center;
      padding: 1rem;
    }
    .modal-backdrop.open { display: flex; }
    .modal-box {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 18px;
      width: 100%;
      max-width: 900px;
      height: 88vh;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      box-shadow: 0 25px 50px rgba(0, 0, 0, 0.6);
    }
    .modal-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 1rem 1.4rem;
      border-bottom: 1px solid var(--border);
      gap: 0.75rem;
      flex-wrap: wrap;
    }
    .modal-top h3 { font-size: 1.15rem; }
    .modal-controls { display: flex; gap: 0.6rem; align-items: center; }
    .modal-frame {
      width: 100%;
      flex: 1;
      border: none;
      background: #0f172a;
    }

    footer { margin-top: 2.5rem; text-align: center; color: var(--muted); font-size: 0.85rem; }
  </style>
</head>
<body>
  <div class="container">
    <header>
      <div class="profile-img-container">
        <img src="{{ url_for('static', filename='profile.jpeg') }}" alt="Zeeshan Arif" class="profile-img" />
      </div>
      <div class="badge">Interactive Portfolio</div>
      <h1>Zeeshan Arif</h1>
      <p class="subtitle">Select an option below to explore profile, designation, and current work status.</p>
      <div class="header-actions">
        <button type="button" class="btn-resume-hero" onclick="openResume()">
          &#128196; View Resume
        </button>
      </div>
    </header>

    <section class="options-grid" role="tablist">
      <button class="option-card active" onclick="selectTab('name', this)">
        <div>
          <div class="card-index">Option 01</div>
          <div class="card-title">Zeeshan Arif</div>
          <p class="card-preview">Personal profile, location, technical skills, and professional links.</p>
        </div>
        <span class="card-action">View Profile &rarr;</span>
      </button>

      <button class="option-card" onclick="selectTab('designation', this)">
        <div>
          <div class="card-index">Option 02</div>
          <div class="card-title">Designation</div>
          <p class="card-preview">Application & Systems Support Engineer | IT & Network Engineer.</p>
        </div>
        <span class="card-action">View Role Details &rarr;</span>
      </button>

      <button class="option-card" onclick="selectTab('status', this)">
        <div>
          <div class="card-index">Option 03</div>
          <div class="card-title">Work Status</div>
          <p class="card-preview">Current employment status, availability, and collaboration options.</p>
        </div>
        <span class="card-action">Check Availability &rarr;</span>
      </button>
    </section>

    <main id="detail-panel" class="detail-panel"></main>

    <footer>
      &copy; 2026 Zeeshan Arif. Powered by Python &amp; Flask.
    </footer>
  </div>

  <!-- Resume Viewer Modal -->
  <div id="resume-modal" class="modal-backdrop" onclick="if(event.target === this) closeResume()">
    <div class="modal-box">
      <div class="modal-top">
        <h3>Zeeshan Arif &mdash; Curriculum Vitae</h3>
        <div class="modal-controls">
          <a href="{{ url_for('static', filename='resume.pdf') }}" target="_blank" rel="noopener" class="btn btn-outline">Open in New Tab</a>
          <a href="{{ url_for('static', filename='resume.pdf') }}" download="Zeeshan_Arif_Resume.pdf" class="btn btn-primary">Download PDF</a>
          <button type="button" class="btn btn-outline" onclick="closeResume()">&#10005; Close</button>
        </div>
      </div>
      <iframe class="modal-frame" src="{{ url_for('static', filename='resume.pdf') }}" title="Zeeshan Arif Resume"></iframe>
    </div>
  </div>

  <script>
    const sections = {{ sections | tojson }};
    function selectTab(key, element) {
      document.querySelectorAll('.option-card').forEach(card => card.classList.remove('active'));
      element.classList.add('active');
      document.getElementById('detail-panel').innerHTML = sections[key];
    }
    function openResume() {
      document.getElementById('resume-modal').classList.add('open');
      document.body.style.overflow = 'hidden';
    }
    function closeResume() {
      document.getElementById('resume-modal').classList.remove('open');
      document.body.style.overflow = '';
    }
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape') closeResume();
    });
    document.getElementById('detail-panel').innerHTML = sections.name;
  </script>
</body>
</html>
"""

PORTFOLIO_SECTIONS = {
    "name": """
        <div class="panel-header">
          <div>
            <h2>Zeeshan Arif</h2>
            <span style="color: var(--muted); font-size: 0.95rem;">Jeddah, Saudi Arabia</span>
          </div>
          <div class="status-pill"><span class="dot"></span> Verified Profile</div>
        </div>
        <div class="panel-body">
          <p>Experienced IT Infrastructure, Systems, and Network Engineer with 5+ years of hands-on expertise managing enterprise servers, Cisco network architecture, Windows Server hybrid environments, and business logistics applications.</p>
          <div class="tags">
            <span class="tag">Cisco CCNA</span>
            <span class="tag">Windows Server Hybrid Admin</span>
            <span class="tag">Active Directory &amp; GPO</span>
            <span class="tag">FortiGate &amp; Switching</span>
            <span class="tag">SQL &amp; Power BI</span>
            <span class="tag">Python &amp; Automation</span>
          </div>
          <div class="btn-group">
            <button type="button" onclick="openResume()" class="btn btn-primary">View Resume</button>
            <a href="https://www.linkedin.com/in/zeeshan-arif-001058250" target="_blank" rel="noopener" class="btn btn-outline">LinkedIn Profile</a>
            <a href="https://github.com/Zeeshan-Arif-Networks" target="_blank" rel="noopener" class="btn btn-outline">GitHub Repositories</a>
          </div>
        </div>
    """,
    "designation": """
        <div class="panel-header">
          <div>
            <h2>Designation &amp; Core Responsibilities</h2>
            <span style="color: var(--muted); font-size: 0.95rem;">Application &amp; Systems Support Engineer | IT &amp; Network Engineer</span>
          </div>
        </div>
        <div class="panel-body">
          <p>Delivering end-to-end IT operations, infrastructure deployment, and enterprise application support across corporate offices and multi-site logistics facilities.</p>
          <div class="list-grid">
            <div class="info-box">
              <h4>Network &amp; Security</h4>
              <p>Cisco Catalyst switches, routers, FortiGate firewalls, Wi-Fi APs, IP telephony, and CCTV/biometric access systems.</p>
            </div>
            <div class="info-box">
              <h4>Systems &amp; Cloud</h4>
              <p>Windows Server, Active Directory, Azure Entra ID, VMware/Hyper-V virtualization, and Endpoint Central management.</p>
            </div>
            <div class="info-box">
              <h4>Enterprise Applications</h4>
              <p>Oracle EBS, document management servers, automated scanning systems, and SQL database administration.</p>
            </div>
            <div class="info-box">
              <h4>Data &amp; Automation</h4>
              <p>Building reporting dashboards and workflow automations using Power BI, SQL, Power Automate, and Python.</p>
            </div>
          </div>
        </div>
    """,
    "status": """
        <div class="panel-header">
          <div>
            <h2>Current Work Status</h2>
            <span style="color: var(--muted); font-size: 0.95rem;">Active Full-Time &amp; Open to Remote Opportunities</span>
          </div>
          <div class="status-pill"><span class="dot"></span> Open to Connect</div>
        </div>
        <div class="panel-body">
          <p>Currently serving full-time as an <strong>Application &amp; Systems Support Engineer / IT &amp; Network Engineer</strong> at Mosanada Logistics Services (Jeddah, Saudi Arabia).</p>
          <div class="list-grid">
            <div class="info-box">
              <h4>Primary Role</h4>
              <p>Full-Time On-Site IT Infrastructure &amp; Enterprise Systems Support (Jeddah, KSA).</p>
            </div>
            <div class="info-box">
              <h4>Remote Availability</h4>
              <p>Available for part-time remote IT support, systems administration, and data analytics projects.</p>
            </div>
          </div>
          <div class="btn-group">
            <button type="button" onclick="openResume()" class="btn btn-primary">View Resume</button>
            <a href="https://www.linkedin.com/in/zeeshan-arif-001058250" target="_blank" rel="noopener" class="btn btn-outline">Message on LinkedIn</a>
          </div>
        </div>
    """
}

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE, sections=PORTFOLIO_SECTIONS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
