#include <iostream>

using namespace std;

int main()
{

    int i,j,x,y,ans,a[5][5];
    for(i=0;i<5;i++){
        for(j=0;j<5;j++){
            cin>>a[i][j];
        }
    }
     for(i=0;i<5;i++){
        for(j=0;j<5;j++){
            if(a[i][j]==1){
                x=i+1;
                y=j+1;
            }
        }
    }
    ans=abs(x-3)+abs(y-3);
    cout<<ans;
}