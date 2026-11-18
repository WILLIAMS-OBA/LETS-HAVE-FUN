import java.util.Scanner;

public class TaskOne{
  public static void main(String[] args){
  Scanner input= new Scanner(System.in);
  
  double average = 0;
  double sum = 0;
  int counter = 0;
  for (; counter <= 10; counter++){
  
  System.out.print("Enter a score: ");
  int score = input.nextInt();
  
    sum += score;
  
  }
  average = sum / counter;
  
  System.out.println("Sum is: "+ sum);
  System.out.println("Average is: "+ average);
  }

}
