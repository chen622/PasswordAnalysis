// 求解两个字符串的公共子串
// 将这两个字符串展开成一个矩阵形式, 行元素为第一个字符串元素. 列元素为第二个字符串元素
// 比较每行与每列中元素个数是否相同, 相同的可置其位置为1, 不相同则置其位置为0
// 累加斜对角线上的元素个数, 最大的即为两字符串的公共子串个数,
// 它们的行下标在第一个字符串中的元素或是列下标在第二个字符串中的元素即为公共子串
// 若存在多个长度相同的子串则匹配第一个子串
#include<iostream>
#include<cstring>
#include<cstdio>
#include<bits/stdc++.h>
using namespace std;

void TwoStringMaxSubstring(string str1, string str2, int &maxlen, int &pos)
{
    int len = 0; // 用于记录两个字符串中较长的字符串的长度

    if (str1 == "" || str2 == "") // 有一个字符串为空，直接结束
        return;

    int len1 = str1.length();
    int len2 = str2.length();

    if (len1 >= len2)
        len = len1;
    else
        len = len2;

    // 定义两个整型数组, 用于记录相匹配的子串个数信息
    int topLine[len];
    int currentLine[len];

    // 数组初始化
    for (int i = 0; i < len; i++)
    {
        topLine[i] = 0;
        currentLine[i] = 0;
    }

    char temp_ch = ' ';

    // 将第一个字符串中的每一个字符依次与第二个字符串的第1, 2, 3,...i,...,n个字符 进行比较
    // 逐行比较
    for (int i = 0; i < len2; i++)
    {
        temp_ch = str2[i];

        for (int j = 0; j < len1; j++)
            if (temp_ch == str1[j])
            {
                if (j == 0)
                {
                    currentLine[j] = 1; // 若为第一列, 则赋值1
                }
                else
                {
                    currentLine[j] = topLine[j-1] + 1; // 在上一个斜对角线的元素个数基础上再加1
                }

                if (currentLine[j] > maxlen)
                {
                    maxlen = currentLine[j];
                    pos = j;
                }
            }

        // 将当前行的字符信息存储起来, 再将数组置为空
        for (int k = 0; k < len; k++)
        {
            topLine[k] = currentLine[k];
            currentLine[k] = 0;
        }
    }
}
string out(string str1,string str2)
{
    //string str1, str2; // 两个字串
    int maxlen = 0, pos = 0; // 最大字串的长度和其下标
//	cout<<"Please input the first string: ";
    //getline(cin, str1); // 输入第一个子串
//	cout<<"Please input the second string: ";
    //getline(cin, str2); // 输入第二个子串
    TwoStringMaxSubstring(str1, str2, maxlen, pos);
//	cout<<"The maximum same substring of these two substring is: "<<<<endl;
    return str1.substr(pos-maxlen+1, maxlen);
}
int main()
{
    freopen("csdn4.txt","r",stdin);
    string a,b,c,bb;
    int ans2 = 0;
    int ans3 = 0;
    int total =0 ;
    while(cin>>a)
    {
//        stringstream ss;
        getline(cin,bb);
        reverse(bb.begin(),bb.end());
        int i = bb.find(' ');
        int len = bb.size();
        b = bb.substr(i,len-i);
        reverse(b.begin(),b.end());
        c = bb.substr(0,i);
        reverse(c.begin(),c.end());
        //cout<<a<<" "<<b<<" "<<c<<endl;
        total++;
        int ans =0;
        if(out(a,b).size()>5)
        {
            ans++;
//            cout<<a<<" "<<b<<endl;
            if(a==b)ans3++;
        }

//        cout<<out(a,b)<<endl;
//        if(out(c,b).size()>5)
//            ans++;
//        cout<<out(b,c)<<endl;
//        cout<<"==="<<endl;
        if(ans>0)ans2++;
    }
    cout<<total<<" "<<ans2<<" "<<ans3<<endl;



    return 0;
}
