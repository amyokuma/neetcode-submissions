class Solution {
    public boolean isAnagram(String s, String t) {
        ArrayList<Character> wordOne = new ArrayList<>();
        ArrayList<Character> wordTwo = new ArrayList<>();
        for (int i = 0; i < s.length(); i++){
            wordOne.add(s.charAt(i));
        }
        for (int i = 0; i < t.length(); i++){
            wordTwo.add(t.charAt(i));
        }
        Collections.sort(wordOne);
        Collections.sort(wordTwo);
        if (wordOne.equals(wordTwo)) return true;
        return false;
    }
}
