import json
import argparse
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def render_resume(data, template_path, output_path, switch_to=None):
    env = Environment(
        loader=FileSystemLoader("."),
        autoescape=select_autoescape(["html", "xml"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    template = env.get_template(template_path)
    html = template.render(data=data, switch_to=switch_to)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html, encoding="utf-8")
    print(f"✅ Wrote: {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Build resume HTML from JSON + Jinja2")
    parser.add_argument("--json1", default="kali.json", help="Primary JSON path")
    parser.add_argument("--json2", default="", help="Secondary JSON path (optional)")
    parser.add_argument("--template", default="resume_template.html.j2", help="Template path")
    parser.add_argument("--outdir", default="resume", help="Output directory")
    args = parser.parse_args()

    outdir = Path(args.outdir)
    # primary
    data1 = load_json(args.json1)
    render_resume(
        data=data1,
        template_path=args.template,
        output_path=outdir / "index.html",
        switch_to="resume.html" if args.json2 else None
    )

    # secondary (optional, for later when you add your real resume json)
    if args.json2:
        data2 = load_json(args.json2)
        render_resume(
            data=data2,
            template_path=args.template,
            output_path=outdir / "resume.html",
            switch_to="index.html"
        )
    else:
        # If not provided, still generate a second file identical to index.html,
        # so links won't 404 if you wire it later.
        render_resume(
            data=data1,
            template_path=args.template,
            output_path=outdir / "resume.html",
            switch_to="index.html"
        )

if __name__ == "__main__":
    main()
