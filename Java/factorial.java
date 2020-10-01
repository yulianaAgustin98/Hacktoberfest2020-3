import java.util.Scanner;

public class Factorial {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter number , whose factorial you want to calculate :");
		int n = sc.nextInt();
		int factorial = 1;
		for(int i = n; i>=1; i--){
			factorial = factorial * i;
		}
		System.out.println(factorial);
	}

}
