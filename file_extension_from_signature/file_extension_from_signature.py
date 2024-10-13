#######################
# @author: RaffaDNDM
# @date:   2023-01-17
#######################

import json
import sys
import os
from termcolor import colored, cprint

SPECIFICATION_PATH = "file_signatures.json"

def format_evaluation(filename):
    global SPECIFICATION_PATH
    dict_signatures = {}
    content = ''

    with open('file_signatures.json') as dict_f:
        dict_signatures = json.load(dict_f)

    with open(filename, 'rb') as f:
        content = str(f.read().hex())

    list_formats = []
    
    for k in dict_signatures:
        signs = dict_signatures[k]['signs']
        
        for s in signs:
            byte_offset = int(s.split(',')[0])
            signature = s.split(',')[1]

            if len(content) >= (byte_offset*2+len(signature)):
                if content[byte_offset*2:].startswith(signature):
                    list_formats.append(dict_signatures[k]['mime'])

    return list_formats


def main():
    if os.path.exists(sys.argv[1]):
        filename = sys.argv[1]
        list_formats = format_evaluation(sys.argv[1])

        print(f"\nFile: {colored(os.path.basename(sys.argv[1]), 'red')}", end='\n\n')
        cprint('       Possible applications', 'blue')
        cprint('___________________________________', 'blue')
        
        i=1
        for f in list_formats:
            print(colored('{:2}> '.format(i), 'green'), f)
            i+=1

        cprint('___________________________________', 'blue', end='\n\n')
    
    else:
        print("[ERROR] File doesn't exist")

if __name__=="__main__":
    main()