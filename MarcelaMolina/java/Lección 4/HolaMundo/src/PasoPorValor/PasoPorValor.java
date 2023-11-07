
package PasoPorValor;

public class PasoPorValor {
    public static void main(String[] args) {
      var valorX = 20;
        System.out.println("valorX = "+valorX);
        cambioValor(valorX);//Solo le enviamos una copia 
        System.out.println("valorX = "+valorX);
    }
    //El parámetro por valor no tiene el poder de retornar un valor dentro
    //del espacio de memoria
    
    public static void cambioValor(int arg1){//Parámetros por valor
        System.out.println("arg1 = " +arg1);
        
    }
}
