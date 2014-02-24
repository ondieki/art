import urllib2
from bs4 import BeautifulSoup
import re
from collections import defaultdict
from HMTLParser import HMTLParser

words = {"Mona Lisa":0, "Mona":0, "Monalisa":0, "mona lisa":0}

pos = {"beauty":0, "mysterious":0, "stylistic":0, "reputation":0, "charm":0, "charming":0, "background:":0, 
"symmetry":0, "beautiful":0, "awesome":0, "Da Vinci":0,"great":0, "beauty":0, "smile:":0, 
"enigmatic":0, "unique":0, "rock star":0,"intrigue":0, "why":0, "what":0, "popular":0, 
"valuable":0, "legendary":0, "secrets":0, "secret":0, "compelling":0, "stunning":0, "intense":0, "feminine":0,
"greatest":0, "beloved":0, "sexual":0, "maternal":0, "seductive":0, "consoling":0, "pleasure":0, "joy":0, "ambiguous":0, 
"undefined":0
}

neg = {"stolen":0, "theft":0, "overrated":0}

for line in open('1.txt'):
  words =line.split(' ')
  for token in words:
    token = token.lower()
    if token in pos:
      pos[token] += 1
    elif token in neg:
      neg[token] += 1

print pos
print "==============NEGATIVE TERMS=============="
print neg