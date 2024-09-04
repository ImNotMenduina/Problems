#include <iostream>

int fibonacci(int N) {
    if(N == 0 || N == 1)
        return 1;
    return fibonacci(N - 1) + fibonacci(N - 2);
}

int main() {
    //Q2
    int N = 0, fib;
    int Q;
    std::cin >> Q;
    while(true)
    {
        fib = fibonacci(N);

        if (fib >= Q)
            break;

        N++;
    }
    if (fib == Q)
        std::cout << Q << " está na sequencia de Fibonacci" << std::endl;
    else
        std::cout << Q << " não está na sequencia de Fibonacci" << std::endl;

    return 0;
}