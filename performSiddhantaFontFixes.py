#!/usr/bin/python3
import sys
import indic_transliteration.sanscript as sanscript
import re

# repl_list = [('ष्ट्य', 'ष्ट'), ('ष्ठ्य', 'ष्ठ')]
repl_list = [('ष्ट्य', 'ट्य'), ('ष्ठ्य', 'ठ्य')]
for file in sys.argv[1:]:
    sys.stderr.write('Updating %s\n' % (file))
    with open(file, 'r') as in_f:
        file_lines = in_f.readlines()

    noReplaces = True
    for old, new in repl_list:
        print(old, '->', new)
        for i in range(len(file_lines)):
            file_lines_new = file_lines[i].replace(old, new)
            if file_lines_new != file_lines[i]:
                file_lines[i] = file_lines_new
                noReplaces = False

    if not noReplaces:
        with open(file, 'w') as out_f:
            out_f.writelines(file_lines)
