//Codigo tomado de https://www.youtube.com/watch?v=UhZ1ESRR4OM

#include <iostream>
#include <cmath>
#include <fstream>
using namespace std;
void integralE(float tf,float dt, float w, float m, string datos);

int main(){
    float w = 50;
    float m=2;
    string datos= "euler.dat";
    integralE(20, 0.01, w,m, datos); 
    
    return 0;
}

void integralE(float tf,float dt, float w, float m, string datos){
    ofstream outfile;
    outfile.open(datos);      
    float x=1;
    float vE=0;

    for(float t=0; t<=tf;t+=dt){
        float xpr=x;
        float vEpr=vE;
        x= x + dt*vEpr;
        vE= vE + dt* (-w/m*xpr);
        outfile << t <<" "<< x<< " " << vE<< std::endl;
    }
    outfile.close();
}
