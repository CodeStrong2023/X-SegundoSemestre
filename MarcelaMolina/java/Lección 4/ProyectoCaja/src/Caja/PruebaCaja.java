
package Caja;

public class PruebaCaja {
    public static void main(String[] args) {
        //Variables locales
        int medidaAncho=150;
        int medidaAlto=220;
        int medidaProf=600;
        
        Caja caja1 = new Caja(); //Instanciamos el objeto, constructor vacío
        caja1.ancho = medidaAncho; //Le pasamos los valores al objeto
        caja1.alto = medidaAlto;
        caja1.profundo = medidaProf;
        
        int resultado = caja1.calcularVolumen(); //Llamamos al método
        
        //Primer resultado 
        System.out.println("Resultado volumen de caja 1: "+resultado+ " mm");
        
        Caja caja2 = new Caja(250,140,260); //Llamamos al constructor 
        //2 con nuevos argumentos
        //Llamamos con el nuevo objeto al método para un nuevo cálculo
        System.out.println("Resultado volumen de caja 2: "+caja2.calcularVolumen()+" mm");
        
        
    }
    
}
