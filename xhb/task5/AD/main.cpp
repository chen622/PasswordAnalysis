// ��������ַ����Ĺ����Ӵ�
// ���������ַ���չ����һ��������ʽ, ��Ԫ��Ϊ��һ���ַ���Ԫ��. ��Ԫ��Ϊ�ڶ����ַ���Ԫ��
// �Ƚ�ÿ����ÿ����Ԫ�ظ����Ƿ���ͬ, ��ͬ�Ŀ�����λ��Ϊ1, ����ͬ������λ��Ϊ0
// �ۼ�б�Խ����ϵ�Ԫ�ظ���, ���ļ�Ϊ���ַ����Ĺ����Ӵ�����,
// ���ǵ����±��ڵ�һ���ַ����е�Ԫ�ػ������±��ڵڶ����ַ����е�Ԫ�ؼ�Ϊ�����Ӵ�
// �����ڶ��������ͬ���Ӵ���ƥ���һ���Ӵ�
#include<iostream>
#include<cstring>
#include<cstdio>
#include<bits/stdc++.h>
using namespace std;

void TwoStringMaxSubstring(string str1, string str2, int &maxlen, int &pos)
{
    int len = 0; // ���ڼ�¼�����ַ����нϳ����ַ����ĳ���

    if (str1 == "" || str2 == "") // ��һ���ַ���Ϊ�գ�ֱ�ӽ���
        return;

    int len1 = str1.length();
    int len2 = str2.length();

    if (len1 >= len2)
        len = len1;
    else
        len = len2;

    // ����������������, ���ڼ�¼��ƥ����Ӵ�������Ϣ
    int topLine[len];
    int currentLine[len];

    // �����ʼ��
    for (int i = 0; i < len; i++)
    {
        topLine[i] = 0;
        currentLine[i] = 0;
    }

    char temp_ch = ' ';

    // ����һ���ַ����е�ÿһ���ַ�������ڶ����ַ����ĵ�1, 2, 3,...i,...,n���ַ� ���бȽ�
    // ���бȽ�
    for (int i = 0; i < len2; i++)
    {
        temp_ch = str2[i];

        for (int j = 0; j < len1; j++)
            if (temp_ch == str1[j])
            {
                if (j == 0)
                {
                    currentLine[j] = 1; // ��Ϊ��һ��, ��ֵ1
                }
                else
                {
                    currentLine[j] = topLine[j-1] + 1; // ����һ��б�Խ��ߵ�Ԫ�ظ����������ټ�1
                }

                if (currentLine[j] > maxlen)
                {
                    maxlen = currentLine[j];
                    pos = j;
                }
            }

        // ����ǰ�е��ַ���Ϣ�洢����, �ٽ�������Ϊ��
        for (int k = 0; k < len; k++)
        {
            topLine[k] = currentLine[k];
            currentLine[k] = 0;
        }
    }
}
string out(string str1,string str2)
{
    //string str1, str2; // �����ִ�
    int maxlen = 0, pos = 0; // ����ִ��ĳ��Ⱥ����±�
//	cout<<"Please input the first string: ";
    //getline(cin, str1); // �����һ���Ӵ�
//	cout<<"Please input the second string: ";
    //getline(cin, str2); // ����ڶ����Ӵ�
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
