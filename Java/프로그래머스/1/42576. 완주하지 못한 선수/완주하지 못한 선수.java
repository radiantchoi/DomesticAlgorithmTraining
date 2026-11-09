import java.util.HashMap;

class Solution {
    public String solution(String[] participant, String[] completion) {
        HashMap<String, Integer> occurence = new HashMap<>();
        
        for (String person : participant) {
            Integer count = occurence.getOrDefault(person, 0);
            occurence.put(person, count + 1);
        }
        
        for (String person : completion) {
            Integer count = occurence.getOrDefault(person, 0);
            occurence.put(person, count - 1);
        }
        
        for (String person: occurence.keySet()) {
            if (occurence.get(person) != 0) {
                return person;
            }
        }
        
        return "";
    }
}