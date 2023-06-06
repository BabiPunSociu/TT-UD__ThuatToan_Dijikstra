from ast import main
import queue
from re import U
import zipapp
import zipfile


class Graph:
    def nhap(self):
        self.n, self.m = map (int , input().split())
        self.A = [[] for i in range(self.n+1)]
        for i in range (self.m):
            u,v,w = map (int , input().split())
            self.A[u].append((w,v))
    def Dijkstra(self,s):   # tim duong di ngan nhat tu s den cac dinh
        L=[1e9]*(self.n+1)  # do dai ngan nhat nhat tu s den i luu vao L[i]
        p=[0]*(self.n+1)    # mang cho
        Q = queue.PriorityQueue()
        Q.put((0,s))
        L[s] =0
        while Q.qsize():
            d,u=Q.get() # u:dinh    d:khoang cach ngan nhat s->u
            if d>L[u]: continue
            for z,u in self.A[u]:
                if L[v]>d+z:
                    L[v]=d+z 
                    p[v]=u 
                    Q.put((d+z,v))
        for i in range(1, self.n+1):
            print("\nDo dai duong di ngan nhat tu %d den %d la: %d"%(s,i,L[i]))
            if L[i]<1e9 : self.inpath(s,i,p)
    def inpath(self,s,i,p):
        if s==1: print(s,end="")
        else:
            self.inpath(s,p[i],p)
            print("->%d"%(i),end="")
            
if __name__ == "__main__":
    G = Graph
    G.nhap
    G.Dijkstra(1)





