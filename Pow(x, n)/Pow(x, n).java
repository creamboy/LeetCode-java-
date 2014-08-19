public class Solution {
    public double pow(double x, int n) {
        if(n<0) return 1.0/helper( x, -n);
        return helper(x, n);
    }
    
    public double helper(double x, int n){
        if(n==0) return 1;
        double v=helper(x, n/2);
        if(n%2==0) return v*v;
        return v*v*x;
    }
    
}
