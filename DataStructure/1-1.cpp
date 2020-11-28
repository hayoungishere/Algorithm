#include <iostream>
#include <string>
#include <utility>

using namespace std;

bool isUnique(string str){

    if(str.length()>26) return false; //a-z 26개만 존재, 문자열의 길이가 26보다 크다는 것은 무조건 중복이 있다는 것

    int checkN=0;
    for(int i=0; i<str.length(); i++){
        int cur = str.at(i)-'a';
        if((checkN & (1<<cur))>0) return false;

        checkN |= (1<<cur);
    }

    return true;
}
int main(){

    if(isUnique("hello")){
        cout<<"TRUE";
    }else{
        cout<<"FALSE";
    }
    return 0;
}