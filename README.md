# Set-Functions
Implementations of Disjoint Sets using Linked Lists.

# Function
<p>MAKE-SET(x) creates a new set whose only member (and thus representative) is x. Since the sets are disjoint, we require that x not already be in some other set.</p>
<p>FIND-SET(x) returns a pointer to the representative of the (unique) set containing x.</p>
<p>UNION(x,y) unites the dynamic sets that contain x and y, say Sx and Sy, into a new set that is the union of these two sets.</p>
<p>CONNECTED-COMPONENTS(v,e) initially places each vertex  in its own set. Then, for each edge (u,v), it unites the sets containing u and v.</p>
<p>SAME-COMPONENT(u,v) can determine whether two vertices are in the same connected component.</p>

<h1> How To Use</h1>
<h2>MakeSet:</h2>
<p>a = Set()<br />
MakeSet(a)</p>
<p>Description: We will make an object through set class and pass the parameter in the MakeSet function to create a new set</p>
<h2>FindSet:</h2>
<p>MakeSet(a)<br />
a = Set()<br /> 
FindSet(a)</p>
<p>Description: We will make an object through set class and pass the parameter in the FindSet function to find an existing set</p>
<h2> Union:</h2>
<p>MakeSet(a)<br />
MakeSet(b)<br />
a = Set()<br />
b = Set()<br />
Union(a,b)</p>
<p>Description: We will make a and b objects through set class and pass the parameter in the Union function to unite two sets</p>
<h2>ConnectedComponent:</h2>
<p>a = Set()<br />
b = Set()<br />
c = Set()<br />
d = Set()<br />
vertices = [a,b,c,d]<br />
edges = [(b,d),(a,b),(a,c)]<br />
ConnectedComponent(vertices,edges)</p>
<p>Description: We will make objects through set class,store vertices and edges in a list and pass the parameters in the Connected Component function to make a graph.</p>
<h2>SameComponent:</h2>
<p>a = Set()<br />
b = Set()<br />
c = Set()<br />
d = Set()<br />
vertices = [a,b,c,d]<br />
edges = [(b,d),(a,b),(a,c)]<br />
ConnectedComponent(vertices,edges)<br />
SameComponent(a,b)</p>
<p>Description: We will make a and b object through set class and pass the parameters in the SameComponent function to check if two vertices are in the same connected component.</p>
