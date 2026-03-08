# extract_title.py
def extract_title(markdown: str) -> str:
    for line in markdown.split("\n"):
        stripped = line.strip()
        if stripped.startswith("# "):
            title = stripped[2:].strip()
            if title == "":
                raise Exception("H1 title is empty")
            return title
    raise Exception("No H1 header found")