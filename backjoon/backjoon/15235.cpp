//
//  15235.cpp
//  backjoon
//
//  Created by 김하영 on 2020/11/29.
//

#include <iostream>
#include <vector>

using namespace std;

void solution(vector<int>* arr, int n){
    vector<int> result = vector<int>(n, 0);
    int cnt = 0;
    for(vector<int>::iterator it = arr->begin(); it != arr->end(); ++it){
        cout<<*it<<endl;
    }
    
    int i=0;
    
    while(arr->size()>0){
        cnt++;
        if(arr->at(i) == 1){
            result[i]=cnt;
            arr->erase(i);
        }
    }
}

int main(){
    
    cout<<"hello cpp"<<endl;
    vector<int> arr;
    int n;
    cin>>n; // get size of members
    int temp;
    for(int i=0; i<n; i++){ //get num of slices per constant
        cin>>temp;
        arr.push_back(temp);
    }
    
    solution(&arr,n);
    
    
    return 0;
}
