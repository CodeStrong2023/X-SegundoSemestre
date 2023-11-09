package Clases;

public class Persona {
    //Atributos de la clase(Características)
    public String nombre; //Cada atributo es de tipo público
    public String apellido;
    
    //Métodos de la clase(Acciones)
    public void obtenerInformacion(){
        System.out.println("Nombre: "+nombre);
        System.out.println("Apellido:"+apellido);
    }
  
}
