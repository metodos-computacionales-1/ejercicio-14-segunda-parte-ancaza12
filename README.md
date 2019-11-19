# ejercicio-14-segunda-parte-ancaza12

1. La gráfica representa un oscilador armónico para lambda=1. Se obtienen gráficas compuestas de senos y cosenos para esta función.
2. Las soluciones esperadas van a ser valores tanto positivos como negativos de "y", ya que la función está compuesta de senos y cosenos.
3. Las gráficas de euler se encuentran por medio del 1.cpp 
4. Se logra observar una oscilación que inicia muy pequeña y va aumentando la amplitud de forma simetrica respecto al y[0] =0.
5. La oscilación que se observa en esta gráfica, no representa cambios de amplitud. Sin embargo sigue siendo una funcion compuesta de senos y cosenos.
6. La gráfica que se obtiene es de forma espiral para el caso de Euler y representa la relación que tienen los senos y cosenos. Para el caso de RK4 se obtiene una forma elíptica, ya que la relación entre ellas no varía de la forma en que hace con el método de Euler.

7. En 3.cpp se obtiene el codigo aplicando la friccion. 
8. Al variar el lambda, se obtiene que entre más grande es este valor, la gráfica se vuelve lineal y en cierto rango tiende a -inf. Al utilizar un lambda de valor 0.03 se observa un decaimiento de y[0] respecto al tiempo; en y[1] vs t se obtiene una relacion lineal negativa y para y[1] vs y[0] se obtiene un aumento no lineal. En estos casos se pierde la oscilación observada con el lambda=1.
