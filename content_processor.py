import os
import markdown
from datetime import datetime

def process_markdown_files(folder_path):
    newsletters = []

    for file in os.listdir(folder_path):
        if file.endswith(".md"):
            path = os.path.join(folder_path, file)

            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            html = markdown.markdown(content)

            lines = content.split("\n")

            title = lines[0].replace("#", "").strip()

            tags = "General"
            for line in lines:
                if line.lower().startswith("tags:"):
                    tags = line.replace("Tags:", "").strip()

            newsletters.append({
                "filename": file,
                "title": title,
                "tags": tags,
                "html": html,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

    return newsletters