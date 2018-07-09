H = int(input())
M = int(input())
S = int(input())
if (0<=H<=12) and (0<=M<=60) and (0<=S<=60):
    print((H*3600 + M*60 + S)/(12*3600/360))
