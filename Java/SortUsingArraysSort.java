// A sample Java program to demonstrate working of 
// Arrays.sort(). 
// It by default sorts in ascending order. 
import java.util.Arrays; 
  
public class SortUsingArraysSort { 
    public static void main(String[] args) 
    { 
        int[] arr = { 113, 17, 16, 145, 121, 19, 1101, 1102 }; 
  
        Arrays.sort(arr); 
  
        System.out.printf("Modified arr[] : %s", 
                          Arrays.toString(arr)); 
    } 
} 
