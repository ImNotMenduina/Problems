#include<iostream>

using namespace std;

int main() {
    std::string s; getline(cin, s);

    cout << "string original : " << s << endl;

    int tam = s.length();
    int trocas = tam / 2;
    for (int i=0; i<trocas; i++) {
        char temp;
        temp = s[tam-1-i];
        s[tam-1-i] = s[i];
        s[i] = temp;
    }   

    cout << "string invertida : " << s << endl;
    
    return 0;
}