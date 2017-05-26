#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include<time.h>

//Se declaran las variables generales y la función fun

double fun(double x, double y);
double ant;
int total = 0;
int i;
int j;
int k;
double xi[84];
double yi[84];


int main(void){
    
    FILE *fun1;
    FILE *fun2;
    
    double x = -1.8;
    double y = 7.5;
    double rx = 0;
    double ry = 0;
    double xnuevo = 0;
    double ynuevo = 0;

    double nx = 0;
    double ny = 0;
    int test;
    double xii;
    double yii;
    
//Se declara una semilla para tomar datos aleatorios
    
   	srand((unsigned) time(NULL));

//Se selecciona el archivo que se lee y el que se va a escribir con las primeras respuestas.
    
    FILE *par1=fopen("1rta.txt","w+");   	
    fun1=fopen("Canal_ionico.txt", "r");
    
//Se cargan los datos

i=0;
    for (i=0; i<42;i++)
    {
        fscanf(fun1,"%lf %lf\n", &xii, &yii);
        xi[i] = xii;
        yi[i] = yii;
        
          //printf("%f %f\n", xi[i], yi[i]);
    } 
    total = 84;
    
    
//Comienza el primer método y guarda todos los resultados obtenidos en un archivo "resultados1.txt" 
    
    int iter = 200000;
    
    FILE *out=fopen("resultados1.txt","w+");
    
    for(i = 0; i<iter;i++){
        
          fprintf(par1, "%f %f\n", x, y);
        
            nx= drand48()*2-1.0;
            ny= drand48()*2-1.0;
        
            xnuevo = x + 0.3*nx;
            ynuevo = y + 0.3*ny;
        
          double alfa = fun(xnuevo,ynuevo)/fun(x,y) ;
        
            if(alfa >1){
                               x = xnuevo;
                               y = ynuevo;
                               rx = x;
                               ry = y;
                               }
            else{
                 ant = (double)rand()/RAND_MAX;
                 if(ant>alfa){
                               x = xnuevo;
                               y = ynuevo;
                                  }
                 }
        
//Se imprimen los resultados en la consola y en resultados1.txt con el orden de x|y|r
         fprintf(out,"%f %f %f\n", xnuevo,ynuevo, fun(xnuevo,ynuevo));	
          }



printf("rta = %f %f %f\n", xnuevo,ynuevo, fun(xnuevo,ynuevo));
    
//Se repite el mismo método pero ahora para el caso del otro archivo "Canal_ionico1.txt"
    
x = 0;
y = 0;
rx = 0;
ry = 0;
total = 0;
xnuevo = 0;
ynuevo = 0;
    
//Se selecciona el archivo que se lee y el que se va a escribir con las segundas respuestas.
    
   	FILE *par2=fopen("2rta.txt","w+"); 
    fun2=fopen("Canal_ionico1.txt", "r");
    
//Se cargan los datos
    i=0;
    for (i=0; i<42;i++)
    {
        fscanf(fun2,"%lf %lf\n", &xii, &yii);
        xi[i] = xii;
        yi[i] = yii;
        
          //printf("%f %f\n", xi[i], yi[i]);
    } 
    total = 84;

    
 //se usa de nuevo el primer método pero guarda todos los resultados obtenidos en un archivo "resultados2.txt" 
         
    iter = 200000;
    FILE *out2=fopen("resultados2.txt","w+");  
    for(i = 0; i<iter;i++){
          fprintf(par2, "%f %f\n", x, y);
          
        
        nx= ((double)rand()/(double)RAND_MAX)*2-1.0;
        ny = ((double)rand()/(double)RAND_MAX)*2-1.0;
        
        xnuevo = x + 0.3*nx;
        ynuevo = y + 0.3*ny;
     
          double alfa = fun(xnuevo,ynuevo)/fun(x,y) ;
            if(alfa >1){
                               x = xnuevo;
                               y = ynuevo;
                               rx = x;
                               ry = y;
                               }
            else{
                 ant = (double)rand()/RAND_MAX;
                 if(ant>alfa){
                               x = xnuevo;
                               y = ynuevo;
                                  }
                 }
    //Se imprimen los resultados en la consola y en resultados2.txt con el orden de x|y|r
        
         fprintf(out2,"%f %f %f\n", xnuevo,ynuevo, fun(xnuevo,ynuevo));		

          }
    

printf("rta = %f %f %f\n", xnuevo,ynuevo, fun(xnuevo,ynuevo));

}



//La función fun, usa la forma en que se calcula el radio 
double fun(double x, double y){
       ant = 0;
       double rta = (double)RAND_MAX;
       for(k = 0;k<total/2;k++){
             ant = sqrt( pow((x-xi[k]),2) + pow((y-yi[k]),2))-1;
//             printf("ant = %f\n", ant);
             if(ant<rta){
                       rta = ant;
                       }
             }
       return rta;
       }



     



