public static int calculateScore(String word){
    int score = 0;
    for (char c : word.toCharArray()) {
        if (c != 'a'){
            score++;
        }
    }
    return score;
}


public static int wordScore(String word){
    return word.replaceAll("a", "").length();
}


public static void main(String[] args) {
    System.out.println(calculateScore("imperative") == 9);
    System.out.println(wordScore("declarative") == 9);
    System.out.println(calculateScore("no") == 2);
    System.out.println(wordScore("yes") == 3);
}
