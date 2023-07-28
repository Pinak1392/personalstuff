from hyphen import Hyphenator
from wordSplitter import *
import random
from collections import defaultdict

h_en = Hyphenator('en_US')
syllableParts = ['v','cv','vc','cvc','ccv','cccv','cvcc','vcc','ccvc','vcv','ccvcc','cvv','cvccc','cccvc']
vowelPhonemes = ['AA','AE','AH','AO','AW','AY','IY','EH','ER','EY','IH','OW','OY','UH','UW','Y-UH','Y-UW','Y-AH']
vowels = ['a','e','i','o','u','y','er','or','ir','ar','ur','le','ow','yr','ew']
dic = {}
consPhonDict = {'b':['B'],'c':['K','S','SH'],'ch':['CH','K'],
                'd':['D'],'f':['F'],'g':['G','JH'],
                'gn':['N'],'gh':['F'],'h':['HH'],
                'j':['JH'],'k':['K'],'l':['L'],'m':['M'],
                'n':['N'],'kn':['N'],'ng':['NG'],'p':['P'],'ps':['S'],
                'ph':['F'],'q':['K'],'r':['R'],'s':['S','ZH','SH','Z'],
                'sh':['SH'],'t':['T','SH','CH'],'th':['TH','DH'],
                'v':['V'],'w':['W','HH'],'wr':['R'],'x':['Z','K'],'z':['Z'],'ZH':['ZH']}

silencer = defaultdict(list)
silencer.update({'b':['m'],'c':['s'],'h':vowels,'k':['c'],'t':['s']})

with open('Syllables.txt') as f:
    for i in f.readlines():
        i = i.strip().split()
        try:
            dic[i[0]] = i[1:]
        except:
            pass

badWords = []
iMode = bool(int(input('inputMode: 0 or 1? ')))
with open('syllWords.txt') as f:
    lines = f.readlines()
    if iMode:
        inp = input('Input> ')
    a = ''
    for things in lines:
        if not iMode or things.split()[0] == inp.upper():
            a = things       

            parts = a.split()
            word = parts[0]
            phonemes = parts[1:]
            vcList = []
            for i in phonemes:
                i = re.sub(r'\d','',i)
                if i in vowelPhonemes:
                    vcList.append('v')
                else:
                    vcList.append('c')

            l = wordSplitter(''.join(vcList), syllableParts)
            wordSyllable = dic[word.lower()]
            options = []
            for i in l:
                if len(i.split('.')) == len(wordSyllable):
                    options.append(i)

            finalisedOpt = []
            for i in options:
                phonemeC = 0
                newi = []
                for a in i.split('.'):
                    group = []
                    for b in a:
                        group.append(phonemes[phonemeC])
                        phonemeC += 1
                    newi.append(group)
                finalisedOpt.append(newi)

            finalised = []
            for i in finalisedOpt:
                fail = False
                for a in range(len(wordSyllable)):
                    if wordSyllable[a][-1] not in vowels and wordSyllable[a][-2:] not in vowels and re.sub(r'\d','',i[a][-1]) in vowelPhonemes:
                        if iMode:
                            print('1')
                        fail = True
                        break
                    elif wordSyllable[a][-1] in vowels and wordSyllable[a][-1] != 'e' and re.sub(r'\d','',i[a][-1]) not in vowelPhonemes:
                        if iMode:
                            print('2')
                        fail = True
                        break
                    elif wordSyllable[a][0] not in vowels and re.sub(r'\d','',i[a][0]) in vowelPhonemes:
                        if len(wordSyllable[a]) < 2:
                            if iMode:
                                print('3')
                            fail = True
                            break
                        if (wordSyllable[a][min(1,len(wordSyllable[a]) - 1)] in vowels or wordSyllable[a][min(1,len(wordSyllable[a]) - 1):min(3,len(wordSyllable[a]))] in vowels) and a>0 and (wordSyllable[a][0] == wordSyllable[a-1][-1] or wordSyllable[a-1][-1] in silencer[wordSyllable[a][0]]):
                            pass
                        elif (wordSyllable[a][min(2,len(wordSyllable[a]) - 1)] in vowels or wordSyllable[a][min(2,len(wordSyllable[a]) - 1):min(4,len(wordSyllable[a]))] in vowels) and a>0 and (wordSyllable[a][0] == wordSyllable[a-1][-1] or wordSyllable[a-1][-1] in silencer[wordSyllable[a][0]]):
                            pass
                        else:
                            if iMode:
                                print('3')
                            fail = True
                            break
                    elif wordSyllable[a][0] in vowels and re.sub(r'\d','',i[a][0]) not in vowelPhonemes and wordSyllable[a][0] != 'y':
                        if iMode:
                            print('4')
                        fail = True
                        break
                    elif wordSyllable[a][0] not in vowels:
                        for keys in consPhonDict:
                            fail = True
                            if re.match(r'^' + keys,wordSyllable[a]):
                                if i[a][0] in consPhonDict[keys]:
                                    fail = False
                                    break

                        if len(wordSyllable[a]) > 1 and wordSyllable[a][1] not in vowels and fail:
                            for keys in consPhonDict:
                                fail = True
                                if re.match(r'^' + keys,wordSyllable[a][1:]):
                                    if i[a][0] in consPhonDict[keys]:
                                        fail = False
                                        break

                        if fail:
                            if iMode:
                                print('5')
                            break

                if not fail:
                    finalised.append(i)

            if len(finalised) > 0:
                if iMode:
                    print(wordSyllable, finalised)
            else:
                if iMode:
                    print(wordSyllable, finalisedOpt)
                    print(l, 'fail')
                else:
                    badWords.append(wordSyllable)

print(badWords)