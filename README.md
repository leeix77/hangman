# hangman
Group members: Kenneth Pak, Jingran Cao, Lei Xu

This is our hangman project, which will emulate the classic hangman game with a human player guessing a word that the computer has randomly chosen.

Data- words.txt

How to run it:
  import hangman1
  
  hangman1.hangman(hangman1.secret_word)

There should be a space for you to input after you run the above code. 
When you input "cheat", the word appear. You are expected to see "You cheat but you win this game." 
When you input "show", it shows all the same letters in the secret word each time and the available times and letters left and you continue guessing until you win or lose.
When you input "dele", it deletes some letters that don't belong to the secret word as a hint
When you guess a letter, it will tell you if it's right or wrong, and you continue guessing until you win or lose.


Reference:
https://python.land/deep-dives/python-try-except
https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/assignments/

Our assignment is different because we implemented exception handling, different hints like cheat, and custom messages that are printed.

<img width="1145" alt="Screen Shot 2022-03-17 at 9 35 45 PM" src="https://user-images.githubusercontent.com/97067231/158938670-020b6aaf-f190-421b-8b99-a389c2183876.png">
This image shows the cheat hint.
<img width="1133" alt="Screen Shot 2022-03-17 at 9 35 12 PM" src="https://user-images.githubusercontent.com/97067231/158938708-0993593f-f2fc-4876-b60d-830afa2ad2be.png">
This image shows an example game.
The output will also show a list of available letters and letters already guessed. It will show an empty _ if that letter hasn't been guessed yet. Output will also show how many chances you have left.
