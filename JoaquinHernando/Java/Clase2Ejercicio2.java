package Java;
import javax.swing.JOptionPane ;
public class Clase2Ejercicio2 {
    public static void main(String[] args) {
        var numero = Integer.parseInt(JOptionPane.showInputDialog ("Digite un numero: "))  ;
        while(numero != 0) {
            if (numero > 0) {
                JOptionPane.showMessageDialog(null, "El numero "+numero+" es POSITIVO") ;
            }
            else {
                JOptionPane.showMessageDialog(null, "El numero "+numero+" es NEGATIVO") ;
            }
            System.out.println("Digite otro numero: ") ;
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: ")) ;
            }
            JOptionPane.showMessageDialog(null, "El numero "+numero+" finaliza el programa") ;
        }

    }
