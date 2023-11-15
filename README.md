# Herramientas-parcial
## Ricardo Perez(rpr9805) - Juan Jose Aguilar(JustRanm) - Luis Ponce(LPonce1305)
### Archivo de Phyton
*Inicialmente tenemos el menu que fue elaborado para saber lo que deseaba hacer el usuario teniendo 3 diferentes opciones, la palabra, el caracter y la salida del programa tras explicar cada una se da la opcion de elegir al usuario dentro de un ciclo while, para que siga sucediendo hasta que este decida darlo por terminado eligiendo 3, cualquier otra eleccion seguira el programa, 1 y 2 lo llevara a la carpeta Operetions y cualquier otro numero sera tomado como no valido y se repetira el ciclo*

![image](https://github.com/JustRanm/Herramientas-parcial/assets/147516960/42ac91ba-7345-42f1-acde-e7737749aeb0)

## FUNCIONAMIENTO DEL CÓDIGO

Este programa se encarga de recibir una  palabra o letra, mostrar esta misma en Código ASCII y la equivalencia del Código ASCII en binarios, para ello se dieron dos pestañas, en la primera se Encuentra “Operetors” en la cual se encuentran las funciones para sacar el Código ASCII de cada letra como su numero binario y abra otra función que juntara las demás para dar la impresión del mensaje correspondiente, la otra pestaña “main” se encuentra el menú, a continuación se explicara cada función detalladamente.


![image](https://github.com/JustRanm/Herramientas-parcial/assets/147520340/66c5e922-8f0c-4978-a5ea-baec9173b57b)

La primera función “ASCII_code” se encarga de mostrar la equivalencia de la letra en codigo ASCII, esta recibe como parámetro una letra y retorna el numero ASCII de dicha letra. La segunda función 
“Binarie_number” se encarga de convertir el numero ASCII en binario, para ello recibe como parámetro este numero y retorna el numero binario de dicho número, el “[2:]” se encarga de eliminar el “0b” que viene por defecto con el método bin que retorna el numero binario con esa adicción, al final la función retorna el numero binario de dicho número sin el “0b”.

![image](https://github.com/JustRanm/Herramientas-parcial/assets/147520340/cdc90055-1770-4bc7-a027-5ee3b3cc7f23)

La funcion “Result” Se encarga de coger todos los valores para imprimirlos por pantalla, en primer lugar se crearon dos listas, “Results” para guardar los valores de la letra, numero ASCII y numero binario y “Binarios_lista” para guardar los números binarios, esta función recibe como parámetro la palabra ingresada por el usuario, el primer for se encarga de coger cada letra de esa palabra y almacenarla en character por cada iteración, creando las variables Ascii y Binarios que llaman a sus funciones correspondientes con el  parámetro de la letra de la iteración, para luego con el Results.append  guardar dichos valores en la lista, al igual que Binarios_lista.append el cual guarda cada valor de binarios, dicho bucle se repite por cada letra de la palabra. El siguiente for se encarga recorre la lista de listas de Results, por cada iteración se toma una lista de adentro en donde se encuentran los tres valores, letras, ASCII y binario, por ello después para la impresión del mensaje se toman estos valores mediante las posiciones dentro de la lista en la que se encuentra dicha iteración usando uwu[0] que representa la letra de esa lista, uwu[1] el numero ASCII y uwu[2] el numero binario finalmente se crea otra variable Binaries la cual imprime el mensaje usando la lista Binarios_lista separándola con espacios con el método join, esta función retorna la impresión de print y Binaries.

## RESULTADOS

Ahora con todo el código completo podemos pasar a los resultados, abrimos el archivo main.py en donde encontraremos la pantalla principal. Tendremos las opciones 1) word 2) character 3) exit, para nuestra primera opción, tenemos el word, que funciona solo cuando queramos conocer el código en binario ASCII de una palabra especifica. Por ejemplo, usemos la palabra Batman, el primer paso seria presionar 1 y enter, el programa te pedira la palabra que quieras conocer, como ya mencionamos decidimos que la palabra será Batman. 

![image](https://github.com/JustRanm/Herramientas-parcial/assets/147520340/31549c61-8ca3-4abd-b2b4-66dd2c9c6372)

Como se puede apreciar, aparece el número al que pertenece la letra en el código ASCII, mostrando letra por letra y su respectivo número en binario trabajando con una cantidad de 8 bits. Así, con cada letra de Batman, y al final da un total que representa todos los números en binario en orden para escribir Batman en binario. Por ultimo, podemos seleccionar nuevamente una opcion de las ya mencionadas.

Ahora, con la segunda opción character encontraremos el valor en binario según el código ASCII de la letra que deseemos, para este caso usaremos la letra B y comparandola con la b. Para usar esta función solo tenemos que apretar el número 2, escribir la letra que deseamos conocer, usaremos primero la B. 

![image](https://github.com/JustRanm/Herramientas-parcial/assets/147520340/e160100d-0617-4753-8888-c2ed694a2f13)

Así vemos como muestra la posicion de la letra B en el código ASCII y su escritura en binario. Bien, ahora probemos con la letra b, aplicamos nuevamente los pasos previamente mencionados. 

![image](https://github.com/JustRanm/Herramientas-parcial/assets/147520340/1c2bcdb2-1a34-4751-93e7-bf75199fca4c)

Y ahora podemos ver como escribe la posicion de la b en el código ASCII 





