#######################
# @author: RaffaDNDM
# @date:   2022-11-27
#######################

import yara
import os
from pathlib import Path

RULES_DIR = "yara"
filepaths = {}
extensions = ('**/*.yar', '**/*.yara')

input_file=input("Path of the file to be analysed:\n")

for path in Path(RULES_DIR).rglob('*.yar'):
    filepaths[os.path.splitext(path)[0]] = str(path)

rules = yara.compile(filepaths=filepaths)

#Print registered yara rules
#for r in rules:
#    print(r.identifier)

matches = rules.match(input_file)

for m in matches:
    print(m)
    print(m.tags)