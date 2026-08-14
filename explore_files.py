import os
import glob

def main():
    search_dirs = [
        r"C:\Users\stv74\Downloads",
        r"C:\Users\stv74\OneDrive\Documents"
    ]
    
    output = []
    for sdir in search_dirs:
        output.append(f"\nScanning directory: {sdir}")
        if not os.path.exists(sdir):
            output.append("Does not exist")
            continue
            
        # Recursive glob up to 3 levels
        files = []
        for ext in ['*.pdf', '*.docx', '*.txt', '*.html', '*.json', '*.xml']:
            files.extend(glob.glob(os.path.join(sdir, "**", ext), recursive=True))
            
        for f in sorted(list(set(files))):
            # Only display if size is less than 5MB and not in node_modules or system folders
            if "node_modules" not in f and ".git" not in f:
                try:
                    output.append(f"- {f} ({os.path.getsize(f)} bytes)")
                except Exception:
                    pass
                    
    with open("workspace_scan.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(output))
    print("Done! Scan written to workspace_scan.txt")

if __name__ == "__main__":
    main()
