import os
import glob
import zipfile
import xml.etree.ElementTree as ET

def get_docx_text(path):
    """Simple docx text extractor using standard library zipfile and xml parsing."""
    try:
        with zipfile.ZipFile(path) as docx:
            xml_content = docx.read('word/document.xml')
            root = ET.fromstring(xml_content)
            
            # The namespace for WordprocessingML
            ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
            
            paragraphs = []
            for para in root.iter('{' + ns['w'] + '}p'):
                texts = [node.text for node in para.iter('{' + ns['w'] + '}t') if node.text]
                if texts:
                    paragraphs.append("".join(texts))
            return "\n".join(paragraphs)
    except Exception as e:
        return f"Error reading {path}: {str(e)}"

def main():
    downloads_path = r"C:\Users\stv74\Downloads"
    resume_files = glob.glob(os.path.join(downloads_path, "*resume*"))
    resume_files += glob.glob(os.path.join(downloads_path, "*Resume*"))
    resume_files = list(set(resume_files)) # deduplicate
    
    output = []
    output.append(f"Found {len(resume_files)} resume files in Downloads:")
    for rf in resume_files:
        output.append(f"- {rf} ({os.path.getsize(rf)} bytes)")
        
    for rf in resume_files:
        if rf.endswith('.docx'):
            output.append("\n" + "="*40)
            output.append(f"EXTRACTED TEXT FROM: {rf}")
            output.append("="*40 + "\n")
            output.append(get_docx_text(rf))
            
    with open("extracted_resume.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(output))
    print("Done! Extracted text written to extracted_resume.txt")

if __name__ == "__main__":
    main()
