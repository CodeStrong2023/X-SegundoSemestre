
package domain;

public class Empleado extends Persona{
    private int idEmpleado;
    private double sueldo;
    private static int contadorEmpleados; //Es para incrementar
    
    //Constructor 
    public Empleado(){
        this.idEmpleado = ++Empleado.contadorEmpleados;
    }

    public Empleado(String nombre,double sueldo) {
        //super(nombre);
        this(); //Se llama desde acá al constructor vacío(llamar al constructor interno)
        this.nombre = nombre;
        this.sueldo = sueldo;
    }

    
    public int getIdEmpleado() {
        return this.idEmpleado;
    }

    public void setIdEmpleado(int idEmpleado) {
        this.idEmpleado = idEmpleado;
    }

    public double getSueldo() {
        return this.sueldo;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Empleado{");
        sb.append("idEmpleado=").append(idEmpleado);
        sb.append(", sueldo=").append(sueldo);
        sb.append('}').append(super.toString());
        return sb.toString();
        //Con el método append se pueden modificar y agregar atributos
    }
    
    
   
    
}
