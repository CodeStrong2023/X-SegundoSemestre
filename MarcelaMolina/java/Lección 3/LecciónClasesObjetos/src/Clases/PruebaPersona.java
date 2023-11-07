
package Clases;

public class PruebaPersona {
    public static void main(String[] args) {
        Persona persona1;
        persona1 = new Persona(); //Llamamos al constructor 
        persona1.nombre = "Marcela";
        persona1.apellido = "Molina";
        persona1.obtenerInformacion();
        
       Persona persona2=new Persona();
       System.out.println("persona2 = "+persona2);
       System.out.println("persona1 = "+persona1);
       persona2.obtenerInformacion();
       //Cada objeto tiene su propia información
       persona2.nombre= "Osvaldo";
       persona2.apellido="Giordanini";
       persona2.obtenerInformacion();
    }
    
}
