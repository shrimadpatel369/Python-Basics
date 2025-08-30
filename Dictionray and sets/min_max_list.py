def main(e):
    list1 = list(e)

    M = list1[0]
    m = list1[0]

    for x in list1:
        if x < m:
            m = x
    for x in list1:
        if M < x:
            M = x
    return(m,M)
e = e ={13,2,47,23,71,17}
print("(Min,Max):",main(e))
