#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
import re

syllable = "(?:[अ-औॐ\uA8F3\uA8F4]|(?:[क-ह](?:\u094D|\u094D\u200D|\u200D\u094D))*[क-ह][\u093E-\u094D]?)\u0901?"
anudatta = "\u0952"
anusvaraVisarga = "\u0902?\u0903?"

import shutil
# shutil.copy2('TaittiriyaSamhita-Kandas.tex', 'TaittiriyaSamhita-Kandas.tex.old') # complete target filename given

REPL_TABLE = [
# ('॒स्स्', 'ः॒ स्'),# ('॒श्श्', 'ः॒ श्'),
# ('॑स्स्', 'ः॑ स्'),# ('॑श्श्', 'ः॑ श्'),
# ('स्स्', 'ः स्'), #('श्श्', 'ः श्'), 
('ख्ष्', 'क्ष्'),
]

MAATRAS = ['', 'ा', 'ि', 'ी', 'ु', 'ू', 'ृ', 'ॄ', 'ॅ', 'ॆ', 'े', 'ै', 'ॉ', 'ॊ', 'ो', 'ौ', '्', 'ॎ', 'ॏ']


with open('TaittiriyaSamhita-Kandas.tex', 'w', errors='replace') as outfile:
    with open('TaittiriyaSamhita-Kandas.orig.tex', 'r', errors='replace') as infile:
        for line in infile.readlines():
            z = line.strip('\n')
            z = z.replace('', '᳚')
            for maatra in MAATRAS:
                # for consonant in ['य', '॑व']:
                #     for swara in ['॑', '_', ]:
                #         z = z.replace('%s%s्%s%sँ' % (swara, consonant, consonant, maatra),
                #                       'ं%s %s%s' % (swara, consonant, maatra))
                        z = z.replace('॒व्व' + maatra + 'ँ', 'ं॒ व' + maatra)
                        z = z.replace('॑व्व' + maatra + 'ँ', 'ं॑ व' + maatra)
                        z = z.replace('व्व' + maatra + 'ँ', 'ं व' + maatra)
                        z = z.replace('॒य्य' + maatra + 'ँ', 'ं॒ य' + maatra)
                        z = z.replace('॑य्य' + maatra + 'ँ', 'ं॑ य' + maatra)
                        z = z.replace('य्य' + maatra + 'ँ', 'ं य' + maatra)
                        z = z.replace('॒स्स' + maatra, 'ः॒ स' + maatra)
                        z = z.replace('᳚स्स' + maatra, 'ः᳚ स' + maatra)
                        z = z.replace('॑स्स' + maatra, 'ः॑ स' + maatra)
                        z = z.replace('स्स' + maatra, 'ः स' + maatra)
            
            # for swara in ['॑', '_', '᳚', '']:
            #     z = z.replace(swara + 'न्दे॒व', 'ं' + swara + 'दे॒व')

            for chunk, repl in REPL_TABLE:
                z = z.replace(chunk, repl)
                # z = z.replace( '॑', 'ः॑',)
                # z = z.replace( '॒', 'ः॒',)
                # z = re.sub(f"({syllable}){anudatta}({anusvaraVisarga})", "\\\\ul{\\1\\2}\\\\nolinebreak[4]", line.strip('\n'))
                # z = re.sub(f"({syllable})({anusvaraVisarga}){anudatta}", "\\\\ul{\\1\\2}\\\\nolinebreak[4]", z)
            print(z, file=outfile)