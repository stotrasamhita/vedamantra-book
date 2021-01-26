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
('ख्ष', 'क्ष'),
('ंदृ', 'न्दृ'),
('क्स', 'ख्स'),
]

MAATRAS = ['', 'ा', 'ि', 'ी', 'ु', 'ू', 'ृ', 'ॄ', 'ॅ', 'ॆ', 'े', 'ै', 'ॉ', 'ॊ', 'ो', 'ौ', '्', 'ॎ', 'ॏ']


with open('TaittiriyaSamhita-Kandas.tex', 'w', errors='replace') as outfile:
    with open('TaittiriyaSamhita-Kandas.R0.tex', 'r', errors='replace') as infile:
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
                        z = z.replace('॒श्श' + maatra, 'ः॒ श' + maatra)
                        z = z.replace('᳚श्श' + maatra, 'ः᳚ श' + maatra)
                        z = z.replace('॑श्श' + maatra, 'ः॑ श' + maatra)
                        z = z.replace('श्श' + maatra, 'ः श' + maatra)
            
            for swara in ['॑', '_', '᳚', '']:
                z = z.replace(swara + 'न्दे॒व', 'ं' + swara + ' दे॒व')

            # for text in ['न्दैव्य', 'न्दृꣳ', 'न्दृ॒ꣳ॒', 'न्धत्त', 'ञ्ज्यो', 'म्प्रो', 'म्प॒वि', 'म्प्रति', 'ङ्ग्र॑थ्ना',
            #  'म्पू॒षा', 'न्धूर्व', 'न्धू᳚र्व', 'ञ्जे᳚ष्म', 'ञ्जहि', 'न्तप॑सा', 'म्मख', 'ङ्गृह्ण', 'ञ्जनम्', 'ञ्जनय', 'ञ्जन॑य']:
            for text in ['म्मा ', 'म्मे॑ ','म्मे ', 'ङ्गच्छ', 'ङ्ग॑च्छ', 'म्ब्रह्म', 'म्प्राण', 'म्प्रा॒ण', 'म्प्र॒जा', 'म्प॒शू', 'म्पा॒हि', 'म्पञ्च', 'ञ्जुष्ट', 'ङ्घृत','ङ्घृ॒त', 'म्प॑र्य', 'म्प॑र']:

                for swara in ['॑', '_', '᳚', '']:
                    z = z.replace(swara + text, 'ं' + swara + ' ' + text[2:])
                

            z = z.replace('॒ं', 'ं॒')
            z = z.replace('॑ं', 'ं॑')
            z = z.replace('ाम्᳚','ा᳚म्')
            z = z.replace('ीम्᳚','ी᳚म्')

            for chunk, repl in REPL_TABLE:
                z = z.replace(chunk, repl)
                # z = z.replace( '॑', 'ः॑',)
                # z = z.replace( '॒', 'ः॒',)
                # z = re.sub(f"({syllable}){anudatta}({anusvaraVisarga})", "\\\\ul{\\1\\2}\\\\nolinebreak[4]", line.strip('\n'))
                # z = re.sub(f"({syllable})({anusvaraVisarga}){anudatta}", "\\\\ul{\\1\\2}\\\\nolinebreak[4]", z)
            print(z, file=outfile)
