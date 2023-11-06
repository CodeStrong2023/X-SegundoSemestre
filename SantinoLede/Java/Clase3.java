/*
 Ejercicio 3
 */

package Ciclos03;

import java.util.Scanner;

public class Ciclos03 {
    public static void main(String[] args){
        Scanner entrada = new Scanner(System.in);
        int num;
        System.out.println("Ingrese un número ");
        num = Integer.parseInt(entrada.nextLine());
        while(num != 0){
            if(numero % 2 == 0){
                System.out.println("El numero es PAR");
            }
            else{
               System.out.println("El numero es IMPAR"); 
            }
            System.out.println("Ingrese otro número ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("El numero ingresado detiene el programa");
    }
    
}

/*
Ejercicio4
 */
package Ciclos04;

import java.util.Scanner;

public class Ciclos04 {
    public static void main(String[] args){
        Scanner entrada = new Scanner(System.in);
        int num, csum = 0;
        System.out.println("Ingrese un número ");
        num = Integer.parseInt(entrada.nextLine());
        while(num >= 0){
           System.out.println("El numero es positivo");
           csum++;
           System.out.println("Ingrese otro número ");
           num = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("Ingresó "+conteo+" numeros positivos");
    }
    
}

/*
Ejercicio5
 */
package Ciclos05;

import java.util.Scanner;

public class Ciclos05 {
    public static void main(String[] args){
        Scanner entrada = new Scanner(System.in);
        int num, rand, csum = 0;
        rand = (int) (Math.random()*100);
        do{
           System.out.println("Ingrese un número ");
           num = Integer.parseInt(entrada.nextLine());
           if(num < rand){
              System.out.println("El número es mayor"); 
           }
           else if(num < rand){
               System.out.println("Ingrese otro número");
           }
           else{
               System.out.println("Número correcto");     
           }
           csum++;
        }while(num != rand);
        System.out.println("Acertaste en "+conteo+" intentos");
    }
}
