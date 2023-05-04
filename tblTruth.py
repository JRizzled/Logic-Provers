#!/bin/python3
def bn_cycle(ab):
    ac = 2 ** ab
    aa = [bin(i)[2:] for i in range(ac)]
    for n, i in enumerate(aa):
        aa[n] = ((ab - len(i)) * '0') + i
    ad = []
    for j in aa:
        ad.append([int(k) for k in j])
    return ad

def truth_tbl(exprs, num_vars):
    
    combs = bn_cycle(num_vars)
    print("| ",end='')
    for i in exprs:
        print(i + " |", end="")
    print()
    for i in combs:
        ## Each binary combination is tested and each parameter is assigned to a value
        for k in range(num_vars):
            locals()[exprs[k]] = i[k]
        print("| ",end='')
        for j in exprs:
            print(str(int(eval(j))) + " "*(len(j) - 1) + " |",end='')
            ## Evaluates each exprs for the parameters of each combination
        if all(list(map(eval, exprs[num_vars:-1]))):
            ## Tests the conditions (not including the parameters) to see if all are true, then tests the conclusion and if it isnt True it returns Invalid. 
            if eval(exprs[-1]):
                print("Valid Argument", end='')
            else:
                print("Invalid Argument", end='')
        print()
        
if __name__ == "__main__":
    d = input("DEBUG? y/n")
    if d.lower() == 'y':
        exprs_par = ["p","q","r","s", "t", "u", "v", "w", "p <= q","r or s", "(not s) <= (not t)", "(not q) or s", "not s", "((not p) and r) <= u", "w or t", "u and w"]
        num_vars_par = 8
        
    else:
        exprs_par = []
        num_vars_par = int(input("How many variables?"))
        for i in range(num_vars_par):
            exprs_par.append(input("Please enter each variable letter:"))
        DONE = False
        while not DONE:
            aab = input("Please enter each expression. Type 'DONE' and press enter when finished.")
            if aab == "DONE":
                break
            else:
                exprs_par.append(aab)
            
     
    truth_tbl(exprs_par, num_vars_par)
        
    
