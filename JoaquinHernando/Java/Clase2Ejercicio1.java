package Java;
import java.util.Scanner ;
public class Clase2Ejercicio1 {

    public static void main(String[] args) {
        try (Scanner entrada = new Scanner(System.in)) {
            int numero, cuadrado;
            System.out.println("Digite un numero: ") ;
            numero = Integer.parseInt(entrada.nextLine()) ;
            while(numero >= 0) {
                cuadrado = (int)Math.pow(numero, 2) ;
                System.out.println("El numero "+numero+" elevado al cuadrado es: "+cuadrado) ;
                System.out.println("Digite otro numero: ") ;
                numero = Integer.parseInt(entrada.nextLine ()) ; 
            }
        } catch (NumberFormatException e) {
            e.printStackTrace();
        }
        System.out.println("El programa ha finalizado por numero negativo") ;
    }
}