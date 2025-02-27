#!/usr/bin/env python3

import re
import os
import html

def parse_changelog(content):
    version_blocks = re.split(r'^(?=# \d|\d)', content, flags=re.MULTILINE)
    version_blocks = [block for block in version_blocks if block.strip()]

    versions = []
    for block in version_blocks:
        lines = block.strip().split('\n')

        version_line = lines[0]
        if version_line.startswith('# '):
            version = version_line[2:].strip()
        else:
            version = version_line.strip()

        changes = []
        fixed_issues = []

        current_section = "changes"
        for line in lines[1:]:
            if line.strip() == "## Fixed issues":
                current_section = "fixed_issues"
                continue

            if line.strip() and line.strip().startswith('-'):
                item = line.strip()[1:].strip()
                if current_section == "changes":
                    changes.append(item)
                else:
                    fixed_issues.append(item)

        versions.append({
            "version": version,
            "changes": changes,
            "fixed_issues": fixed_issues
        })

    return versions

def generate_html(version_data):
    version = version_data["version"]
    changes = version_data["changes"]
    fixed_issues = version_data["fixed_issues"]

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NetXMS Version {version} changes</title>
    <style>
        body {{
            font-family: system-ui, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
        }}
        h1 {{
            color: #2c3e50;
            border-bottom: 2px solid #eee;
            padding-bottom: 10px;
        }}
        h2 {{
            color: #3498db;
            margin-top: 20px;
        }}
        ul {{
            padding-left: 20px;
        }}
        li {{
            margin-bottom: 8px;
        }}
        .logo {{
            position: absolute;
            top: 30px;
            right: 30px;
            align-items: flex-end;
        }}
    </style>
</head>
<body>
    <img class="logo" src="https://netxms.com/assets/images/logo-netxms-changelog.svg" width="32px" />
    <h1>Version {version}</h1>

"""

    if changes:
        html_content += "    <h2>Changes</h2>\n    <ul>\n"
        for change in changes:
            html_content += f"        <li>{html.escape(change)}</li>\n"
        html_content += "    </ul>\n"

    if fixed_issues:
        html_content += "    <h2>Fixed Issues</h2>\n    <ul>\n"
        for issue in fixed_issues:
            html_content += f"        <li>{html.escape(issue)}</li>\n"
        html_content += "    </ul>\n"

    html_content += """</body>
</html>
"""

    return html_content

def generate_index_html(versions, output_dir="changelog-html"):
    index_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NetXMS Changelog Index</title>
    <style>
        body {
            font-family: system-ui, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        h1 {
            color: #2c3e50;
            border-bottom: 2px solid #eee;
            padding-bottom: 10px;
        }
        ul {
            padding-left: 20px;
        }
        li {
            margin-bottom: 8px;
        }
        a {
            color: #3498db;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>NetXMS Changelog Index</h1>
    <ul>
"""

    for version_data in versions:
        version = version_data["version"]
        safe_version = version.replace('.', '_')
        index_content += f'        <li><a href="{safe_version}.html">Version {version}</a></li>\n'

    index_content += """    </ul>
</body>
</html>
"""

    index_filename = f"{output_dir}/index.html"
    with open(index_filename, 'w', encoding='utf-8') as f:
        f.write(index_content)

    print(f"Generated {index_filename}")

def save_html_files(versions, output_dir="changelog-html"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for version_data in versions:
        version = version_data["version"]
        safe_version = version.replace('.', '_')
        filename = f"{output_dir}/{safe_version}.html"

        html_content = generate_html(version_data)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)

        print(f"Generated {filename}")

def main():
    with open('ChangeLog.md') as f:
        content = f.read()

    print("Parsing changelog...")
    versions = parse_changelog(content)

    print(f"Found {len(versions)} versions")

    output_dir = "changelog-html"
    print("Sorting versions...")
    versions.sort(key=lambda x: x["version"], reverse=True)

    print("Generating HTML files...")
    save_html_files(versions)

    print("Generating index.html...")
    generate_index_html(versions, output_dir)

    print("Done!")

if __name__ == "__main__":
    main()
