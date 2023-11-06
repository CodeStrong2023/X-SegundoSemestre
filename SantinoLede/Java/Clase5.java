/*
Ejercicio8
 */
package Ciclo08;

import java.util.Scanner;

public class Ciclo08 {
    public static void main(String[] args){
        Scanner entrada = new Scanner(System.in);
        System.out.println("Escriba un número ");
        int num = Integer.parseInt(entrada.nextLine());
        int i = 1;
        while( i <= numero){
            System.out.println(i);
            i++;
        }
    }   
}

/*
Ejercicio8 
 */
package Ciclo08;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class Ejercicio08 {
    public static void main(String[] args){
        int num = Integer.parseInt(JOptionPane.showInputDialog("Escriba un número "));
        int i = 1;
        while( i <= num){
            JOptionPane.showMessageDialog(null, 1);
            i++;
        }
    }   
}