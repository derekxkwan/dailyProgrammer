//2015-07-13 challenge #223 [easy] garland words

#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
class Garland{ 
		string input;
	public:
		Garland(string);
		int degree;
		string output;
};

Garland::Garland(string ipt){
	int len, i=1, lastPos;
	size_t pos;
	string sub, test;
	degree =0;
	input = ipt;
	transform(input.begin(), input.end(), input.begin(), ::tolower);
	len = input.length();
	test = input.substr(1,len);
	pos = 0;
	do{ lastPos = pos;
		sub = input.substr(0, i);
		pos = test.find(sub);
		i++;
	} while((pos < len)&&(i<len));
	if(((sub.length()-1) + (lastPos+1)) == len){
		degree = i-2;
	};
	if(degree > 0){
		string tackOn = input;
		string copy = input;
		tackOn.erase(0, degree);
		output = copy.append(tackOn);
		}
	else{
		output = "(none)";
	};
};

int main(int argc, char* argv[]){
	string cand;
	if(argc == 2){
		cand = string(argv[1]);
		
	Garland gar(cand);
	cout << "input: " << cand << ", degree: " << gar.degree << ", garland: "<< gar.output << endl;
	}
	else{
		cout << "Wrong number of arguments!" << endl;
	};
};
