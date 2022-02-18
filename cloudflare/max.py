def max_1(data):
    '''finds the max sequence of 1s from the list'''
    max_ones = max(map(len,data[0].split('0')))
    for i in range(1,100):
        if max(map(len,data[i].split('0')))  > max_ones:
            max_ones = max(map(len,data[i].split('0')))
    return(max_ones)


def max_0(data):
    '''finds the max sequence of 0s from the list'''
    max_zeros = max(map(len,data[0].split('1')))
    for i in range(1,100):
        if max(map(len,data[i].split('1')))  >  max_zeros:
            max_zeros = max(map(len,data[i].split('1')))
    return(max_zeros)