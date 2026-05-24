import os

def save_report(content: str, prefix: str, output_dir: str = "reports") -> str:
    if not content:
        raise ValueError("Cannot save empty content to file.")

    filename = f"{prefix}.md"
    filepath = os.path.join(output_dir, filename)

    try:
        os.makedirs(output_dir, exist_ok=True)
        
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)
            
        return filepath
        
    except IOError as e:
        raise RuntimeError(f"Failed to write report to {filepath}: {str(e)}") from e