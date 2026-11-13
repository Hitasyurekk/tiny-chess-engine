import json,os,re,urllib.request as U
E=os.environ.get("MAKEFUN_ENV_URL")
N,S=-10,10
V=dict(P=100,N=310,B=330,R=500,Q=920,K=60000)
G="KKKKUUUUMMOQLLMPKKKOLJIKLMMGKKKKACEECGKKEKMNELNOEKNOELMNCGKLACEEGIIIIKKKIKLMILLMIKMMIMMMILKKGIIIKKKKLMMMJKKKJKKKJKKKJKKKJKKKKKKLECCAECCAECCAECCAGEECIGGGOOKKOQMKACEGEGIKEIOQEIQSEIQSEIOQEEKKAEEE"
def tab(g):
 Z={}
 for o,p in enumerate(V):
  Z[p]=t=[0]*120
  for i in range(64):r,f=divmod(i,8);t[21+r*10+f]=V[p]+5*ord(G[32*((0,1,2,3,2,4)[o]+(g and o>4))+r*4+min(f,7-f)])-375+(g and o<1)*b'\0<#\17\5\0\0\0'[r]
 return Z
Z=tab(0)
B=-9,-11,9,11;O=N,S,1,-1
D=dict(P=(N,2*N,-11,-9),N=(-21,-19,-8,-12,12,8,19,21),B=B,R=O,Q=B+O,K=B+O)
P=__import__('collections').namedtuple('P','b s w c e k')
MU,ML=69200,50800
def gen(p):
 b=p.b
 for o in re.finditer('[A-Z]',b):
  i=o.start();x=o[0]
  for d in D[x]:
   j=i+d
   while 1:
    y=b[j]
    if y<'.'or'@'<y<'['or x=='P'and(d%10<1 and y!='.'or d<-19 and(i<81 or b[i+N]!='.')or d%10 and y=='.'and j not in(p.e,p.k,p.k-1,p.k+1)):break
    yield i,j
    if x in'PNK'or y>'Z':break
    if i==91 and b[j+1]=='K'and p.w[0]:yield j+1,j-1
    if i==98 and b[j-1]=='K'and p.w[1]:yield j-1,j+1
    j+=d
def val(p,m):
 i,j=m;b=p.b;x=b[i];y=b[j];t=Z[x];s=t[j]-t[i]
 if y>'Z':s+=Z[y.upper()][119-j]
 if abs(j-p.k)<2:s+=Z['K'][119-j]
 if x=='K'and abs(j-i)==2:s+=Z['R'][(i+j)//2]-Z['R'][(91,98)[j>i]]
 if x=='P':
  if j<29:s+=Z['Q'][j]-t[j]
  if j==p.e:s+=Z['P'][129-j]
 return s
rot=lambda b:b[::-1].swapcase()
def mv(p,m):
 i,j=m;b=list(p.b);x=b[i];w,c=p.w,p.c;e=k=0;b[j]=x;b[i]='.'
 w=(w[0]and i!=91,w[1]and i!=98);c=(c[0]and j!=28,c[1]and j!=21)
 if x=='K':
  w=(0,0)
  if abs(j-i)==2:k=(i+j)//2;b[(91,98)[j>i]]='.';b[k]='R'
 if x=='P':
  if j<29:b[j]='Q'
  if j-i==2*N:e=i+N
  if j==p.e:b[j+S]='.'
 return P(rot(''.join(b)),-p.s-val(p,m),c,w,e and 119-e,k and 119-k)
nul=lambda p:P(rot(p.b),-p.s,p.c,p.w,0,0)
def chk(p):q=nul(p);return any(val(q,m)>=ML for m in gen(q))
def F(p,a,z,d,h):
 global n
 n+=1
 if n>H:raise TimeoutError
 if p.s<=-ML:return-MU
 if h and p.b in R:return 0
 q=d<1;e=tt.get(p);bm=w=None;a0=a;o=-MU
 if e:
  t,v,f,bm=e
  if t>=d and h and(f==0 or f>0 and v>=z or f<0 and v<=a):return v
 if q:
  o=p.s
  if o>=z:return o
  a=max(a,o)
 elif d<3 and h and p.s-120*d>=z:return p.s
 elif d>2 and h and p.s>=z and re.search('[NBRQ]',p.b):
  v=-F(nul(p),-z,1-z,d-3,h+1)
  if v>=z:return v
 L=sorted(((val(p,m),m)for m in gen(p)if not q or p.b[m[1]]>'Z'or abs(m[1]-p.k)<2 or m[1]<29 and p.b[m[0]]=='P'),reverse=True)
 if bm:L.sort(key=lambda x:x[1]!=bm)
 for k,(v,m) in enumerate(L):
  if q and p.s+v+200<a:break
  if 0<d<3 and k and v<50 and p.s+v+150*d<a:continue
  c=mv(p,m);s=-F(c,-a-1,-a,d-2,h+1)if d>2 and k>3 and v<50 else a+1
  if s>a:s=-F(c,-z,-a,d-1,h+1)
  if s>o:o=s;w=m
  a=max(a,s)
  if a>=z:break
 if not q:
  if o<=-ML:o=h-MU if chk(p)else 0
  tt[p]=(d,o,(o>=z)-(o<=a0),w)
 return o
def think(p):
 global n,tt
 n=0;tt={};m=None
 try:
  for d in range(1,40):
   v=F(p,-MU,MU,d,0);m=tt[p][3]
   if n>H/4.7 or v>ML:break
 except:pass
 return m
sq=lambda s:4+ord(s[0])-10*int(s[1])
nm=lambda i:chr(i%10+96)+str(10-i//10)
def fen(f):
 global Z
 a=f.split();b=' '*21+'  '.join(re.sub(r'\d',lambda m:'.'*int(m[0]),r)for r in a[0].split('/'))+' '*21
 Z=tab(sum(V[x]for x in b.upper()if x in'NBRQ')<2600)
 c=a[2];e=a[3]!='-'and sq(a[3]);x=('Q'in c,'K'in c);y=('k'in c,'q'in c)
 p=P(rot(b),0,y,x,e and 119-e,0)if a[1]=='b'else P(b,0,x,y,e,0)
 return p._replace(s=sum(Z[x][i]if x.isupper()else-Z[x.upper()][119-i]for i,x in enumerate(p.b)if x.isalpha()))
post=lambda u,d:json.load(U.urlopen(U.Request(E+u,json.dumps(d).encode(),{'content-type':'application/json'})))
H=1.6e5
while E:
 g=post('/game',{})
 if g['status']=='done':break
 while g['status']=='your_move':
  R=set();f=g['start_fen'];o=fen(f);bl=f.split()[1]=='b';X=lambda i:bl and 119-i or i
  for u in g['moves']:R.add(o.b);o=mv(o,(X(sq(u)),X(sq(u[2:]))));bl=not bl
  p=fen(g['fen']);m=think(p);L=g['legal_moves'];u=m and nm(X(m[0]))+nm(X(m[1]))+'q'*(p.b[m[0]]=='P'and m[1]<29)
  g=post('/move',{'game':g['game'],'move':u if u in L else L[0]})
