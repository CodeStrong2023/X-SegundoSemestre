
package dominio;

public class Persona {
    //Atributos
    private String nombre;
    private double sueldo;
    private boolean eliminado;
    
    //Constructor
    public Persona(String nombre, double sueldo,boolean eliminado){
        this.nombre = nombre;
        this.sueldo = sueldo;
        this.eliminado = eliminado;   
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public double getSueldo() {
        return sueldo;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }

    public boolean isEliminado() {//en el boolean el get cambia por is,es como una pregunta es V o F
        return eliminado;
    }

    public void setEliminado(boolean eliminado) {
        this.eliminado = eliminado;
    }
    
 //Método toString permite imprimir el estado del objeto, los valores del atributo
//en cualquier momento. 
    public String toString(){
        return "Persona[nombre: "+this.nombre+
                ",sueldo: "+this.sueldo+
                ",eliminado: "+this.eliminado+" ]";
        
    }
}