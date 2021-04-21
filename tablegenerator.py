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
    print(result)
    table = pd.DataFrame(val for sublist in result for val in sublist)#.transpose()
    return table.to_html()

table = []

table.append('## Summary showing which points from the checklist are fulfilled by studies.\n')
path = os.path.join('papers_checklist', "*.json")
table.append(check_jsons(path))

table.append('\n\n## Summary showing which points from the checklist are fulfilled by data resources.')
path = os.path.join('datasets_checklist', "*.json")
table.append('\n')
table.append(check_jsons(path))

table.append('\n\n## This table presents the data sources. The JPEG quality factor (QF) for most images has been set to 75, other cases are indicated.')
path = os.path.join('datasets_information', "*.json")
table.append('\n')
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
