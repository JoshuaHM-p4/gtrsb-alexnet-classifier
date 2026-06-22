import os
import re
import subprocess

def escape_latex(text):
    # Order is important: escape backslash first
    text = text.replace('\\', '\\textbackslash{}')
    text = text.replace('%', '\\%')
    text = text.replace('&', '\\&')
    text = text.replace('_', '\\_')
    text = text.replace('$', '\\$')
    text = text.replace('#', '\\#')
    text = text.replace('{', '\\{')
    text = text.replace('}', '\\}')
    
    # Replace markdown bold and italic
    text = re.sub(r'\*\*(.*?)\*\*', r'\\textbf{\1}', text)
    text = re.sub(r'\*(.*?)\*', r'\\textit{\1}', text)
    
    # Smart quotes and clean up quotes
    text = text.replace('“', '``').replace('”', "''")
    text = text.replace('‘', '`').replace('’', "'")
    
    return text

def parse_markdown(md_path):
    if not os.path.exists(md_path):
        raise FileNotFoundError(f"Markdown file not found at {md_path}")
        
    with open(md_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    slides = []
    current_slide = None
    in_speech = False
    speech_lines = []
    
    for line in lines:
        line_str = line.strip()
        
        # Check for Slide Heading
        slide_match = re.match(r'^##\s+(Slide\s+\d+:\s+.*)', line_str)
        if slide_match:
            # If we had a previous slide, finalize its speech
            if current_slide and speech_lines:
                current_slide['speech'] = " ".join(speech_lines)
                speech_lines = []
                
            current_slide = {
                'title': slide_match.group(1),
                'heading': '',
                'speech': ''
            }
            slides.append(current_slide)
            in_speech = False
            continue
            
        # Check for Slide Heading text
        heading_match = re.match(r'^\*\*Slide Heading:\*\*\s+\*(.*)\*', line_str)
        if heading_match:
            if current_slide:
                current_slide['heading'] = heading_match.group(1)
            continue
            
        # Check for Presenter Speech header
        if line_str.startswith("### Presenter Speech:"):
            in_speech = True
            speech_lines = []
            continue
            
        # Accumulate speech lines if in speech state
        if in_speech:
            if line_str.startswith(">"):
                # Clean up blockquote marker and quotes
                clean_line = line_str.lstrip(">").strip()
                if clean_line:
                    # Strip leading and trailing double quotes if present
                    if clean_line.startswith('"') and clean_line.endswith('"'):
                        clean_line = clean_line[1:-1]
                    speech_lines.append(clean_line)
            elif line_str == "" or line_str.startswith("---"):
                # Transition out of speech block
                if current_slide and speech_lines:
                    current_slide['speech'] = "\n\n".join(speech_lines)
                    speech_lines = []
                in_speech = False
                
    # Finalize last slide
    if current_slide and speech_lines:
        current_slide['speech'] = "\n\n".join(speech_lines)
        
    return slides

def build_latex(slides, tex_path):
    header = (
        "\\documentclass[11pt]{article}\n"
        "\\usepackage[margin=1in]{geometry}\n"
        "\\usepackage{xcolor}\n"
        "\\usepackage{array}\n"
        "\\usepackage[hidelinks]{hyperref}\n"
        "\\usepackage{titlesec}\n"
        "\\setlength{\\parindent}{0pt}\n"
        "\\setlength{\\parskip}{6pt}\n\n"
        "\\definecolor{primary}{RGB}{21, 57, 107}\n"
        "\\definecolor{secondary}{RGB}{46, 125, 50}\n"
        "\\definecolor{speechbg}{RGB}{248, 249, 250}\n\n"
        "\\titleformat{\\section}{\\large\\bfseries\\color{primary}}{\\thesection}{1em}{}\n"
        "\\titleformat{\\subsection}{\\normalsize\\bfseries\\color{secondary}}{\\thesubsection}{1em}{}\n\n"
        "\\title{\\bfseries Traffic Sign Classification using AlexNet \\\\ Presenter Script \\& Speaker Notes}\n"
        "\\author{\\textbf{Group 1:} Carlos Jerico S. Dela Torre, Joshua H. Mistal, Aidan R. Tiu}\n"
        "\\date{CMPE 362 Pattern Recognition \\\\ Polytechnic University of the Philippines \\\\ June 2026}\n\n"
        "\\begin{document}\n"
        "\\maketitle\n"
        "\\tableofcontents\n"
        "\\clearpage\n"
    )
    
    body_parts = []
    for slide in slides:
        title = escape_latex(slide['title'])
        body_parts.append(f"\\section{{{title}}}")
        
        if slide['heading']:
            heading = escape_latex(slide['heading'])
            body_parts.append(f"\\textbf{{Slide Visual Content:}} \\textit{{{heading}}}\\\\ [8pt]")
            
        if slide['speech']:
            # Break paragraphs by \newline\newline
            paragraphs = slide['speech'].split("\n\n")
            escaped_paragraphs = [escape_latex(p) for p in paragraphs]
            speech_text = "\\newline\\newline ".join(escaped_paragraphs)
            
            body_parts.append(
                "\\noindent\n"
                "\\begin{tabular}{!{\\color{primary}\\vrule width 3pt} p{0.92\\textwidth}}\n"
                f"  \\small\\color{{black!80}} {speech_text}\n"
                "\\end{tabular}\n"
                "\\vspace{15pt}\n"
            )
            
    footer = "\\end{document}\n"
    
    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(header)
        f.write("\n".join(body_parts))
        f.write(footer)
        
    print(f"LaTeX file written to {tex_path}")

def compile_pdf(tex_path, output_dir):
    # Run pdflatex twice to ensure table of contents compiles correctly
    for run in range(2):
        print(f"Running pdflatex run {run + 1}...")
        res = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", "-output-directory", output_dir, tex_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        if res.returncode != 0:
            print(res.stdout.decode('utf-8', errors='ignore'))
            raise RuntimeError(f"pdflatex failed with return code {res.returncode}")
            
    print("PDF compiled successfully!")

def main():
    md_path = "docu/presentation_script.md"
    tex_path = "docu/presentation_script.tex"
    output_dir = "docu"
    
    print("Parsing presentation_script.md...")
    slides = parse_markdown(md_path)
    print(f"Successfully parsed {len(slides)} slides.")
    
    print("Building LaTeX document...")
    build_latex(slides, tex_path)
    
    print("Compiling LaTeX to PDF...")
    compile_pdf(tex_path, output_dir)
    
    # Clean up auxiliary LaTeX files in docu directory
    exts = [".aux", ".log", ".out", ".toc"]
    for ext in exts:
        file_path = f"docu/presentation_script{ext}"
        if os.path.exists(file_path):
            os.remove(file_path)
            
    print("Cleaned up auxiliary compilation files.")
    print(f"Final presentation notes PDF: docu/presentation_script.pdf")

if __name__ == "__main__":
    main()
