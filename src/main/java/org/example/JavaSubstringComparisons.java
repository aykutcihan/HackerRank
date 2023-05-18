package org.example;

import java.util.Scanner;

public class JavaSubstringComparisons {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();

        String result = getSmallestAndLargest(s, k);
        System.out.println(result);
    }

    public static String getSmallestAndLargest(String s, int k) {

        String smallest = "";
        String largest = "";

        for (int i = 0; i <= s.length() - k; i++) {
            String current = s.substring(i, i + k);
            if (smallest.equals("") || current.compareTo(smallest) < 0) {
                smallest = current;
            }
            if (largest.equals("") || current.compareTo(largest) > 0) {
                largest = current;
            }
        }
        return smallest + "\n" + largest;

    }

}