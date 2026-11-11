import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        ArrayList<Integer> result = new ArrayList<>();
        
        for (int number : arr) {
            if (result.size() < 1) {
                result.add(number);
                continue;
            } else {
                if (result.get(result.size() - 1) != number) {
                    result.add(number);
                }
            }
        }

        int[] answer = new int[result.size()];
        int idx = 0;
        
        while (idx < result.size()) {
            answer[idx] = result.get(idx);
            idx++;
        }
        
        return answer;
    }
}