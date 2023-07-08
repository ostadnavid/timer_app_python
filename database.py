import os

def write_to_file(fpath, content, index=-99, mode='w'):
    if index == -99:
        with open(fpath, mode=mode) as f:
            f.write(content)
    else:
        with open(fpath, mode='r') as f:
            lines = f.readlines()
        
        lines[index] = content
        
        with open(fpath, mode='w') as f:
            f.writelines(lines)

def read_from_file(fpath, get_lines=False):
    with open(fpath, 'r') as f:
        if get_lines:
            content = f.readlines()
        else:
            content = f.read()
    
    return content

def check_file(fpath):
    return os.path.exists(fpath)
