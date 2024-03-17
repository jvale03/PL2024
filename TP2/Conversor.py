import sys
import re

def markdown_to_html(md_text):
    # Substituir títulos
    md_text = re.sub(r'### (.+)', r'<h3>\1</h3>', md_text)
    md_text = re.sub(r'## (.+)', r'<h2>\1</h2>', md_text)
    md_text = re.sub(r'# (.+)', r'<h1>\1</h1>', md_text)
    
    # Substituir negrito
    md_text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', md_text)
    
    # Substituir itálico
    md_text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', md_text)

    # Substituir imagems
    md_text = re.sub(r'\!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1">', md_text)
    
    # substituir links
    md_text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href=\2>\1</a>', md_text)



    # Substituir paragrados
    md_text = re.sub(r'\n\n', r'\n</p>\n<p>\n', md_text)
    md_text = '<p>' + md_text + '</p>'

    # Substituir listas numeradas
    text_list = []
    list_number = 0
    for line in md_text.split("\n"):
        text = re.match(r"(\d+)\. (.+)",line)
        if text:
            if list_number == 0:
                text_list.append(f"<ol>\n    <li>{text.group(2)}</li>") 
            else: 
                text_list.append(f"    <li>{text.group(2)}</li>")
            list_number += 1
        
        elif list_number != 0:
            text_list.append(f"</ol>")
            text_list.append(line)
            list_number = 0
        
        else: 
            text_list.append(line)
        
    # Substituir listas nao numeradas
    md_text = "\n".join(text_list)
    text_list = []
    list_number = 0
    for line in md_text.splitlines():
        text = re.match(r"(\-) (.+)",line)
        if text:
            if list_number == 0:
                text_list.append(f"<ul>\n    <li>{text.group(2)}</li>") 
            else: 
                text_list.append(f"    <li>{text.group(2)}</li>")
            list_number += 1
        
        elif list_number != 0:
            text_list.append(f"</ul>")
            text_list.append(line)
            list_number = 0
        
        else: 
            text_list.append(line)

    return "\n".join(text_list)

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

