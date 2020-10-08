import java.io.*;
import java.util.*;
import java.lang.*;
class Data {
 Scanner sc = new Scanner(System.in);
 double r;
void read() {
 System.out.println("Enter Radius");
 r = sc.nextDouble();
 }
}
class Area extends Data {
 double area;
 void calculate() {
 area = 3.14 * r * r;
 }
 void display() {
 System.out.println("Area is" + area);
 }
}
class Volume extends Area {
 double vol;
 void volume() {
 vol = (area * 4 * r) / 3;
 }
 void display1() {
 System.out.println("Volume is " + vol);
 }
}
class MultipleInheritance {
 public static void main(String[] args) {
 Volume c = new Volume();
 c.read();
 c.calculate();
 c.display();
 c.volume();
 c.display1();
}
}
