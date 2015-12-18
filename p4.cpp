#include <iostream>
#include <cstdlib>
using namespace std;
int abs(int a){
	if(a < 0 )
		a = -a;
	return a;
}
int main(void){
	int a = 16807;
	int m = 2147483647;
	int c = 0;
	cout << "How many random numbers do you want" << endl;
	int n;
	srand(time(NULL));
	cin >> n;
	int seed = rand()%20;
	while(n--){
		cout << seed/(float)m << endl;
		seed = abs((a*seed+c)%m);
	}

}
