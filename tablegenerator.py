import glob
import sys
import os
import json
import pandas as pd
from pathlib import Path

def check_jsons(path):
    result = []
    for f in glob.glob(path):
        print(f)
        with open(f, "rb") as infile:
            result.append(json.load(infile))
    print(result[0])
    table = pd.DataFrame(result[0])
    return table.to_html()

table = []
path = os.path.join('papers', "*.json")
table.append(check_jsons(path))

path = os.path.join('datasets', "*.json")
table.append('\n\n')
table.append(check_jsons(path))



readme_file = []
with open('README.md', 'r') as readme:
    readme = readme.readlines()
    save = True
    for line in readme:
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
print('\n')

#with open('README.md','w') as f:
#   f.write(''.join(readme_file))

p = Path('README.md')
p.write_text(''.join(str(v) for v in readme_file))
