// Olympiad Pizza

#include <iostream>
#include <vector>

using namespace std;

int main(){

vector<int> arr;
    arr.push_back(1);
    arr.push_back(3);
    arr.push_back(1);
    arr.push_back(4);

vector<int>res = vector<int>(4,0);

for(int i=0; i<res.size(); i++){
    cout<<res[i]<<" ";
}



return 0;
}