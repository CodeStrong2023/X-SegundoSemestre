package Java;
import domain.Persona ;
public class Clase8Ejercicio1 {
    private int contador ;
    public static void main(String[] args) {
        Persona persona1 = new Persona("Ariel") ;
        System.out.println("Persona 1 = "+ persona1);
        Persona persona2 = new Persona("Naty") ;
        System.out.println("Persona 2 = " +persona2);
        imprimir(persona1) ;
        imprimir(persona2) ;
        this.contador = 10 ;
        PersonaPrueba personaP1 = new PersonaPrueba() ;
        System.out.println(personaP1.getContador());
    }
    static public void imprimir (Persona persona) {
        System.out.println("Persona = " + persona) ;
    }

    public int getCOntador() {
        imprimir(new Persona("Liliana")) ;
        return this.contador ;
    }
}
