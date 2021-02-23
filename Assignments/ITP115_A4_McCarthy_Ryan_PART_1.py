# Ryan McCarthy, rbmccart@usc.edu
# ITP 115, Fall 2020
# Assignment 4
# Description:
# Part 1 takes a sentence from the user and counts the number of times a letter or special character appear
# this info is returned to the user

# Part 1: this gets the sentence
sentence = input('PART 1 - Character Counter\nPlease enter a sentence:')
# this removes all of the white space so I don't have to worry about spaces when iterating and counting characters
sentence = sentence.replace(" ", "")
# changes sentence to lower so it doesn't count caps as special chars
sentence = sentence.lower()
# defines all of the characters counts
ac = "a: NONE"
bc = "b: NONE"
cc = "c: NONE"
dc = "d: NONE"
ec = "e: NONE"
fc = "f: NONE"
gc = "g: NONE"
hc = "h: NONE"
ic = "i: NONE"
jc = "j: NONE"
kc = "k: NONE"
lc = "l: NONE"
mc = "m: NONE"
nc = "n: NONE"
oc = "o: NONE"
pc = "p: NONE"
qc = "q: NONE"
rc = "r: NONE"
sc = "s: NONE"
tc = "t: NONE"
uc = "u: NONE"
vc = "v: NONE"
wc = "w: NONE"
xc = "x: NONE"
yc = "y: NONE"
zc = "z: NONE"
special_c = "Special Characters: NONE"

# for each loop to add an asterisk to the count if the letter is found
for character in sentence:
    char = character
    if char == "a":
        ac = ac.replace("NONE", "")
        ac += "*"
    elif char == "b":
        bc = bc.replace("NONE", "")
        bc += "*"
    elif char == "c":
        cc = cc.replace("NONE", "")
        cc += "*"
    elif char == "d":
        dc = dc.replace("NONE", "")
        dc += "*"
    elif char == "e":
        ec = ec.replace("NONE", "")
        ec += "*"
    elif char == "f":
        fc = fc.replace("NONE", "")
        fc += "*"
    elif char == "g":
        gc = gc.replace("NONE", "")
        gc += "*"
    elif char == "h":
        hc = hc.replace("NONE", "")
        hc += "*"
    elif char == "i":
        ic = ic.replace("NONE", "")
        ic += "*"
    elif char == "j":
        jc = jc.replace("NONE", "")
        jc += "*"
    elif char == "k":
        kc = kc.replace("NONE", "")
        kc += "*"
    elif char == "l":
        lc = lc.replace("NONE", "")
        lc += "*"
    elif char == "m":
        mc = mc.replace("NONE", "")
        mc += "*"
    elif char == "n":
        nc = nc.replace("NONE", "")
        nc += "*"
    elif char == "o":
        oc = oc.replace("NONE", "")
        oc += "*"
    elif char == "p":
        pc = pc.replace("NONE", "")
        pc += "*"
    elif char == "q":
        qc = qc.replace("NONE", "")
        qc += "*"
    elif char == "r":
        rc = rc.replace("NONE", "")
        rc += "*"
    elif char == "s":
        sc = sc.replace("NONE", "")
        sc += "*"
    elif char == "t":
        tc = tc.replace("NONE", "")
        tc += "*"
    elif char == "u":
        uc = uc.replace("NONE", "")
        uc += "*"
    elif char == "v":
        vc = vc.replace("NONE", "")
        vc += "*"
    elif char == "w":
        wc = wc.replace("NONE", "")
        wc += "*"
    elif char == "x":
        xc = xc.replace("NONE", "")
        xc += "*"
    elif char == "y":
        yc = yc.replace("NONE", "")
        yc += "*"
    elif char == "z":
        zc = zc.replace("NONE", "")
        zc += "*"
    else:
        special_c = special_c.replace("NONE", "")
        special_c += "*"

print("Here is the character distribution:\n\n " + ac, "\n", bc, "\n", cc, "\n", dc, "\n", ec, "\n", fc, "\n", gc, "\n",
      hc, "\n", ic, "\n", jc, "\n", kc, "\n", lc, "\n", mc, "\n", nc, "\n", oc, "\n", pc, "\n", qc, "\n", rc, "\n",
      sc, "\n", tc, "\n", uc, "\n", vc, "\n", wc, "\n", xc, "\n", yc, "\n", zc, "\n", special_c)
