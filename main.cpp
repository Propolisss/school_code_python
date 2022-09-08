#include <iostream>
#include <math.h>
using namespace std;
 
bool simple (int n) {
 if (n<2) return 0;
 if (n<4) return 1;
 for (int i=2; i<=floor(sqrt((float)n)); i++) if (n%i==0) return 0;
 return 1;
}
 
int main () {
 int a,b, count = 0;
 a = 1000;
 b = 10000;
 for (int i=a; i<=b; i++) if (simple(i) && simple(i+2)) count++;
 cout << count;
 cout << endl;
 system("pause");
 return 0;
}