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
	int buckets[10] = {0};
	int expected = n/10;
	for(int i=0;i<n;++i){
		buckets[(int)(v[i]*10)]++;
	}
	double sum = 0.0;
	for(int i =0 ;i < 10;++i){
		cout << buckets[i] << endl;
		int oi = buckets[i];
		sum+= pow(oi-expected,2)/expected;
	}
	cout << "Chi-Square value = " << sum << endl;
	cout << "Chi-Square at 0.05 and 10 buckets = 16.9 \n";
	if(sum > 16.9)
		cout << "Rejected" << endl;
	else
		cout << "Accepted" << endl;
}
int main(void){
	cout << "How many random numbers do you want" << endl;
	int n;
	cin >> n;
	vector<float> nums;
	generate(nums,n);
	validate(nums,n);
	

}
