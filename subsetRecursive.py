import string


def Solve(ip,op):
    if len(ip) == 0:
        print(op,end=" ")
        return
    op1 = op
    op2 = op + ip[0]
    ip = ip[1:]
    Solve(ip,op1)
    Solve(ip,op2)
    return
ip = "abc"
op = " "
Solve(ip,op)