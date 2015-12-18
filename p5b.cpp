#include <iostream>
#include <cstdlib>
#include <vector>
#include <cmath>
using namespace std;
int abs(int a){
	if(a < 0 )
		a = -a;
	return a;
}
void generate(vector<float>& v,int n){
	int a = 16807;
	int m = 2147483647;
	int c = 0;
	srand(time(NULL));
	int seed = rand()%20;
	for(int i = 0;i < n;++i){
		seed = abs((a*seed+c)%m);
		v.push_back(seed/(float)m);
	}
}
void validate(vector<float>& v,int n){
	float dminus=0;
	float dplus=0;
	for (int i = 0; i < n; ++i)
	{
		float temp = i/(float)n - v[i];
		if(temp> dplus)
			dplus = temp;
	}
	for (int i = 0; i < n; ++i)
	{
		float temp = v[i] - ((i-1)/(float)n);
		if(temp> dminus)
			dminus = temp;
	}
	cout << max(dminus,dplus) << endl;
}
int main(void){
	cout << "How many random numbers do you want" << endl;
	int n;
	cin >> n;
	vector<float> nums;
	generate(nums,n);
	validate(nums,n);
	

}
