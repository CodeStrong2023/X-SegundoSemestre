/*
Ejercicio 7: Pedir números hasta qu se introduzca uno negativo y 
calcular la media. 
*/
package Ciclos07;

import javax.swing.JOptionPane;


public class Ejercicio07 {
    public static void main(String[] args) {
        int numero, conteo =0, suma= 0;
        float promedio =0;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número: "));
        while(numero >=0 ){ //Mientras el númeero no sea negativo 
            suma +=numero;
            conteo++;
            System.out.println("Ingrese un número: ");
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese otro número: "));   
        }
        if (conteo ==0){
            JOptionPane.showInputDialog("\nError, La división entre cero no existe");
        }
        else{
            promedio= (float)suma/conteo;
            JOptionPane.showInputDialog("\nEl promedio es:"+promedio);
        }
    }
}
