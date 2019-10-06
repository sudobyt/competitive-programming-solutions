#include<iostream>
using namespace std;
int rev(int n)
{
	int r=0,rem;
	while(n!=0)
	{
		rem=n%10;
		r=r*10+rem;
		n/=10;
	}
	return r;
}
int main()
{

	int a,b,t,sum,revsum;
	cin>>t;
	while(t--)
	{
	
	cin>>a>>b;
	int r1=rev(a);
	int r2=rev(b);
	sum=r1+r2;
	revsum=rev(sum);
	cout<<revsum<<endl;
	}
return 0;
}
