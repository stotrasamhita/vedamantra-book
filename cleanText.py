#!/usr/bin/python3
import sys
import indic_transliteration.sanscript as sanscript
import re

def replaceText():
    repl_list = [# ('र्द्ध्', 'र्ध्'), ('र्द्ध', 'र्ध'),
                 ('त्स्', 'थ्स्'), ('प्स्', 'फ्स्'),
                 ('त्स', 'थ्स'), ('प्स', 'फ्स'),
                 ('', '᳚'),
                 ('॑', 'ः॑'), ('॒', 'ः॒'), ('᳚', 'ः᳚'),
                 ('', 'ꣳ'), ('', 'ꣳ॑'), ('', 'ꣳ᳚'), ('', 'ꣳ॒'),
                 ('', 'ꣴ'), ('', 'ꣴ॒'), ('', 'ꣴ॑'), ('', 'ꣴ᳚')]
    for file in sys.argv[1:]:
        sys.stderr.write('Updating %s\n' % (file))
        with open(file, 'r') as in_f:
            file_lines = in_f.readlines()

        noReplaces = True
        for old, new in repl_list:
            for i in range(len(file_lines)):
                file_lines_new = file_lines[i].replace(old, new)
                if file_lines_new != file_lines[i]:
                    file_lines[i] = file_lines_new
                    noReplaces = False

        if not noReplaces:
            with open(file, 'w') as out_f:
                out_f.writelines(file_lines)


def main():
    for file in sys.argv[1:]:
        # sys.stderr.write('Updating %s\n' % (file))
        with open(file, 'r') as in_f:
            file_lines = in_f.readlines()

            for i, line in enumerate(file_lines):
                for word in line.split(' '):
                    trans_word = sanscript.transliterate(word, 'devanagari', 'itrans')
                    if trans_word == word:
                        continue
                    trans_word_rep = re.sub('([kgcjtdpb])s', '\\1hs', trans_word)
                    if trans_word_rep != trans_word:
                        print('%40s:%05d:: %s' % (file, i, trans_word))


if __name__ == '__main__':
    main()
