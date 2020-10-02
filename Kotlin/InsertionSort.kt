/**
 * Perform insertion sort using kotlin
 */

fun insertionSort2(arr: Array<Int>): Array<Int> {
    for(i in arr.indices){
        val key = arr[i]
        var j = i - 1

        while (j >= 0 && arr[j] > key){
            arr[j + 1] = arr[j]
            j -= 1
        }

        arr[j + 1] = key
    }
    return arr
}
