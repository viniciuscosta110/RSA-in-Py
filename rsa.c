#include <stdio.h>

int MDC(int p, int x)
{
    if(x == 0)
        return p;
    else
        return MDC(x, p % x);
}

int main(void)
{
    int p = 101701;
    int q = 101719;
    int n = p * q;
    int totiente_n = ((p - 1) * (q - 1));
    
    

    return 0;
}
