/*
 Ejercicio 1
 */

 package Ciclos01;

 public class Ciclos01 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, cuadrado;
        
        System.out.printIn("Escriba un número")
        numero = Integer.parseInt(entrada.nextLine())
        while (numero >=0) {
            cuadrado = (int)Math.pow(numero, 2);
            System.out.printIn("El número"+numero+" elevado al cuadrado es: "+cuadrado)
            System.out.printIn("Escriba otro número")
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.printIn("Programa finalizado")
    }
 }

 /*
  Ejercicio 2
  */

package Ciclos02;

import java.util.Scanner;

public class Ejercicio2 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner (System.in);
        System.out.printIn("Escriba un número")
        var numero = Integer.parseInt(entrada.nextLine())
        while (numero != 0) {
            if (numero > 0) {
                System.out.printIn("El número positivo");
            }
            else {
                System.out.printIn("El número es negativo");
            }
            System.out.printIn("Escriba otro número");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.printIn("Programa finazliado")
    }
}