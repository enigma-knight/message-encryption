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
alph2 = 'ÆBÇĐËFĢHÎJĶŁMŃØPQŔ§ÞŮVWXÝŻ'  # this was to test it to see if you could switch it over to another group of letters, to make the output more mysterious lol

f = lambda n: f(n-1)+n if n>1 else 1  # this is how I determined how the letter would be replaced, so the first letter in a group of 7 would go up or down 1, second would go up or down 3, then 6, 10, 15, etc.
s = lambda x,p: (f(p)*(-1)**(x))  # this actually says whether it should go up or down, depending on if it is an evenly indexed or oddly indexed letter.
ltr = lambda l: alph.find (l)  # finds the index of the letter, to use in s function.
enc = lambda l,p: alph[int((ltr(l) + s(ltr(l),p))%26)]  # to replace the letter with the appropriate letter.

''' all of the above was really rather easy, though maybe not very intuitive.
The next part, about separating the message into groups of 7, and then encoding
them each properly was the real challenge. '''

def letter_distr (m):
    ''' just finds the percentage of letters used in a message.
    this is used for analising the message afterwards. '''
    letters=[]
    alph='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    msg=re.sub("[^a-zA-Z]+", "", m).upper()  # gets rid of non letter symbols, so when you count the size of the messaage, they don't have an affect.
    msg = ''.join(msg.split())
    for l in alph:
        letters.append("{0:.4f}%".format(100*msg.count(l)/len(msg)))
    return letters

def tidy_msg (m):
    ''' cleans up the message, and replaces certain symbols with letters. '''
    qq='QQ'
    period=['QP','PQ']
    space=['QS','SQ']
    m=m.replace ('.',period[m.find('.')%2])  # replaces periods with qp or pq.
    m=m.replace ('!',period[m.find('!')%2])  # replaces exclamation points with qp or pq, like a period.
    m=re.sub("[^a-zA-Z]+", " ", m)  # gets rid of all non letter symbols.
    m=m.replace (' ',space[m.find(' ')%2])  # removes spaces.
    m=m.replace ('?',qq)  # replaces question marks with qq.
    m=m.upper()
    return m


def sep(s, no):
    c = 0
    n = ''
    for i in s:
        if i == ' ':
            continue

        if c == no - 1:
            n += i + ' '
            c = 0

        else:
            n += i
            c += 1
    return n

def encode(m):
    ''' actually encodes the entire message.
    This particular encryption method is based around 7, although
    a higher number would be more secure, I haven't gone into how
    it would really affect it. '''
    m = tidy_msg(m)
    m = sep(m, 7)  # you could change this to any other positive integer to experiment.
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
for letter in alph:
    print(letter, encode(letter * 7))

for i in range(len(letter_distr(encode(msg)))):
    ''' this is to show the original distribution of letters,
    then the distribution after encoding. '''
    print(alph[i], letter_distr(msg)[i], end = ' || ')
    print(letter_distr(encode(msg))[i])