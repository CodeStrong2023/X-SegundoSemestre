/*
Ejercicio 4: Peedir números hasta que se teclee uno negativo y mostrar cuántos
números se han introducido. Lo hacemos primero con Scanner y luego con JOptionPane.
 */
package Ciclos04;

import java.util.Scanner;

public class Ciclos04 {
    public static void main(String[] args){
        Scanner entrada = new Scanner(System.in);
        int numero,conteo = 0;
        System.out.println("Ingrese un número: ");
        numero = Integer.parseInt(entrada.nextLine());
        while(numero >=0){
            System.out.println("El número "+numero+" es POSITIVO");
            conteo++;
            System.out.println("Ingrese otro número: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("Ha ingresado "+conteo+ " numeros que no son negativos");
        
        
    }
}
