from itertools import starmap, zip_longest
from operator import add
from slogi import *
from azbuk import *
import numpy as np
sl=['привет',
    'спасибо',
    'хорошо',
    'да',
    'как дела',
    'россия',
    'апельсин',
    'ложка',
    'чай',
    'я',
    'животное',
    'жираф',
    'обезьяна',
    'кошка',
    'собака',
    'мышь',
    'хомяк',
    'суслик',
    'бобр',
    'кенгуру',
    'баран',
    'медведь',
    'корова',
    'заяц',
    'свинья',
    'панда',
    'шиншилла',
    'фламинго',
    'цикада',
    'друг',
    'ребёнок',
    'америка',
    'кекс',
    'отель',
    'красота',
    'музыка',
    'поэт',
    'карикатура',
    'фотограф',
    'артист',
    'кровать']

t=['konnichiwa',
   'arigato',
   'yoidesu',
   'hai',
   'ogenkidesuka',
   'roshia',
   'orenji',
   'supun',
   'ota',
   'watashi',
   'dobutsu',
   'kirin',
   'saru',
   'neko',
   'inu',
   'nezumi',
   'yamanezumi',
   'jinezumi',
   'kairi',
   'kangaru',
   'osuhitsuji',
   'kuma',
   'ushi',
   'usagi',
   'buta',
   'panda',
   'chinchira',
   'furamingo',
   'semi',
   'tomo',
   'ko',
   'amerika',
   'keki',
   'hoteru',
   'bi',
   'ongaku',
   'shijin',
   'giga',
   'kameraman',
   'geijitsuka',
   'bedo']

t_a=['hello',
     'thanks',
     'good',
     'how are you',
     'yes',
     'russia',
     'orange',
     'spoon',
     'tee',
     'i',
     'animal',
     'giraffe',
     'monkey',
     'cat',
     'dog',
     'mouse',
     'hamster',
     'gopher',
     'beaver',
     'kangaroo',
     'sheep',
     'bear',
     'kine',
     'rabbit',
     'pig',
     'panda',
     'chinchilla',
     'flamigos',
     'cicada',
     'friend',
     'child',
     'america',
     'cake',
     'hotel',
     'beauty',
     'music',
     'poet',
     'caricature',
     'cameraman',
     'artist',
     'bed']
prov=[2,2,2,2,2,1,1,1,2,2,2,2,2,2,2,2,2,2,2,1,2,2,2,2,2,1,1,1,2,2,2,1,1,1,2,2,2,2,1,2,1]
def transl(word, sl):
    ind =0
    w_p=['a']
    w=['a']
    #print(word, sl,t)
    for k in sl:
        if word==k:
            w=t[ind]
        else:
            ind=ind+1
    if w==w_p:
        return 0
    else:
        return w
az_1=['a','i','u','e','o','ka','ki','ku','ke','ko','sa','shi','su','se','so','ta','chi','tsu','te','to','na','ni','nu','ne','no','ha','hi','hu','he','ho','ma','mi','mu','me','mo','ya','yu','yo','ra','ri','ru','re','ro','wa','wi','we','wo','n','ga','gi','gu','ge','go', 'za','zi','zu','ze','zo', 'da','ji','de','do','ba','bi','bu','be','bo','pa','pi','pu','pe','po']
romaji_kat =['ア','イ','ウ','エ','オ','カ','キ','ク','ケ','コ','サ','シ','ス','セ','ソ','タ','チ','ツ','テ','ト','ナ','ニ','ヌ','ネ','ノ','ハ','ヒ','フ','ヘ','ホ','マ','ミ','ム','メ','モ','ヤ','ウ','ヨ','ラ','リ','ル','レ','ロ','ワ','ヰ','ヱ','ヲ','ン','ガ','ギ','グ','ゲ','ゴ','ザ','ジ','ズ','ゼ','ゾ','ダ','ジ','デ','ド','バ','ビ','ブ','ベ','ボ','パ','ピ','プ','ペ','ポ']
#romaji_kat =['ア','イ','ウ','エ','オ','カ','キ','ク','ケ','コ','サ','シ','ス','セ','ソ','タ','チ','ツ','テ','ト','ナ','ニ','ヌ','ネ','ノ','ハ','ヒ','フ','ヘ','ホ','マ','ミ','ム','メ','モ','ヤ','ユ','ヨ','ラ','リ','ル','レ','ロ','ワ','ヰ','ヱ','ヲ','ン','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
romaji_hir =['あ','い','う','え','お','か','き','く','け','こ','さ','し','す','せ','そ','た','ち','つ','て','と','な','に','ぬ','ね','の','は','ひ','ふ','へ','ほ','ま','み','む','め','も','や','ゆ','よ','ら','り','る','れ','ろ','わ','ゐ','ゑ','を','ん','が','ぎ','ぐ','げ','ご','ざ','じ','ず','ぜ','ぞ','だ','じ','で','ど','ば','び','ぶ','べ','ぼ','ぱ','ぴ','ぷ','ぺ','ぽ']
word = input(u'slovo:    ')
s=[]
s=transl(word, sl)
print(s)
if s==0:
    print("Такого слова нет в базе")
else:
    slogi(s,az_1,romaji_kat,romaji_hir, azb(s, t_a))
#slogi(word, az_1, romaji_kat, romaji_hir, 2)
v=0
nv=0
ind=0
prvv=[]
prnv=[]
kat=0
hir=0
print("--------------")
print("Расчёт точности")
for word in sl:
    p=[]
    p=transl(word,sl)
    #print(s)
    a=azb(p, t_a)
    slogi_p(p, az_1, romaji_kat, romaji_hir, a)
    if a==prov[ind]:
        v=v+1
        prvv.append(sl[ind])
    else:
        nv=nv+1
        prnv.append(sl[ind])
    ind=ind+1
print((v/41)*100,"%")
#print(prvv)
#print("-----------")
#print(prnv)
#for i in prov:
 #   if i==1:
#        kat=kat+1
#    else:
#        hir=hir+1
#print(kat,hir)
#123456
