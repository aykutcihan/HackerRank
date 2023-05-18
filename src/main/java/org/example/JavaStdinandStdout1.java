package org.example;

import java.util.*;

public class JavaStdinandStdout1 {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        for(int i = 0; i < 3; i++) {
            int num = scan.nextInt();
            System.out.println(num);
        }

        scan.close();

    }
}
