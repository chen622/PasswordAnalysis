#include <iostream>
#include<bits/stdc++.h>
using namespace std;
map<string,int>mp;
map<int,string>fmp;
int cnt =1;
int id(string a){
   if(mp[a])return mp[a];
   else mp[a]=cnt++;
   fmp[cnt-1] = a;
//   cout<<cnt<<endl;
   return mp[a];
}
string fid(int id){
   return fmp[id];
}
int main()
{

    freopen("Change_password2.txt","r",stdin);
    freopen("Password_number3.txt","w",stdout);
//    freopen("id.txt","w",stdout);
    string str;
   // int cnt = 0;
    int pp =0;
    while(getline(cin,str)){

        stringstream ss(str);
        string a,OUT;
        int uu = 0;
//        cout<<str<<endl;
        while(ss>>a){
            uu++;
            int ids = id(a);
            stringstream tt;
            tt<<ids;
            string temp;
            tt>>temp;
            OUT+=temp;
            OUT+=" ";
        }
        string out;
        if(uu>1)
        {
//            tt>>out;
            cout<<OUT<<endl;
        }
//        if(pp++>6)
//        break;
    }
//    cout<<cnt<<endl;
//    for(int i=1;i<cnt;i++){
//        cout<<fid(i)<<" ";
//    }
//    cout<<endl;
    return 0;
}
