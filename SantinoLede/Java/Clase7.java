/*
Ejercicio 11
 */
package ciclos11;

import javax.swing.JOptionPane;

public class Ciclos11 {
    public static void main(String args[]){
        long producto = 1;
        for(int i = 1; i<=20;i+=2) {
            producto *= i;
        }
        JOptionPane.showMessageDialog("La solución de los números dados es "+producto);
    }
    
}

/*
Ejercicio 12
 */

package ciclos12;

import javax.swing.JOptionPane;