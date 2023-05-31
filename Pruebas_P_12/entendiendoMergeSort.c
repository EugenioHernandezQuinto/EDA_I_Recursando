/* Implementación de Merge sort */
#include <stdio.h>
#include <stdlib.h>

// Fusiona dos subarreglos de arr[].
// El primer subarray es arr [l..m]
// El segundo subarray es arr [m + 1..r]
int globalMergeSort=0;
int globalMerge=0;

void merge(int arr[], int l, int m, int r)
{
    printf("Control 3, entré a merge\n");
    int i, j, k;
    int n1 = m - l + 1;
    int n2 = r - m;
    
    printf("Valor de n1 es %d\n", n1);
    printf("Valor de n2 es %d\n", n2);

    /* Se crean arreglos temporales */
    int L[n1], R[n2];

    /* Copie datos en arreglos temporales L[] y R[] */
    for (i = 0; i < n1; i++)
    {
        printf("Control 4, entré al primer for\n");
        L[i] = arr[l + i];
    }
    for (j = 0; j < n2; j++)
    {
        R[j] = arr[m + 1 + j];
    }

    /* Se combinan los arreglos temporales de nuevo en arr[l..r]*/
    i = 0; // Índice inicial del primer subarreglo
    j = 0; // Índice inicial del segundo subarreglo
    k = l; // Índice inicial del subarreglo combinado
    while (i < n1 && j < n2) 
    {
        if (L[i] <= R[j]) 
        {
            arr[k] = L[i];
            i++;
        }
        else
        {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    /* Se copian los elementos restantes de L[], si hay alguno */
    while (i < n1) 
    {
        arr[k] = L[i];
        i++;
        k++;
    }

    /* Se copian los elementos restantes de R[], si hay alguno */
    while (j < n2) 
    {
        arr[k] = R[j];
        j++;
        k++;
    }
}

/* l es para el índice izquierdo y r es el índice derecho del subarreglo
de arr que se ordenará */
void mergeSort(int arr[], int l, int r)
{
    int s;
    printf("Control 1, imprimir arreglo actual ");
    for(s=0; s<6; s++)
    {
        printf("%d ", arr[s]);
    }
    printf("\n");
    
    globalMergeSort+=1;
    printf("Valor de globalMergeSort es %d\n", globalMergeSort);
    
    if (l < r) 
    {
        printf("Control 2, entré al if\n");
        // Igual que (l+r)/2, pero evita el desbordamiento para
        // grandes l y h
        int m = l + (r - l) / 2; //m=0+(5-1)/2

        // Ordenar la primera y la segunda mitad
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}

/* Función para imprimir */
void printArray(int A[], int size)
{
    int i;
    for (i = 0; i < size; i++)
        printf("%d ", A[i]);
    printf("\n\n");
}

/* Función main */
int main()
{
    int arr[] = { 12, 11, 13, 5, 6, 7 };
    int arr_size = sizeof(arr) / sizeof(arr[0]);
    printf("Tamaño del arreglo %d\n", arr_size);

    printf("El arreglo dado es: \n");
    printArray(arr, arr_size);
    
    mergeSort(arr, 0, arr_size - 1);
    printf("\nEl arreglo ordenado es: \n");
    printArray(arr, arr_size);
    return 0;
}