//A number representing the maximum profit you can make if you are allowed a single transaction to buy and sell stock.

import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();
        int[] arr = new int[n];
        for(int i = 0 ; i < n ; i ++)
            arr[i]=scn.nextInt();
            
        int least = arr[0];
        int profit = Integer.MIN_VALUE;
        
        for(int i = 1 ;i < n ; i ++){
            if(arr[i]<least){
                least=arr[i];
            }else{
                int curprofit = arr[i]-least;
                if(curprofit>profit)
                    profit = curprofit;
            }
        }
        
        System.out.println(profit);
    }

}