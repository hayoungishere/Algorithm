#include <iostream>
#include <string>

using namespace std;

void reverse(char * str){
    char* end = str;
    char temp;

    if(str){
        while(*end){
            ++end;
        }
    }
    --end;

    while(str<end){
        temp = *str;
        *str++ = *end;
        *end-- = temp;
    }
}

int main(){
    char str[] = "hello world";
    
    reverse(str);
    cout<<str;
    
    return 0;
}