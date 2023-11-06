/*
Ejercicio 6 
 */
package Ciclos06;

import java.util.Scanner;

public class Ciclos06 {
    public static void main(String[] args){
        Scanner entrada = new Scanner(System.in);
        int num,csum = 0;
        do{
            System.out.println("Ingrese un número ");
            num = Integer.parseInt(entrada.nextLine());
            csum+= num;
        }while(num != 0);
        System.out.println("La suma es: "+csum);
    }
}


/*
Ejercicio 7
 */
package Ciclos07;

import java.util.Scanner;

public class Ciclos07 {
    public static void main(String[] args){
        Scanner entrada = new Scanner(System.in);
        int num,csum = 0; 
        sum = 0;
        float mean = 0;
        System.out.println("Ingrese un número ");
        num = Integer.parseInt(entrada.nextLine());
        while(num >= 0){ 
            sum += num;
            csum++;
            System.out.println("Ingrese otro número ");
            num = Integer.parseInt(entrada.nextLine());
        }
        if(csum==0){
            System.out.println("No se puede dividir por 0");    
        }
        else{
            mean = (float)sum/csum;
            System.out.println("El promedio es: "+mean);
        }
    }
    
}