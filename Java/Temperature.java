import java.util.Scanner;
class Temperature
{
	public static void main(String arg[]){
		Scanner KB=new Scanner(System.in);
		System.out.println("Enter the temperature in Celsius:");
		float c=KB.nextFloat();
		float f=((9*c)/5)+32;
		System.out.println("The temperature in farenheit is="+f);
	}
}
