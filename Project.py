class Set:
    def __init__(self):
        self.head = None
        self.tail = None
        self.next = None
            
def MakeSet(x):
    if FindSet(x) is None:
        x.head = x
        x.tail = x
        
        
def FindSet(x):
    return x.head

    
def Union(x,y):
    x.tail.next = y
    z = x.head
    while z != None:
        z.head = x.head
        z.tail = y.tail
        z = z.next
    
def Same_Component(u,v):
    if FindSet(u) == FindSet(v):
        return True
    return False

def Connected_Component(vertices,edges):
    for vertex in vertices:
        MakeSet(vertex)
    for edge in edges:
        if FindSet(edge[0])!= FindSet(edge[1]):
            Union(edge[0],edge[1])
