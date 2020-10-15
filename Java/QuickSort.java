import java.util.Arrays;
import java.util.Scanner;

public class QuickSort
{
    public static void main(String[] args)
    {Scanner sc = new Scanner(System.in);
        System.out.println("Enter the size of your array:");
        int n = sc.nextInt(); 

        int array[] = new int [n];
        
        System.out.println("Enter your array:");
        for (int i = 0; i < n; i++)
         array[i] =sc.nextInt(); 
 
        // Let's sort using quick sort
        quickSort( array, 0, array.length - 1 );
 
        System.out.println(Arrays.toString(array));
        sc.close();
    }
 
    public static void quickSort(int[] array, int low, int high) {

        if (array == null || array.length == 0) {
            return;
        }

        if (low >= high) {
            return;
        }

        int middle = low + (high - low) / 2;
        int pivot = array[middle];

        int i = low, j = high;
        while (i <= j) {

            while (array[i] < pivot) {
                i++;
            }

            while (array[j] > pivot) {
                j--;
            }
            if (i <= j) {
                swap(array, i, j);
                i++;
                j--;
            }
        }
        if (low < j) {
            quickSort(array, low, j);
        }
        if (high > i) {
            quickSort(array, i, high);
        }
    }
     
    public static void swap (int[] array, int x, int y) {
        int temp = array[x];
        array[x] = array[y];
        array[y] = temp;
    }
}
