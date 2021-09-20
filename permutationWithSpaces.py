'''
suppose the given string is abc the the output should be "a_b_C","a_bc","ab_c","abc
"_" = spaces here
'''

def solve(ip, op, uniqueset):
    if len(ip) == 0:
        uniqueset.append(op)
        return
    op1 = op+ ip[0]
    op2 = op +" " + ip[0]
    ip = ip[1:]
    solve(ip, op1, uniqueset)
    solve(ip, op2, uniqueset)
    return uniqueset


ip = "abc"
op = ""
op = op + ip[0]
ip = ip[1:]
global unique
unique = list()
unique = solve(ip, op, unique)
unique.sort()
print(unique)
