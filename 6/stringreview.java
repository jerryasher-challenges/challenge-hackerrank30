import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class stringreview {

   public static void main(String[] args) {
       Scanner scan = new Scanner(System.in);
       int n = scan.nextInt(); 
       String line = "";
       String first = "";
       String second = "";
       line = scan.nextLine(); // throwaway
       for (int i = 0; i < n; i++) {
           first = "";
           second = "";
           line = scan.nextLine();
              
           for (int c = 0; c < line.length(); c++) {
               char ch = line.charAt(c);
               if (c % 2 == 0) {
                   first += ch;
               } else {
                   second += ch;
               }
           }
           System.out.println(first + " " + second);
       }
       scan.close();
   }
}
