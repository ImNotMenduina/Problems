#include <iostream>

using namespace std;

int main() {
    //Q1
    int INDICE = 13, SOMA = 0, K = 0;
    
    while(K < INDICE) {
        K++;
        SOMA += K;
    }

    std::cout << SOMA << std::endl;

    return 0;
}