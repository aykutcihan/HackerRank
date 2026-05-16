package org.example;

import java.util.Scanner;

public class JavaStringToken {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();

        if(s.replaceAll(" ","").length()==0){
            System.out.println(0);
        }
        else{
            s=s.trim();
            // s= s.replaceAll("[\\p{Punct}]", "");
            String[] arr = s.split("[\\p{Punct} ]+");


            System.out.println(arr.length);
            for(int i=0; i<arr.length; i++){

                System.out.println(arr[i]);
            }
        }

        scan.close();
    }
}



