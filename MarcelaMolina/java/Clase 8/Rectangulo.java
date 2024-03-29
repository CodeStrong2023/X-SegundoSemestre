import java.util.Scanner;

public class Rectangulo {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingresar la longitud del lado 1: ");
        double lado1 = scanner.nextDouble();

        System.out.print("Ingresar la longitud del lado 2: ");
        double lado2 = scanner.nextDouble();

        double area = calcularArea(lado1, lado2); 
        double perimetro = calcularPerimetro(lado1, lado2);

        System.out.println("El área del rectángulo es: " + area);
        System.out.println("El perímetro del rectángulo es: " + perimetro);
        
        scanner.close();
    }

    public static double calcularArea(double lado1, double lado2){
        return lado1 * lado2; 
    }
    public static double calcularPerimetro(double lado1, double lado2){
        return 2 * (lado1 + lado2);
    }
    
}
