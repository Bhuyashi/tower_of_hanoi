import sys

def printStep(n,start,end):
    print(str(n),":",str(start),"->",str(end))

def drawTowers(towers,N):
    lens = [len(towers[0]),len(towers[1]),len(towers[2])]
    for i in range(N,0,-1):
        for j in range(3):
            if i <= len(towers[j]):
                for k in range(N-towers[j][lens[j]-i]):
                    print(' ' ,end='')
                for k in range(towers[j][lens[j]-i]):
                    print('-' ,end='')
                print('|',end="")
                for k in range(towers[j][lens[j]-i]):
                    print('-' ,end='')
                for k in range(N-towers[j][lens[j]-i]):
                    print(' ' ,end='')
            else:
                for k in range(N):
                    print(' ' ,end='')
                print('|',end="")
                for k in range(N):
                    print(' ' ,end='')
        print(end='\n')
    print('='*(3*N*2+3))

def towerOfHanoi(N):
    def recurse(n,start,end,towers,N):
        other = 6 - (start+end)
        if n==0:
            return
        recurse(n-1,start,other,towers,N)
        # printStep(n,start,end)
        towers[end-1] = [towers[start-1][0]] + towers[end-1]
        towers[start-1] = towers[start-1][1:]
        drawTowers(towers,N)
        recurse(n-1,other,end,towers,N)
    l = list(range(1,N+1))
    t = [l,[],[]]
    drawTowers(t,N)
    recurse(n=N,start=1,end=3,towers=t,N=N)

if __name__ == '__main__':
    N = sys.argv[1]
    towerOfHanoi(int(N))