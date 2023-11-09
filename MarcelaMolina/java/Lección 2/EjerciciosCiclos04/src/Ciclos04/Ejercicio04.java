/*Ejercicio 4: Peedir números hasta que se teclee uno negativo y mostrar cuántos
números se han introducido. Lo hacemos primero con Scanner y luego con JOptionPane.
*/

package Ciclos04;
import javax.swing.JOptionPane;


public class Ejercicio04 {
    public static void main(String[] args){

        int numero , conteo = 0;
       numero= Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número: "));
       
        while(numero >=0){
             JOptionPane.showMessageDialog(null, "El número "+numero+" es POSITIVO");
             conteo++;
             numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese otro número: "));
        }
        JOptionPane.showMessageDialog(null,"Ha ingresado "+conteo+ " números que no son positivos");
    }
}


