//Program to find index of matrix element
#include<bits/stdc++.h>
using namespace std;

int main()
{int m,n,k;
    cin>>m;
    cin>>n;
    cin>>k;
    int a[m][n];
    int i;
    int j,l=0;
    for(i=0;i<m;i++)
    { for(j=0;j<n;j++)
        cin>>a[i][j];}
    for(i=0;i<m;i++)
    { for(j=0;j<n;j++)    
        {if(a[i][j]==k)
        
        {cout<<"True"<<i+1<<","<<j+1<<endl;
        l++; }
    
      
        }
        
    }    
        
    if(l==0)
    cout<<"False";


}