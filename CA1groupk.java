/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
We enjoy writing programs.

We write software that has:
Class: Authors
Method 1: print ‘Hello World’
Method 2: add two numbers
Method 3: subtract one number from another
Method 4: Multiply two numbers

 */




package ca1groupk;

import java.io.BufferedReader;//Public class BufferedReader extends Reader.
import java.io.InputStreamReader;//An InputStreamReader is a bridge from byte streams to character streams.
/**
 *
 * @author Jurijus Pacalovas
 */
public class CA1groupk {

    static void MyAuthors()
    {
      //Class: Authors in the program.
        //I have created the CA1groupk main class in the program.
        //I have created the myObj.x. object in the program.
        MyAuthors myObjl = new MyAuthors();
        System.out.println(myObjl.x);
        System.out.println(myObjl.x1);
        System.out.println(myObjl.x2);
        System.out.println(myObjl.x3);
        System.out.println(myObjl.x4);
        System.out.println(myObjl.x5);
        System.out.println(myObjl.x6);
        System.out.println(myObjl.x7);
    }
        
    /**
     * @param args the command line arguments
     */
    //I have made the method HW for Hello World.
     static void HW() {
      System.out.println("Hello World!!!");
  }
    
    //method Multiply  add one number from another in the program.
     
     public static int addf(int n1, int n2) {
   int total;
   
    total=n1+n2;
    
   return total; 
}
     //metod minus  one number from another in the program.
     
   public static int subf(int n1, int n2) {
   int total;
   
    total=n1-n2;
    
   return total; 
}
      //method Multiply one number from another in the program.
    public static  int mulf(int n1, int n2) {
   int total;
   
    total=n1*n2;
    
   return total; 
}
     
     static void method(){ 
        String myName = "Luiza";
               System.out.println ("Hello world by: " + myName); 
    }
     
    static void methodm()
             
             {
                      BufferedReader myKeyboard = new BufferedReader(new InputStreamReader(System.in)); 
      int anum1, bnum2, total;
        
      System.out.println("Please enter 1st number");
        
        try{
            anum1 = Integer.parseInt(myKeyboard.readLine()); 
            //readLine() method ONLY reads text - need Integer.parseInt to convert to int value (if possible)
        
            System.out.println("Please enter 2nd number");
             bnum2 = Integer.parseInt(myKeyboard.readLine());
   
           
            
               total = addf(anum1, bnum2);//I have made the addf metod for add the numbers in the program. 
               
        System.out.println(" num1 " + anum1 + " and num2 " + bnum2 + " sum numbers " + total);//The program show numbers that is add.        
               
               
               total = subf(anum1, bnum2);//I have made the subf method for substract the numbers in the program.
               
               
        
         System.out.println(" num1 " + anum1 + " and num2 " + bnum2 + " subtract numbers " + total); //The program show numbers that is substract.
         
                total = mulf(anum1, bnum2);//I have made the mulf method for Multiply the numbers in the program.
                
        
         System.out.println(" num1 " + anum1 + " and num2 " + bnum2 + " Multiply  numbers " + total); //The program show numbers that is Multiply. 
         
       
        }
        catch (Exception e){
            
            System.out.println("That is not valid input -- only numbers allowed");//Error this varibles not numbers in the program.
        }
                 
             }
   
   //Method 4: Multiply two numbers
    public static void main(String[] args) {
        // TODO code application logic here
      
        
        MyAuthors();// I have crated the MyAuthors method for Authors in the program
       //Method 1: print ‘Hello World’ in the program.
        HW();
        method();//Hello world: Luiza
        methodm();// I have crated the *,-,+ method in the program
        
        
    }
      
      
        
    }
    
    

