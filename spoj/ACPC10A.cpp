#include<iostream>
using namespace std;
int main()
{
int a,b,c,n,q=1;
while(q)
{
cin>>a>>b>>c;
if(a==0 && b==0 && c==0)
{	q=0;
	break;
}
else
{
	n=(a-b)/(b-c);
	if(n==1)
	{
		cout<<"AP "<<(c+b-a)<<'\n';
	}
	else
	{
		cout<<"GP "<<((c*b)/a)<<'\n';
	}
}
}
return 0;
}
