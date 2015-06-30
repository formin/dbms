
# header find
def h_find(h_l, h_elem):
    return h_l.index(h_elem)

# data find
def data_find(l, elem, sheader):

    for row, i in enumerate(l):
        try:
            column = i.index(elem)
        except ValueError:
            continue

        if column == sheader:
         return row

    return -1
