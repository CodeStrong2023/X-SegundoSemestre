/*
Ejercicio1: Leer 5 numeros, guardalos en un arreglo 
y mostrar en el orden inverso al introducirlos.
 */
package arreglos;

import java.util.Scanner;

public class Ejercicio2 {

    private static String[] numeros;
      public static void main(String[] args){
        Scanner entrada = new Scanner(System.in);
        float[] arreglos = new float[5];
        
        System.out.println("Guardando los datos en el arreglo");
        for(int i=0;i<5;i++){
            System.out.print((i+1)+".Digite un numero: ");
            arreglos[i] = entrada.nextFloat();       
        }
        
        System.out.println("\nImprimir los elementos del arreglo");
        for(int i=4;i>=0;i--){
            System.out.print(" "+numeros[i]);
        }
        System.out.println("\n");  
    }  
    
}
