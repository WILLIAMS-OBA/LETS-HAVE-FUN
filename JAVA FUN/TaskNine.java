import java.util.Scanner;

public class TaskOne{
  public static void main(String[] args){
  Scanner input= new Scanner(System.in);
  
  
  double sum = 0;
  int counter = 1;
  for (; counter <= 10; counter++){
  
  System.out.print("Enter a score: ");
  int score = input.nextInt();
  if (score > 0 && score < 100){
    sum += score;
  }
  }
  
  System.out.println("Sum is: "+ sum);
  
  }

}
