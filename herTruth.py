hyps = [ 'p <= (q or r)','(not q) <= s', '(s and p) <= (not r)']

concl = 'q'

fst = "{0:^3s}|{1:^3s}|{2:^3s}|{3:^3s}|{4:^8s}|{5:^7s}|{6:^9s}|{7:^3s}"

fst2 = "{0:^3d}|{1:^3d}|{2:^3d}|{3:^3d}|{4:^8d}|{5:^7d}|{6:^9d}|{7:^3d}"

div = "---+---+---+---+--------+-------+---------+---"

print(fst.format('p','q','r','s','p->q|r','~q->s','s&p->~r','q'))
for p in range(2):
    for q in range(2):
        for r in range(2):
            for s in range(2):
                print(div)
                print (fst2.format(p,q,r,s, eval(hyps[0]), \
                    eval(hyps[1]), eval(hyps[2]),eval(concl)))
