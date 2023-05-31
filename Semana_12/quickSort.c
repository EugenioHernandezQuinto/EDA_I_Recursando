// Implementación de QuickSort en C

#include <stdio.h>
// Función para intercambiar dos elementos
void swap(int* a, int* b)
{
    int t = *a;
    *a = *b;
    *b = t;
}

// Particionar el arreglo usando el último elemento como pivote
int partition(int arr[], int low, int high)
{
    // Elegir el pivote
    int pivot = arr[high];

    // Índice de elemento más pequeño e indica
    // la posición correcta del pivote encontrada hasta ahora
    int i = (low - 1);
    for (int j = low; j < high; j++) 
    {
        // Si el elemento actual es más pequeño que el pivote
        if (arr[j] < pivot) 
        {
            // Índice de incremento del elemento más pequeño
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return (i + 1);
}

// Función que implementa QuickSort
// arr[] --> Arreglo a ordenar,
// low --> ïndice inicial,
// high --> Índice final
void quickSort(int arr[], int low, int high)
{
    if (low < high) 
    {
        // pi es índice de partición, arr[p]
        // ahora está en el lugar correcto
        int pi = partition(arr, low, high);

        // Ordenar por separado los elementos antes de la
        // partición y después de la partición
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

// Función main
int main()
{
    int arr[] = { 10, 7, 8, 9, 1, 5 };
    int N = sizeof(arr) / sizeof(arr[0]);

    // Function call
    quickSort(arr, 0, N - 1);
    printf("Sorted array: \n");
    for (int i = 0; i < N; i++)
        printf("%d ", arr[i]);
    return 0;
}