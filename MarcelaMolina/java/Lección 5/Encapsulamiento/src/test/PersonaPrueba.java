
package test;
import dominio.Persona;
public class PersonaPrueba {
    public static void main(String[] args) {
       Persona persona1 = new Persona("Osvaldo",57.000,false);
        System.out.println("persona1 su nombre es: "+persona1.getNombre());
       //Modificación a través de métodos
       persona1.setNombre("Juan Ignacio");
       
       //persona1.nombre = "Juan Ignacio"; //Ya no se puede utilizar
        //System.out.println("El nombre es: "+persona1.nombre); Tampoco se accede así al atributo
        
        System.out.println("persona1 con su nombre modificado: "+persona1.getNombre());
        System.out.println("persona1 el resultado para el sueldo: "+persona1.getSueldo());
        System.out.println("persona1 para obtener el booleano: "+persona1.isEliminado());
        
        //Tarea: Crear otro tipo de persona, asignar valores de manera inicial
        //imprimir, volver a modificar sus valores y luego volver a imprimir. 
        
        System.out.println("persona1: "+persona1.toString());
        
    }
}


