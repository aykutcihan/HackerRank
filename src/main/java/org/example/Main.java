package org.example;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();

        ArrayList<ArrayList<Integer>> nestedList = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            ArrayList<Integer> innerList = new ArrayList<>();
            int d = scan.nextInt();
            for (int k = 0; k < d; k++) {
                Integer element = scan.nextInt();
                innerList.add(element);
            }

            nestedList.add(innerList);
        }

        int coordNum = scan.nextInt();
        for (int i = 0; i < coordNum; i++) {
            int x = scan.nextInt();
            int y = scan.nextInt();
            try {
                Integer value = nestedList.get(x - 1).get(y - 1);
                System.out.println(value);
            } catch (IndexOutOfBoundsException e) {
                System.out.println("ERROR!");
            }
        }
    }
}