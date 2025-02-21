# Kevin and Stuart want to play the 'The Minion Game'.

# Game Rules

# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# Scoring
# A player gets +1 point for each occurrence of the substring in the string .

# For Example:
# String  = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.




def minion_game(string):
    # your code goes here
    li = ["A","E","I","O","U"]
    points_k =0
    points_s = 0
    
    for i in range(len(string)):
        if string[i] in li:
            points_k+=len(string)-i
        else:
            points_s+=len(string)-i
            
    if points_k>points_s:
        print(f"Kevin {points_k}")
    elif points_k==points_s:
        print("Draw")
    else:
        print(f"Stuart {points_s}")

if __name__ == '__main__':
    s = input()
    minion_game(s)