# combine english, esperanto, spanish and french gismu lists into one
# html document for easy comparing
# run this in the vocab.es directory of cvs tree

import os
from string import strip
cwd = os.getcwd()
english = ('vocab.eo', 'gismu.en')
esperanto = ('vocab.eo', 'gismu.eo')
spanish = ('vocab.es', 'gismu_spanish.txt')
french = ('vocab.fr', 'gismu')

parent = os.path.split(cwd)[0]
##print cwd
##print os.path.join(parent, spanish)
##print os.path.join(parent, french)

en = open(apply(os.path.join, (parent,) + english))
es = open(apply(os.path.join, (parent,) + spanish))
eo = open(apply(os.path.join, (parent,) + esperanto))
fr = open(apply(os.path.join, (parent,) + french))

output = ['<html><head><title>le gi\'uste pe bau so\'ida</title></head><body>',
          '<p>']

# cycle through the first few lines before the first gismu
# first three lines of the spanish list
for i in range(3):
    output.append(es.readline() + '<br>')

# first line of the esperanto and french and english
output.append(eo.readline() + '<br>')
output.append(fr.readline() + '<br>')
output.append(en.readline() + '<br>')
output.append('<dl>')

def split_spanish(s):
    args = (strip(s[:5]), strip(s[6:20]), (s[20:36]), (s[36:]))
    return '<dt><b>%s</b> [ %s ] %s <dd> %s' % args

def split_logflash(s):
    args = (strip(s[:5]), strip(s[6:19]), strip(s[19:61]),
            strip(s[61:158]), strip(s[168:]))
    return '<dt><b>%s</b> [ %s ] %s <dd> %s <br> %s' % args

# now cycle through the lists
while 1:
    # english
    line = en.readline()
    if not strip(line):
        break
    print line[:5]
    output.append(split_logflash(line))
    # esperanto
    output.append(split_logflash(eo.readline()))
    # spanish
    output.append(split_spanish(es.readline()))
    # french
    output.append(split_logflash(fr.readline()))

    # add a horizontal rule
    output.append('</dl><hr><dl>')

output.append('</body></html>')

out = open(os.path.join(parent, esperanto[0], 'combined.html'), 'w')
out.writelines(output)
out.close()

##raw_input()
