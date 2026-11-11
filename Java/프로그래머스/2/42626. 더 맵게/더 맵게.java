import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> foods = new PriorityQueue<>();
        
        for (int food : scoville) {
            foods.offer(food);
        }
        
        while (foods.peek() < K && foods.size() > 1) {
            Integer first = foods.poll();
            Integer second = foods.poll();
            
            foods.offer(first + 2 * second);
            answer++;
        }
        
        return foods.peek() < K ? -1 : answer;
    }
}