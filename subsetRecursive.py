import string


def solve(ip, op, uniqueset):
    if len(ip) == 0:
        uniqueset.append(op)
        return
    op1 = op
    op2 = op + ip[0]
    ip = ip[1:]
    solve(ip, op1, uniqueset)
    solve(ip, op2, uniqueset)
    return uniqueset


ip = "aab"
op = " "
global unique
unique = list()
unique = solve(ip, op, unique)
uni = list()
for i in unique:
    if i in uni:
        pass
    else:
        uni.append(i)
print(uni)
