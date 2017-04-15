/**
 * Created by Jello on 2017. 4. 15..
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class P1406 {
    public static void printMessage(Stack<Character> left, Stack<Character> right){
        while(!left.isEmpty()){
            right.push(left.pop());
        }
        while(!right.isEmpty()){
            System.out.print(right.pop());
        }
    }
    public static void main(String[] args) throws IOException {
        // String? ArrayList? LinkedList? Stack?
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Stack<Character> left = new Stack<>();
        Stack<Character> right = new Stack<>();

        char[] message = br.readLine().toCharArray();
        for(char c : message){
            left.push(c);
        }

        int n = Integer.parseInt(br.readLine());
        for(int i=0;i<n;i++){
            char[] command = br.readLine().toCharArray();
            if(command[0] == 'L' && left.size() > 0){
                right.push(left.pop());
            }else if(command[0] == 'D' && right.size() > 0){
                left.push(right.pop());
            }else if(command[0] == 'B' && left.size() > 0){
                left.pop();
            }else if(command[0] == 'P'){
                left.push(command[2]);
            }
        }

        printMessage(left, right);
        br.close();
    }
}
