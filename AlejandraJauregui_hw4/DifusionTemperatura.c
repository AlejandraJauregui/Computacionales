#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int mod(int i, int j);

int main()
{
	/*Se definen variables*/

	float v = 10E-2;
	float Temp[100][100]; 
	float Tempant[100][100];	
	float dx = 1;
	float dt = 0.25;
	float r = dt*v/(dx*dx);
	int i;
	int j;
	int n;
       
    for(i=0;i<100;i++)
	{
		for(j=0;j<100;j++)
		{
			if((i>=20) && (i<40) && (j>=40) && (j<=60))
			{
				Temp[i][j] = 100;
                fprintf(T1,"%f",100.0);
                fprintf(T1,"%s"," ");
			}
			else
			{
				Temp[i][j] = 50;
                fprintf(T1,"%f",50.0);
                fprintf(T1,"%s"," ");
			}
		}

    fprintf(T1,"%s\n"," ");
}
    


return 0;

}

/*Caso 2 Periódicas*/
 FILE*T2=fopen("t2.txt","w+");
int Period(int time)
{
    for(t =0 ; t<time;t++)
    {
        for(i = 1;i<Long-1;i++)
        {
            for(j = 1;j<Long-1;j++)
            {
                  Tempant[i][j]=Temp[i][j];
                
                Temp[i][j]=Temp[i][j] - Temp[i][j] +Temp[i+1][j]+Temp[i][j-1]+Temp[i][j+1]); 
            }
                
        }
    }
}




/*Caso 3 Fijas*/
 FILE*T2=fopen("t2.txt","w+");

