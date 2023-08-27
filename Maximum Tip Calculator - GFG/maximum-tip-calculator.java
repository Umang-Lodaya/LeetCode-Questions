//{ Driver Code Starts

import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine().trim());
        while (tc-- > 0) {
            String[] inputLine;
            inputLine = br.readLine().trim().split(" ");
            int n = Integer.parseInt(inputLine[0]);
            int x = Integer.parseInt(inputLine[1]);
            int y = Integer.parseInt(inputLine[2]);
            int[] a = new int[n];
            inputLine = br.readLine().trim().split(" ");
            for (int i = 0; i < n; i++) {
                a[i] = Integer.parseInt(inputLine[i]);
            }
            int[] b = new int[n];
            inputLine = br.readLine().trim().split(" ");
            for (int i = 0; i < n; i++) {
                b[i] = Integer.parseInt(inputLine[i]);
            }

            long ans = new Solution().maxTip(a, b, n, x, y);
            System.out.println(ans);
        }
    }
}


// } Driver Code Ends


class Solution {
    long maxTip(int[] a, int[] b, int n, int x, int y) {
        // code here
        Pair[] arr = new Pair[n];
        for(int i=0; i<n; i++){
            int diff = Math.abs(a[i]-b[i]);
            Pair p = new Pair(diff, i);
            arr[i] = p;
        }
        Arrays.sort(arr);
        
        // for (Pair p:arr){
        //     System.out.println(p.toString());    
        // }  
        
        
        long ans = 0;
        
        for(int i=0; i<n; i++){
            int index = arr[i].index;
            if(x>0 && y>0){
                if(a[index] > b[index]){
                    // System.out.println("a["+index+"]: "+a[index]);
                    ans += a[index];
                    x--;
                }else{
                    // System.out.println("b["+index+"]: "+b[index]);
                    ans += b[index];
                    y--;
                }
            }else if(x==0){
                // System.out.println("b["+index+"]: "+b[index]);
                ans += b[index];
                y--;
            }else{
                // System.out.println("a["+index+"]: "+a[index]);
                ans += a[index];
                x--;
            }
        }
        
        return ans;
    }
    
    class Pair implements Comparable<Pair>{
        int diff;
        int index;
        
        public Pair(int diff, int index){
            this.diff = diff;
            this.index = index;
        }
        
        public int compareTo(Pair p){
            return p.diff-this.diff;
        }
        
        public String toString(){
            return diff+" : "+index;
        }
    }
}