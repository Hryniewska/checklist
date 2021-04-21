import glob
import sys
import os
import json
from json2html import *
from pathlib import Path

argumentList = sys.argv[1:]

print(argumentList[0][7:])

path = os.path.join(argumentList[0][7:], "*.json")

result = []
for f in glob.glob(path):
    print(f)
    with open(f, "rb") as infile:
        result.append(json.load(infile))

table = json2html.convert(json = result)
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
            readme_file.append(table[8:-10])
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

#with open('f1.md','w') as f:
#  f.write(''.join(readme_file))

p = Path('README.md')
p.write_text(''.join(readme_file))
