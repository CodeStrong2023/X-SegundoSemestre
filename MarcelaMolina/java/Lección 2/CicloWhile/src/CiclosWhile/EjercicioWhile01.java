
package CiclosWhile;


public class EjercicioWhile01 {
    public static void main(String[] args){
        var conteo= 0; //Interferencia de tipos
        while(conteo < 7){
            System.out.println("conteo = "+ conteo);
            conteo++; //Se aumenta la variable en uno 
            //PARA CORRER EL PROGRAMA SE UTILIZA RUN FILE
        }
        
        var contador = 0;
        do {
            System.out.println("contador= " + contador);
            contador++;
        }while (contador <7);
        
        
        for(var contando=0 ; contando <7 ; contando++){
            if(contando % 2 == 0){ 
                System.out.println("contando=" + contando);
                break;
                //Toma el primer valor y al dar 0 entonces cierra el ciclo
                //Si break es comentado al correr el programa van a resultar 
                //los números pares por lo que fue establecido en la condición 
                
                
            }
        }
        
        for(var contando=0 ; contando <7 ; contando++){
            if(contando % 2 != 0){ 
                continue;
            }
             System.out.println("contando=" + contando);
        }
        
        //ETIQUETAS LABELS
        inicio:
         for(var contando=0 ; contando <7 ; contando++){
            if(contando % 2 == 0){ 
                System.out.println("contando=" + contando);
                break inicio;   
            }
        }
        inicio:
        for(var contando=0 ; contando <7 ; contando++){
            if(contando % 2 != 0){ 
                continue inicio;
            }
             System.out.println("contando=" + contando);
        }
    }
}


