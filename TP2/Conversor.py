import re
import sys

def markdown_to_html(md_text):
    # Substituir títulos
    md_text = re.sub(r'### (.+)', r'<h3>\1</h3>', md_text)
    md_text = re.sub(r'## (.+)', r'<h2>\1</h2>', md_text)
    md_text = re.sub(r'# (.+)', r'<h1>\1</h1>', md_text)
    
    # Substituir negrito
    md_text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', md_text)
    
    # Substituir itálico
    md_text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', md_text)
    
    # Substituir listas
    md_text = re.sub(r'\n- (.+)', r'\n<ol>\n<li>\1</li>\n</ol>', md_text)

    # Substituir imagems
    md_text = re.sub(r'\!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1">', md_text)
    
    # Substituir links
    md_text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href=\2>\1</a>', md_text)

    # Substituir paragrados
    md_text = re.sub(r'\n\n', r'\n</p>\n<p>', md_text)
    md_text = '<p>' + md_text + '</p>'
    
    return md_text

def read_md_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        md_text = file.read()
    return md_text

def write_html_file(html_text, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(html_text)
if __name__ == "__main__":

    md_text = read_md_file(sys.argv[1])

    html_text = markdown_to_html(md_text)

    write_html_file(html_text, 'output.html')

