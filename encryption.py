import re

msg = '''I met a traveller from an antique land,
Who said—“Two vast and trunkless legs of stone
Stand in the desert. . . . Near them, on the sand,
Half sunk a shattered visage lies, whose frown,
And wrinkled lip, and sneer of cold command,
Tell that its sculptor well those passions read
Which yet survive, stamped on these lifeless things,
The hand that mocked them, and the heart that fed;
And on the pedestal, these words appear:
My name is Ozymandias, King of Kings;
Look on my Works, ye Mighty, and despair!
Nothing beside remains. Round the decay
Of that colossal Wreck, boundless and bare
The lone and level sands stretch far away.”'''

alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

f = lambda n: f(n - 1) + n if n > 1 else 1
s = lambda x, p: (f(p) * (-1) ** (x))
ltr = lambda l: alph.find(l)
enc = lambda l, p: alph[int((ltr(l) + s(ltr(l), p)) % 26)]

def tidy_msg(m):
    qq = 'QQ'
    period = ['QP', 'PQ']
    space = ['QS', 'SQ']
    m = m.replace('.', period[m.find('.') % 2])
    m = m.replace('!', period[m.find('!') % 2])
    m = re.sub("[^a-zA-Z]+", " ", m)
    m = m.replace(' ', space[m.find(' ') % 2])
    m = m.replace('?', qq)
    m = m.upper()
    return m


def sep(s, no):  # this function courtesy of Coding Panda on SoloLearn. I only made slight alterations.
    c = 0
    n = ""
    for i in s:
        if i == " ":
            continue
        if c == no - 1:
            n += i + " "
            c = 0
        else:
            n += i
            c = c + 1
    return n


def encode(m):
    m = tidy_msg(m)
    m = sep(m, 7)
    m = m.split()
    msg = []
    for block in m:
        ltrs = []
        for p in range(len(block)):
            l = block[p]
            ltrs.append(enc(l, p + 1))
        msg.append(''.join(ltrs))
    msg = ' '.join(msg)
    return msg


print(encode(msg))

print('\n{----\n')

mm = 'the quick brown fox jumps over the three lazy dogs.'
