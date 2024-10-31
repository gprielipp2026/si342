class PLVException (Exception):
    pass

class DFA:
    def __init__(self,M):
        self.Q,self.E,self.D,self.s,self.W = M
        self.Tmap = {(p,x):q for p,x,q in self.D} 

    def run(self,w):
        try:
            q = self.s
            for x in w:
                q = self.Tmap[(q,x)]
            return q in self.W
        except KeyError:
            return False

    def showrun(self, w):
        q = None
        try:
            q = self.s
            for x in w:
                print(str(q) + " =" + str(x) + "=> ", end="")
                q = self.Tmap[(q,x)]
            print(str(q))
            return q in self.W
        except KeyError:
            print(str(q))
            return False

    def find(self, arr, val):
        hitInds = []
        for i, x in enumerate(arr):
            if x == val:
                hitInds.append(i)
        return hitInds

    def plv2(self, w):
        if not self.run(w):
            raise PLVException(''.join(w) + " not accepted by M")

        visited = {q: False for q in self.Q}
        path = []
        char = None
        try:
            q = self.s
            for char in w:
                if visited[q]:
                    path.append(q)
                    first, second = self.find(path, q)
                    x = w[0:first]
                    y = w[first:second]
                    z = w[second:] 
                    return (x, y, z) 
                
                visited[q] = True
                path.append(q)
                q = self.Tmap[(q,char)]
            # somehow no loop happened
            return ("", "", w) 
            
        except KeyError:
            raise PLVException(str(char) + " not in alphabet " + str(self.E))
