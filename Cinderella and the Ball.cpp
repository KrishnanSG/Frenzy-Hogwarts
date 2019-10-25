// Solution to Cinderella and the Ball problem.

#include<iostream>
#include<math.h>
using namespace std;

int gcd(int, int);
int main()
{
    int n, m, q, i;
    cin>>n>>m>>q;
    int cx[q], cy[q], px[q], py[q];
    for(i=0;i<q;i++)
        cin>>cx[i]>>cy[i]>>px[i]>>py[i];
    int groupc, groupp, g;
    g=gcd(n,m);
    for(i=0;i<q;i++)
    {
        groupc  = ceil(cy[i]*g/cx[i]);
        groupp  = ceil(py[i]*g/px[i]);
        if(groupc==groupp)
            cout<<"YES";
        else
            cout<<"NO";
        cout<<endl;
    }
}

int gcd(int n, int m)
{
    if (n == 0)
       return m;
    if (m == 0)
       return n;
    if (n == m)
        return n;
    if (n > m)
        return gcd(n-m, m);
    return gcd(n, n-m);
}
