package Java;
import javax.swing.JOptionPane ;
public class Clase4Ejercicio1 {
    public static void main(String[] args) {
        int numero, suma = 0 ;
        do {
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero, con el numero 0 finaliza la suma: ")) ;
            suma += numero ;
        }while(numero != 0) ;
        JOptionPane.showMessageDialog(null, "La suma de todos los numeros ingresados es: "+suma) ;
    }
}
