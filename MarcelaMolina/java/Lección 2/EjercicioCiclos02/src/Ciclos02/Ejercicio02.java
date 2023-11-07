/*
Ejercicio 2: Leer un número e indicar si es positivo o negativo. 
El proceso se repetira hasta que se introduzca un cero. 
*/
package Ciclos02;

import java.util.Scanner;

public class Ejercicio02 {

   
    public  static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
       System.out.println("Ingrese un número");
       var numero = Integer.parseInt("Ingrese un número: ");
       while(numero !=0){
           if(numero >0){
               System.out.println("El número " +numero+ " es POSITIVO");
           }
           else{
               System.out.println("El número " +numero+ " es NEGATIVO");
           }
           System.out.println("Ingrese otro número ");
           numero = Integer.parseInt(entrada.nextLine());
           
       }
       
        
    }
    
    
}
