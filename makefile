ecuaciones.png : euler.dat rk4.dat fric.dat ej14.py
	python ej14.py
    
euler.dat : 1.x
	./1.x > euler.dat
    
rk4.dat : 2.x
	./2.x > rk4.dat
 
fric.dat : 3.x
	./3.x > fric.dat
    
1.x : 1.cpp
	c++ 1.cpp -o 1.x

2.x : 2.cpp
	c++ 2.cpp -o 2.x
   
3.x : 3.cpp
	c++ 3.cpp -o 3.x
    
clean:
	rm -rf 1.x 2.x 3.x euler.dat rk4.dat fric.dat ecuaciones.png