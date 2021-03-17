import os
import argparse


class File():
    def __init__(self, name, size):
        self.name = name
        self.size = size


    def get_file(self):
        return {"name": self.name, "size": self.size}

def factor(x):

    _ = {
        0: 'B',
        1: 'K',
        2: 'M',
        3: 'G',
        4: 'T'
    }

    return _[x]


def f_size(size, n = 0):
    if size >= 1024:
        size /= 1024
        n += 1
        return f_size(int(size), n)
    else:
        return f'{size}{factor(n)}'


def scan_dir(base_dir):
    files = []
    try:
        if os.listdir(base_dir):
            for file in os.listdir(base_dir):
                filepath = os.path.join(base_dir, file)
                if os.path.isfile(filepath):
                    size = f_size(os.stat(filepath).st_size)
                    files.append(File(filepath, size))
        
        return files
                                     
    except:
        return []


if __name__ == '_main_':
    parser = argparse.ArgumentParser(description='script that lists files under given directory')
    
    parser.add_argument('--dir', help='directory to be read')
    
    args = parser.parse_args()
    if args.dir:
        scan_dir(base_dir=args.dir)