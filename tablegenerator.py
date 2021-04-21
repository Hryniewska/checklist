import glob
import sys
import os
import json
from json2html import *
from pathlib import Path

def check_jsons(path):
    result = []
    for f in glob.glob(path):
        print(f)
        with open(f, "rb") as infile:
            result.append(json.load(infile))
    table = json2html.convert(json = result)

    return table

table = []
path = os.path.join('papers', "*.json")
table.append(check_jsons(path)[8:-10])

path = os.path.join('datasets', "*.json")
table.append('\n\n')
table.append(check_jsons(path)[16:-20])



print(table)
print('\n\n')

readme_file = []
with open('README.md', 'r') as readme:
    readme = readme.readlines()
    save = True
    for line in readme:
        print(line)
        if line == '<!--START_SECTION:data-section-->\n':
            save = False
            readme_file.append('<!--START_SECTION:data-section-->\n')
            for item in table:
            	readme_file.append(item)
            #print('\n\n')
            #print(table)
            #print('\n\n')
        elif line == '<!--END_SECTION:data-section-->\n':
            save = True
            readme_file.append('\n<!--END_SECTION:data-section-->\n')
        elif save == True:
            readme_file.append(line)
print('\n\n')
print(readme_file)

#with open('README.md','w') as f:
#   f.write(''.join(readme_file))

p = Path('README.md')
p.write_text(''.join(str(v) for v in readme_file))
