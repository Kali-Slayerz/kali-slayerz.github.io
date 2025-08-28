import json
from jinja2 import Environment, FileSystemLoader
import os

# Load Jinja environment
env = Environment(loader=FileSystemLoader("templates"))

# Load template
template = env.get_template("resume_template.html")

# List of resumes to generate
resumes = [
    {"json_file": "kali.json", "output": "index.html", "link_to": "resume.html"},
    {"json_file": "sid.json", "output": "resume.html", "link_to": "index.html"}
]

# Generate HTML for each resume
for res in resumes:
    with open(res["json_file"], "r") as f:
        data = json.load(f)

    # Add link to other resume
    data["switch_link"] = res["link_to"]

    # Render template
    html_content = template.render(data=data)

    # Save HTML
    with open(res["output"], "w", encoding="utf-8") as f:
        f.write(html_content)

print("Resumes generated successfully!")
