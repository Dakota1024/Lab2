def createMenu(ls):
    st = ""
    for num in range(len(ls)):
        st += str(num) + ") " + ls[num] + "\n"
    return st
