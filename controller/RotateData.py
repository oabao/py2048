
def roateup(data):
    return roatedown(data)

def roatedown(data):
    resdata = []
    for idx in range(3, -1, -1):
        resdata.append(data[idx])
    return resdata


def roateright(data):
    resdata = []
    for oldidy in range(0,4,1):
        newline = []
        for oldidx in range(3,-1,-1):
            newline.append(data[oldidx][oldidy])
        resdata.append(newline)

    return resdata


def roateleft(data):
    resdata = []
    for oldidx in range(3, -1, -1):
        newline = []
        for oldline in data:
            #print(oldline)
            newline.append(oldline[oldidx])
        resdata.append(newline)
    return resdata