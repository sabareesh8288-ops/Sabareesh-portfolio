import os
import glob

def main():
    downloads_path = r"C:\Users\stv74\Downloads"
    output = []
    output.append("Top-level files in Downloads:")
    if os.path.exists(downloads_path):
        for f in os.listdir(downloads_path):
            full_path = os.path.join(downloads_path, f)
            if os.path.isfile(full_path) and any(f.lower().endswith(ext) for ext in ['.pdf', '.docx', '.txt', '.doc', '.xlsx', '.png', '.jpg']):
                output.append(f"- {f} ({os.path.getsize(full_path)} bytes)")
                
    output.append("\nTop-level files inside project directories:")
    doc_path = r"C:\Users\stv74\OneDrive\Documents"
    for proj in ["frcl.app", "jarvis3.0", "skincare proto"]:
        proj_path = os.path.join(doc_path, proj)
        output.append(f"\nProject: {proj}")
        if os.path.exists(proj_path):
            for root, dirs, files in os.walk(proj_path):
                # Only go 2 levels deep
                depth = root[len(proj_path):].count(os.sep)
                if depth > 1:
                    continue
                for f in files:
                    if any(f.lower().endswith(ext) for ext in ['.html', '.css', '.js', '.py', '.json', '.md', '.txt']):
                        output.append(f"  * {os.path.join(root, f)} ({os.path.getsize(os.path.join(root, f))} bytes)")
        else:
            output.append("  Does not exist")
            
    with open("list_downloads.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(output))

if __name__ == "__main__":
    main()
