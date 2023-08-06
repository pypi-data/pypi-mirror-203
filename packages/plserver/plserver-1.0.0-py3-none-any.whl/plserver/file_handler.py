# Updated source checks
import os
import re

# Current Working Directory.
w_dir = os.getcwd()

# Get Content of a File.
def file_content(path) -> bytes:
    source  = w_dir + path
    try:
        f = open(source, "rb")
    except FileNotFoundError:
        return b''
    else:
        return f.read(9000000)

# Html Tags atrribute values Search.
def get_atribute_values(html, attribute_name) -> list:
    regex_string = f'{attribute_name}="([^"]*)"'
    regex = re.compile(rf'{regex_string}', re.IGNORECASE | re.MULTILINE)
    values = re.findall(regex, html)
    return values

# Links inside an Html Tag after search.
def get_links(html, tag, attribute) -> list:
    values = []
    #if tag = ""
    tag_regex = f'<{tag}[^>]+>.*?<\/{tag}>'
    regex = re.compile(rf'{tag_regex}', re.IGNORECASE | re.MULTILINE)
    tags = re.findall(regex, html)
    for i in tags:
        attribute_values = get_atribute_values(i, attribute)
        if len(attribute_values) > 0:
            values.append(attribute_values[0])
    return values

# Main File path Extrsctor.
def file_extractor(path):
    files_path = []
    p_Content = file_content(path).decode("utf-8")
    css = get_atribute_values(p_Content, "href")
    js = get_links(p_Content, "script", "src")
    for i in css:
        if ".css" in i:
            files_path.append('/' + i)
    
    for i in js:
        if ".js" in i:
            files_path.append('/' + i)
    files_path.append(path)
    return files_path

# Get the sizes of each files in source.
def initial_sizes1(files) -> dict:
    sizes = {}
    for i in files:
        sizes[i] = len(file_content(i))
    return sizes

# Check for any changes in all the source files.
def file_size_checker(path, size):
    p_c = file_content(path)
    #print(path)
    #print(len(p_c), size)
    if len(p_c) == size:
        return 0
    else:
        return 1

# Updated FIles handler.
def source_file_Handler(initial_sizes, file_ex):
    #print(file_ex)
    state = 0
    for i in file_ex:
        if state == 0:
            if file_size_checker(i, initial_sizes[i]) == 1:
                state = 1
            else:
                state = 0
        else:
            pass
    #print(state)
    return state