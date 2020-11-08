#include <cstdio>
#include <algorithm>
#include <cstring>
#include<iostream>
#include <string>
#include <vector>
#define setIO(s) freopen(s".in","r",stdin)
#define maxn 2000009
#define N 230
using namespace std;
int result,query,n,M;
char s[3000009];

void Decode(int mask){
    int nn=strlen(s);
    for(int j=0;j<nn;j++){
        mask=(mask*231+j)%nn;
        swap(s[j],s[mask]);
    }
}
struct Link_Cut_Tree{
    int ch[maxn][2],f[maxn],tag[maxn],sta[maxn],val[maxn];
    int get(int x) {return ch[f[x]][1]==x; }
    int which(int x){ return ch[f[x]][1]==x;}
    int isRoot(int x){ return !(ch[f[x]][1]==x||ch[f[x]][0]==x);}
    int lson(int x){ return ch[x][0];}
    int rson(int x){return ch[x][1];}
    void add(int x,int delta){if(!x)return;val[x]+=delta,tag[x]+=delta;}
    void pushdown(int x){if(tag[x]) add(lson(x),tag[x]),add(rson(x),tag[x]),tag[x]=0;}
    void rotate(int x){
        int old=f[x],fold=f[old],which=get(x);
        if(!isRoot(old)) ch[fold][ch[fold][1]==old]=x;
        ch[old][which]=ch[x][which^1],f[ch[old][which]]=old;
        ch[x][which^1]=old,f[old]=x,f[x]=fold;
    }
    void splay(int x){
        int v=0,u=x;
        sta[++v]=u;
        while(!isRoot(u)) sta[++v]=f[u],u=f[u];
        while(v) pushdown(sta[v--]);
        u=f[u];
        for(int fa;(fa=f[x])!=u;rotate(x))
            if(f[fa]!=u) rotate(get(fa)==get(x)?fa:x);
    }
    void Access(int x){
        for(int y=0;x;y=x,x=f[x])
            splay(x),ch[x][1]=y;
    }
    void link(int a,int b){
        Access(a),splay(a),add(a,val[b]),f[b]=a;
    }
    void cut(int b){
        Access(b),splay(b);
        add(lson(b),-val[b]),f[lson(b)]=ch[b][0]=0;
    }
}tree;
struct Suffix_Automaton{
    int last,tot,dis[maxn],ch[maxn][N];
    int f[maxn];
    void init(){last=tot=1;}
    void ins(int c){
        int p=last,np=++tot; last=np; dis[np]=dis[p]+1;tree.val[np]=tree.tag[np]=1;
        while(p&&!ch[p][c])ch[p][c]=np,p=f[p];
        if(!p) f[np]=1,tree.link(1,np);
        else{
            int q=ch[p][c],nq;
            if(dis[q]==dis[p]+1)f[np]=q,tree.link(q,np);
            else{
                nq=++tot;tree.val[nq]=0;
                dis[nq]=dis[p]+1;
                memcpy(ch[nq],ch[q],sizeof(ch[q]));
                //printf("%d\n",q)
                f[nq]=f[q];
                tree.link(f[q],nq),tree.cut(q),tree.link(nq,q),tree.link(nq,np);
                f[q]=f[np]=nq;
                while(p&&ch[p][c]==q) ch[p][c]=nq,p=f[p];
            }
        }
    }
    int search_str(){
        n=strlen(s);
        int p = 1;
        for(int i=0;i<n;++i) {
            if(!ch[p][s[i]]) return -1;
            p=ch[p][s[i]];
        }
        return p;
    }
}sam;
struct node{
   string a;
   int num;
};
vector<node>vc;
int cmp(node a,node b){
    return a.num>b.num;
}
int main(){
    //setIO("input");
    freopen("out.txt","r",stdin);
    sam.init();
    gets(s);
    //scanf("%s",s);
    n=strlen(s);
    printf("%d\n",n);
    query = 2498;
    for(int i=0;i<n;++i) sam.ins(s[i]);
    int opt=2;
     int u;
    while(query--){
        scanf("%s",s+1);
       // Decode(M);
        if(opt==1) {
            n=strlen(s);
            for(int i=0;i<n;++i) sam.ins(s[i]);
        }
        if(opt==2) {
            n=strlen(s);
            s[0] = '#';
            s[n]='#';
            s[n+1]='\0';
             n=strlen(s);
//            cout<<s<<endl;
            u=sam.search_str();
            if(u==-1) result=0;
            else tree.Access(u),tree.splay(u),result=tree.val[u];
           // M^=result;
            if(result!=0)
            //printf("%s %d\n",s,result);
            vc.push_back(node{s,result});


        }
    }
    sort(vc.begin(),vc.end(),cmp);
    for(int i=0;i<min((int)vc.size(),100);i++){
        cout<<vc[i].a<<" "<<vc[i].num<<endl;
    }
    return 0;
}
