<pre>😵 Hangman Game
A classic command-line implementation of the famous word-guessing game "Hangman." Try to guess the hidden word one letter at a time before the stick figure is fully drawn!

📖 Description
This project is a Python-based game where the computer randomly selects a word from a predefined list (animals like cheetah, kangaroo, lion, etc.). The player must guess the letters of the word.

Correct Guess: The letter is revealed in its correct position.

Wrong Guess: You lose a life, and a part of the "Hangman" is drawn on the screen.

Game Over: If you make 6 wrong guesses, the game ends.

I built this project to practice:

Python Lists: Managing the state of the word (['_', '_', 'a', '_']).

String Manipulation: Joining lists into strings for display.

Visual Logic: Using ASCII art to represent game states.

Loops & Conditionals: Checking guesses against the secret word.

⚡ Features
Visual Feedback: Displays the current stage of the hangman using ASCII art.

Duplicate Check: Prevents you from losing a life if you guess a letter you've already found.

Randomization: Every game picks a new word from the list.

Life Tracker: Tells you exactly how many lives you have left.

🎮 How to Play
Run the script.

You will see dashes representing the length of the secret word (e.g., _ _ _ _ _).

Enter a single letter and press Enter.

If you are right, the letter fills in the blanks.

If you are wrong, a piece of the hangman is added.

Win by filling in the word, or lose if the drawing is complete!</pre>
