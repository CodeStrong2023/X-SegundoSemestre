/*
Ejercicio 11: Diseñar un programa que muestre producto de los 10 primeros
números impares. Hacerlo con JOptionPane. 
*/
package ciclos11;

import javax.swing.JOptionPane;

public class Ciclos11 {
    public static void main(String[] args) {
        long producto=1;//variable de tipo long
        for(int i=1; i <=20; i+=2){
            producto *=i;
        }
        JOptionPane.showMessageDialog(null, "El producto de los números impares es: "+producto);
        
        
    
    }
  
    
}
