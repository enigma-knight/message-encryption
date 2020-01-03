import re

vers = '1.1.2'

groups = 7 # change this to change the grouping of letters in the encrypted version of the message.

alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

f = lambda n: f(n - 1) + n if n > 1 else 1 # this is how it determines which letter to use; mathematically, anyway.
s = lambda x, p: (f(p) * (-1) ** (x)) # this helps make even indexed letters work differently than odd ones.
ltr = lambda l: alph.find(l) # simply finds the index of the letter.
enc = lambda l, p: alph[int((ltr(l) + s(ltr(l), p)) % 26)] # actually encodes a single letter, based on index.

def tidy_msg(m):
    # cleans the message, to replace spaces with qs/sq, gets rid of all symbols except periods/exclam. points (qp/pq), question marks (qq).
    # a fix for numbers being deleted will be coming soon.
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


def sep(s, no):
    # takes a number no and seperates it in groups of s length.
    # this function comes courtesy of Coding Panda on SoloLearn. I only made slight alterations.
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
    # this actually takes the groups of seven and encodes each letter.
    m = tidy_msg(m)
    m = sep(m, groups)
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


def docs():
    print("""encryption.py v{}
    Thank you for using encryption.py. These docs are a brief breakdown of them
    encryption method and how to use it.

    A normal Caesar substitution cypher takes a letter and offsets it by n letters.
    A small example chart: n by letter
        0 1 2 3 4 5
        A B C D E F
        B C D E F G
        C D E F G H
        D E F G H I
    This cypher takes the message into groups of s, then takes each letter and
    replaces it with another based on a function f of its position p in that group.
    It removes all non-letter symbols sans [? and (! and .)], replacing those with qq and
    qp respectively.

    The default group size in the algorithm is 7, and that was the originally
    intended value. No real testing of other values greater than 7 have been done,
    so be aware of the possibility of unwieldy or difficult to decrypt outputs.
    The group size is defined as `encryption.groups`.

    To encrypt a message, use `encryption.encode(message)`.""".format(vers))


if __name__ == "__main__":
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

    print(encode(msg))

    print("\n\n")

    pangram = 'Pack my box with five dozen liquor jugs.' # has every letter in the English alphabet in it.
    print(encode(pangram))
else:
    welcome_message = """Thank you for using Enigma Knight's encryption module.
https://github.com/enigma-knight/

To read docs in console, use the command encryption.docs()."""

    print(welcome_message)
