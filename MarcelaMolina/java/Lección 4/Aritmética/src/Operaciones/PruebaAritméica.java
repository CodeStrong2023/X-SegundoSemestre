
package Operaciones;

public class PruebaAritméica {
    public static void main(String[] args) {
        Aritmética aritmetica1 = new Aritmética(); //El alcance de un atributo con el new es superior
        aritmetica1.a=3;//variabls locales
        aritmetica1.b=7;//Memoria stack
        miMétodo();//Se lo llama así al nuevo método
        aritmetica1.sumarNumeros();
        //Para almacenar un objeto o los atributos se utiliza la memoria heap
        
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " +resultado);   
        
        resultado = aritmetica1.sumarConArgumentos(12,26);
        System.out.println("Resultado usando argumemtos = "+resultado);
        
        
        System.out.println("aritmetica1 a: " +aritmetica1.a);
        System.out.println("aritmetica1 b: " +aritmetica1.b);
        
        Aritmética aritmetica2= new Aritmética(5,8);
        System.out.println("aritmetica2 = " +aritmetica2.a);
        System.out.println("aritmetica2 = " +aritmetica2.b);
        //aritmetica1=null,nunca utilizar esto
        //System.gc(); método para limpiar residuos, es pesado, se recomienda 
        //no usar.
        Persona persona = new Persona("Marcela", "Molina");
        System.out.println("persona = "+persona);
        System.out.println("Persona nombre: "+persona.nombre);
        System.out.println("Persona apellido: "+persona.apellido);
        
    }
    
     //Modularidad creamos un nuevo método
    public static void miMétodo(){
        //a = 10; //La variable a no tiene alcance del método main a miMetodo
        System.out.println("Aquí hay otro método");
    }
    
}
//CREAMOS UNA NUEVA CLASE
//Para crear una clase dentro de otra, solo una puede ser de tipo pública. Se le
//asigna un modificador de acceso "default" o "package". 

class Persona{ //A esta clase solo se puede acceder dentro del mismo paquete
    String nombre;
    String apellido;
    
    Persona(String nombre, String appellido){ //Constructor
       super(); //Llamada al constructor de la clase Padre object
        //Imprimir imprimir = new Imprimir();
        new Imprimir().imprimir(this);
        this.nombre = nombre;
        this.apellido = apellido;
        
        System.out.println("Objeto persona usando this: "+this);  
    }  
}

class Imprimir{
    public Imprimir(){
        super(); //construcor de la clase padre para reservar memoria
    }
    public void imprimir(Persona persona){
        System.out.println("Persona desde la clase imprimir: "+persona);
        System.out.println("Impresión del objeto actual (this): "+this);
    }
}

