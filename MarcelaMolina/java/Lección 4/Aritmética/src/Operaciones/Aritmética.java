
package Operaciones;

public class Aritmética {
    
    //Atributos de la clase 
    int a; //Las variables tienen asignado el valor de 0 por default
    int b;
    
    //El constructor es un método especial
    
    public Aritmética(){//Constructor 1 vacio
            System.out.println("Se está ejecutando el constructor número uno");
    }
    //Sobrecarga de constructores
    public Aritmética(int a, int b){ //Constructor 2
        this.a=a;
        this.b=b;
        System.out.println("Se está ejecutando el construcor número dos");
        
    }
    //Método
    public void sumarNumeros(){ 
       int resultado = a+ b;
       System.out.println("resultado = " +resultado);
    }
    
    public int sumarConRetorno(){
        //int resultado = a+b; //Se puede utilizar variable o 
        return a+b;
    }
    public int sumarConArgumentos(int a,int b){ //Las variables no pueden ser
        //tipo var de dentro de los parámetros o atributos tienen que ser int.
        
        this.a=a; //El argumento a se asigna al atribuo this.a
        this.b=b; //El uso del this es opcional
       // return a+b;
       return this.sumarConRetorno();
    }
    
    
   
    
            
}
