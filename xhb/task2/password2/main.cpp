#include <iostream>
#include <sstream>
#include<bits/stdc++.h>
using namespace std;
int id(char c)
{
    if(c>='a'&&c<='z')return 1;
    else if(c>='A'&&c<='Z')return 1;
    else if(c>='0'&&c<='9')return 2;
    else return 3;
}
int main()
{
    freopen("password2.txt","r",stdin);
    freopen("Change_password2.txt","w",stdout);
    string str;
//    cin>>str;
    while(getline(cin,str))
    {
        string ans;
        int len = str.size();
        int cnt = 0,pre = -1;
        for(int i=0; i<len; i++)
        {
            int u = id(str[i]);
            if(pre==u)
            {
                cnt++;
            }
            else if(pre!=-1)
            {
//        if(pre==-1)continue;
                string num;
                stringstream ss;
                ss<<cnt;
                ss>>num;
                cnt = 1;
                if(pre==1)
                {
                    ans+='L';
                }
                else if(pre==2) ans+='N';
                else ans+='O';

                ans+=num;
                ans+=' ';
            }
            pre = u;
        }
        string num;
        stringstream ss;
        ss<<cnt;
        ss>>num;
        cnt = 0;
        if(pre==1)
        {
            ans+='L';
        }
        else if(pre==2) ans+='N';
        else ans+='O';
        ans+=num;
        ans+=' ';
        cout<<ans<<endl;

    }

    return 0;
}
