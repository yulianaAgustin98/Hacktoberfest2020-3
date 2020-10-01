class binarysearch {
    public static int binsearch(int arr[], int x) {
        int n = arr.length;
        int i = 0, j = arr.length - 1;
        while (i < j) {
            if (arr[i] == x)
                return i;
            if (arr[i] < x)
                i++;
            else
                j--;
        }
        return -1;
    }

    public static void main(String args[]) {
        int arr[] = { 2, 10, 13, 24, 29 };
        int x = 13;

        int result = binsearch(arr, x);
        if (result == -1)
            System.out.print("Element is not present in array");
        else
            System.out.print("Element is present at index " + result);
    }
}
