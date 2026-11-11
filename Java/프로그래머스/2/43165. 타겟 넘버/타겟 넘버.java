import java.util.*;

class Solution {
    public int solution(int[] numbers, int target) {
        return traverse(numbers, 0, 0, target);
    }
    
    private int traverse(int[] numbers, int current, int idx, int target) {
        if (numbers.length == idx) {
            return target == current ? 1 : 0;
        }
        
        return traverse(numbers, current + numbers[idx], idx + 1, target) + 
            traverse(numbers, current - numbers[idx], idx + 1, target);
    }
}