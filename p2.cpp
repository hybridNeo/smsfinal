#include <iostream>
#include <cstdlib>
using namespace std;
class Row{
	public:
	int at;
	int nbegin;
	int nst;
	int nend;
	int nit;
	int nwait;
	int dbegin;
	int dst;
	int dwait;
	int dend;
	int dit;
	int total;	
};
int max(int a,int b){
	if(a>b)
		return a;
	else
		return b;
}
int getST();
int getIAT();
void initRow(Row& first){
	cout << "AT -- NBT -- NEnd -- NWait -- DBegin -- DEND -- Dwait -- Total -- DIT -- NIT\n";
	first.at = 0;
	first.nbegin = 0;
	first.nst = getST();
	first.nend = first.nst;
	first.nwait = 0;
	first.dbegin = first.nend;
	first.dst = getST();
	first.dit = 0;
	first.nit = 0;
	first.dwait = 0;
	first.dend = first.dbegin + first.dst;
	first.total = first.dend;		
	cout << first.at << " ----- " << first.nbegin << " ----- " << first.nend << " ----- " << first.nwait<< " ----- " << first.dbegin << " ----- " << first.dend << " ----- "<< first.dwait <<" ----- "<< first.total << " ----- " << first.dit << " ----- " << first.nit << endl;
}
int main(void){
	int n = 10;
	Row rows[n];
	int wtp = 0;
	int wtn = 0;
	int wtd = 0;
	initRow(rows[0]);
	for(int i = 1; i < n;++i){
		rows[i].at = rows[i-1].at + getIAT();
		rows[i].nbegin = max(rows[i].at,rows[i-1].nend);
		rows[i].nst = getST();
		rows[i].nend = rows[i].nbegin + rows[i].nst;
		int wait =  rows[i].nbegin -rows[i].at 	;
		rows[i].nwait = 0;
		rows[i].dwait = 0;
		rows[i].dit = 0;
		rows[i].nit = 0;
		if(wait > 0){
			rows[i].nwait = wait;
		}
		rows[i].dbegin = max(rows[i].nend,rows[i-1].dend);
		rows[i].dst = getST();
		wait =  rows[i].nbegin - rows[i-1].nend ;
		if(wait > 0){
			rows[i].nit = wait;
		}
		rows[i].dend = rows[i].dbegin + rows[i].dst;
		wait =  rows[i].dbegin-rows[i-1].dend ;
		if(wait > 0){
			rows[i].dwait = wait;
		}
		wait = rows[i-1].dend - rows[i].dbegin;
		if(wait > 0){
			rows[i].dit = wait;
		}
		wtp+= rows[i].nwait + rows[i].dwait;
		wtd += rows[i].dit;
		wtn += rows[i].nit;
		rows[i].total = rows[i].dend - rows[i].at;
		cout << rows[i].at << " ----- " << rows[i].nbegin << " ----- " << rows[i].nend << " ----- " << rows[i].nwait<< " ----- " << rows[i].dbegin << " ----- " << rows[i].dend << " ----- "<< rows[i].dwait <<" ----- "<< rows[i].total << " ----- " << rows[i].dit << " ----- " << rows[i].nit << endl;
	}
	cout << "avg waiting time --- person " << wtp/n << endl << "doctor: " << wtd/n << endl << "Nurse: " << wtn/n <<endl;
}


int getST(){
	return rand() % 12;
}
int getIAT(){
	return rand() % 15;
}
