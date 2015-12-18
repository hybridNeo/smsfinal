#include <iostream>
#include <cmath>
#include <cstdlib>
using namespace std;
/*
	Here the bomber and the fighter are in a dogfight and if the fighter jet gets in a 
	threshold distance of the bomber it wins, after a certain number of moves elapse, the
	bomber wins.
*/

//fighter bomber problem
int main(void){
	double threshDist = 50;
	//set the values of the bomber;
	double bomberX = 80;
	double bomberY = 0;
	//set the initial values of the fighter jet
	double fighterX = 0;
	double fighterY = 50;
	double d = 0;// set d value to 0
	int maxMoves = 6;
	int fighterVelo = 10;
	int savedMax = maxMoves;
	while(maxMoves--){
		srand(time(NULL));
		//cout << "Rand: " << rand() % 100 << endl;
		d = sqrt(pow(bomberY-fighterY,2)+pow(bomberX-fighterX,2));
		if( d <= threshDist){
			cout << "Bomber destroyed!!\n";
			cout << "Distance: " << d << endl;
			cout << "Move: " << savedMax - maxMoves << endl;
			break;
		}
		double sint = (bomberY-fighterY)/d;
		double cost = (bomberX-fighterX)/d;
		fighterX = fighterX+fighterVelo*cost;
		fighterY = fighterY+fighterVelo*sint;
		bomberX = rand() % 100 ;
		bomberY = rand() % 100 ;			
	}
	if( d > threshDist){
		cout << "Bomber escaped\n";
	}
}
