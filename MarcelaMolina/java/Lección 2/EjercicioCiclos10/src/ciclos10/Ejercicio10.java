/*
Ejercicio 10: Pedir 10 números y escribir la suma. 
*/
package ciclos10;

import javax.swing.JOptionPane;

public class Ejercicio10 {
    public static void main(String[] args) {
        int numero,suma=0;
        for(int i = 1; i <= 10; i++){
            System.out.println("Ingrese un número");
            numero= Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número"));
            suma +=numero;   
        }
        JOptionPane.showMessageDialog(null, "La suma de todos los números es: "+suma);
    }
        
}
