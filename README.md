# Deutsch-Jozsa-algorithm

Este programa busca implemetnar el algoritmo de Deutsch-josza en computacion clasica.

En este caso nos damos cuenta de la poca eficiencia que hay al tratar de aplicar este algoritmo mediante mas grande se hace el tamaño del problema, el n maximo que mi maquina
fue capaz de computar sin problemas fue cuando n = 4, lo que hace que el tamaño maximo del problema que pude computar fuera de 2^(2^(4)) = 65536, cualquier n mayor generaria un
salto en la cantidad de funciones exagerado siendo que cuando n = 5, el total de las mismas seria de 4294967296.

Viendo este resultado y los tiempos de ejecucion nos damos cuenta de la ventaja que se obtiene al utilizar un computador cuantico a la hora de cumplir con estas tareas en especifico.

Todo el codigo esta documentado, pero ademas quiero añadir que una parte del mismo esta basada en el proyecto de github: https://github.com/MyEntangled/MyEntangled-Blog/blob/master/Quantum%20Programming%20Projects/Deutsch-Jozsa%20algorithm.ipynb

Solo queda añadir que la unica libreria necesaria para correr el programa es numpy.
