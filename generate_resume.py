import json
from jinja2 import Environment, FileSystemLoader

# Load JSON file
with open("resume.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Setup Jinja
env = Environment(loader=FileSystemLoader("."))
template = env.get_template("resume_template.html")

# Render HTML
output = template.render(data=data)

# Save to file
with open("resume.html", "w", encoding="utf-8") as f:
    f.write(output)

print("✅ Resume generated as resume.html")
