#include <iostream>
#include<bits/stdc++.h>
using namespace std;
// https://pasteme.cn/59514
map<string,int>mp;
map<int,string>fmp;
int Edge[500][500]= {0};
int top = 0;
int id(string s)
{
    if(mp[s])return mp[s];
    else
    {
        mp[s] = top++;
        fmp[top-1] = s;
        return mp[s];
    }
}
string fid(int id)
{
    return fmp[id];
}
int head[5000],cnt;
struct node
{
    int u,v,w,next;
} edge[5000];
void addedge(int u,int v,int w)
{

    edge[cnt].u = u;
    edge[cnt].v = v;
    Edge[u][v] = 1;
    Edge[v][u] = 1;

    edge[cnt].w = w;
    edge[cnt].next = head[u];
    head[u] = cnt++;
}
int vis[5000];
const int M = 8;
int Cnt=0;
void dfs(int id,int step,string ans)
{
    if(step>=M)
    {
        // cout<<++Cnt<<endl;
        cout<<ans<<endl;
        return ;
    }
    //cout<<id<<endl;
    for(int i=head[id]; ~i; i=edge[i].next)
    {
        int v = edge[i].v;
        if(!vis[v])
        {
            vis[v] = 1;
            string k = ans;
            k+=fid(v);
            dfs(v,step+1,k);
            vis[v] = 0;
        }
    }
}
bool pan(char a,char b)
{

    string ta;
    ta+=a;
    string tb ;
    tb+=b;
    int aa = id(ta);
    int bb = id(tb);
    return Edge[aa][bb];
}
struct data
{
    string name;
    int num;

};
int cmp(data a,data b)
{
    return a.num>b.num;
}
int main()
{
    freopen("data.txt","r",stdin);
//    freopen("data.out","w",stdout);
    int n;
    cin>>n;
    cnt = 0;
    memset(head,-1,sizeof head);
    for(int i=1; i<=n; i++)
    {
        string a,b;
        cin>>a>>b;
        if(a[0]>='A'&&a[0]<='Z'&&b[0]>='A'&&b[0]<='Z')
        {
            string pa,pb;
            pa += a[0]+32;
            pb += b[0]+32;
            int aa = id(pa);
            int bb = id(pb);
            //  cout<<fid(aa)<<" "<<fid(bb)<<endl;
            addedge(aa,bb,1);
            addedge(bb,aa,1);
        }
        int aa = id(a);
        int bb = id(b);
        //  cout<<fid(aa)<<" "<<fid(bb)<<endl;
        addedge(aa,bb,1);
        addedge(bb,aa,1);
    }
//    cout<<"ok"<<endl;
    freopen("CON", "r", stdin);
    cout<<"ok2"<<endl;
    freopen("out.txt","r",stdin);

//    cout<<"ok2"<<endl;
    string s;
    map<string,int>OUT;
    int ans = 0;
//    cout<<pan('a','s')<<endl;
//    cout<<pan('s','d')<<endl;
//    cout<<pan('d','f')<<endl;
//    cout<<pan('f','g')<<endl;
//    cout<<pan('g','h')<<endl;


    while(getline(cin,s))
    {
        int len = s.size();
        for(int i=0; i<len-1; i++)
        {

            int num = 1;
            string record;
            record+=s[i];
            for(int j=i; j<len-1; j++)
            {

                if(pan(s[j],s[j+1]))
                {
                    record+=s[j+1];
                    num++;
                }
                else
                {
                    i = j+1;
                    break;
                }
            }
            if(num>=5)
            {
                ans++;
//                 cout<<record<<endl;
                OUT[record]++;
                break;
            }

        }

    }
    cout<<ans<<endl;
    vector<data>vc;
    cout<<"yy"<<endl;
    for(auto it:OUT)
    {

//       cout<<it.second<<" "<<it.first<<endl;
        vc.push_back(data{it.first,it.second});
    }
    sort(vc.begin(),vc.end(),cmp);
    int uu = 0;
    for(auto h:vc)
    {
        uu++;
        if(uu>100)break;
        cout<<h.name<<" "<<h.num<<endl;
    }

//    for(int i=0; i<111; i++)
//    {
//        memset(vis,0,sizeof vis);
//        vis[i] = 1;
//        dfs(i,0,fmp[i]);
//    }


    return 0;
}
