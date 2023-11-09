/*
Uso de la palabra Final
Tiene diferentes significados dependiendo de donde se aplique: 
variables: evita cambiar el valor que almacena la variable
métodos: evita que se modifique la definición o el comportamiento de un método
           desde una subclase
clase: evita que se creen clases hijas
Otra característica es que cuando se trabaja con variables se combina con el
modificador de acceso estático para convertir una variable en una constante, 
es decir, que no se puede modificar su valor. En la clase Math en la cual todos
sus atributos son de tipo static y final, es por esto que la variable pi* se 
conoce como una constante. 
*/

package test;

import domain.Persona;


public class TestFinal {
    public static void main(String[] args) {
        final int miDni = 39555278;
        System.out.println("miDni = " + miDni);
        //miDni = 25639885; no se puede modificar el valor de la variable 
        //Persona.CONSTANTE_AQUI=9; //No se modifica
        System.out.println("Mi atributo constante es: "+Persona.CONSTANTE_AQUI);
        
        final Persona persona1 = new Persona();
        //persona1 = new Persona(); //No se puede asignar una nueva referencia
        //pero si el contenido del objeto
        persona1.setNombre("Marcela Molina");
        System.out.println("persona1 nombre = " + persona1.getNombre());
        
        persona1.setNombre("Liliana");
        System.out.println("persona1 nombre = " + persona1.getNombre());
        
    }
    
    
}
