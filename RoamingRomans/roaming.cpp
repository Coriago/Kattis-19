#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;
//Author: Gage Miller
//Date:   6/18/19   

//Input Area
double getIn(){
    double num;
    cin >> num;
    return num;
}

//Main Program
int main(){
    cout << std::setprecision(0) << fixed << round(getIn() * 5280000 / 4854);
    return 0;
}