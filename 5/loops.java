import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

   public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
      int n = scan.nextInt(); 
      scan.close();
      String ans="";
          
      for (int i = 1; i <= 10; i++) {
          ans = String.format("%d x %d = %d", n, i, n*i);
          System.out.println(ans);
      }
   }
}
