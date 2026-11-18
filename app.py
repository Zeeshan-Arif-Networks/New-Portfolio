from flask import Flask, render_template

app = Flask(__name__)

PORTFOLIO_DATA = {
    "name": "Zeeshan Arif",
    "location": "Jeddah, Saudi Arabia",
    "badge": "Interactive Portfolio",
    "subtitle": "Select an option below to explore profile, designation, and current work status.",
    "sections": {
        "name": {
            "title": "Zeeshan Arif",
            "subtitle": "Jeddah, Saudi Arabia",
            "status_badge": "Verified Profile",
            "description": "Experienced IT Infrastructure, Systems, and Network Engineer with 5+ years of hands-on expertise managing enterprise servers, Cisco network architecture, Windows Server hybrid environments, and business logistics applications.",
            "tags": [
                "Cisco CCNA",
                "Windows Server Hybrid Admin",
                "Active Directory & GPO",
                "FortiGate & Switching",
                "SQL & Power BI",
                "Python & Automation"
            ],
            "links": [
                {"label": "LinkedIn Profile", "url": "https://www.linkedin.com/in/zeeshan-arif-001058250", "primary": True},
                {"label": "GitHub Repositories", "url": "https://github.com/Zeeshan-Arif-Networks", "primary": False}
            ]
        },
        "designation": {
            "title": "Designation & Core Responsibilities",
            "subtitle": "Application & Systems Support Engineer | IT & Network Engineer",
            "status_badge": "",
            "description": "Delivering end-to-end IT operations, infrastructure deployment, and enterprise application support across corporate offices and multi-site logistics facilities.",
            "cards": [
                {
                    "heading": "Network & Security",
                    "text": "Cisco Catalyst switches, routers, FortiGate firewalls, Wi-Fi APs, IP telephony, and CCTV/biometric access systems."
                },
                {
                    "heading": "Systems & Cloud",
                    "text": "Windows Server, Active Directory, Azure Entra ID, VMware/Hyper-V virtualization, and Endpoint Central management."
                },
                {
                    "heading": "Enterprise Applications",
                    "text": "Oracle EBS, document management servers, automated scanning systems, and SQL database administration."
                },
                {
                    "heading": "Data & Automation",
                    "text": "Building reporting dashboards and workflow automations using Power BI, SQL, Power Automate, and Python."
                }
            ]
        },
        "status": {
            "title": "Current Work Status",
            "subtitle": "Active Full-Time & Open to Remote Opportunities",
            "status_badge": "Open to Connect",
            "description": "Currently serving full-time as an Application & Systems Support Engineer / IT & Network Engineer at Mosanada Logistics Services (Jeddah, Saudi Arabia).",
            "cards": [
                {
                    "heading": "Primary Role",
                    "text": "Full-Time On-Site IT Infrastructure & Enterprise Systems Support (Jeddah, KSA)."
                },
                {
                    "heading": "Remote Availability",
                    "text": "Available for part-time remote IT support, systems administration, and data analytics projects."
                }
            ],
            "links": [
                {"label": "Message on LinkedIn", "url": "https://www.linkedin.com/in/zeeshan-arif-001058250", "primary": True}
            ]
        }
    }
}


@app.route("/")
def home():
    return render_template("index.html", data=PORTFOLIO_DATA)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
