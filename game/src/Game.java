import java.util.Random;
import java.util.Scanner;

public class Game {
    private final Random random;
    private final Scanner scanner;
    private int score;

    public Game(Scanner scanner) {
        this.random = new Random();
        this.scanner = scanner;
        this.score = 0;
    }

    public void startNewGame() {
        int numberToGuess = random.nextInt(100) + 1;
        int attempts = 0;
        int maxAttempts = 5;
        boolean guessedCorrectly = false;

        System.out.println("Guess a number between 1 and 100.");

        while (attempts < maxAttempts && !guessedCorrectly) {
            System.out.print("Enter your guess: ");
            int guess = scanner.nextInt();
            attempts++;

            if (guess == numberToGuess) {
                System.out.println("Correct! You've guessed the number!");
                score += maxAttempts - attempts + 1; // Score calculation based on attempts
                guessedCorrectly = true;
            } else if (guess < numberToGuess) {
                System.out.println("Too low. Try again.");
            } else {
                System.out.println("Too high. Try again.");
            }
        }

        if (!guessedCorrectly) {
            System.out.println("You've used all your attempts. The number was " + numberToGuess);
        }

        System.out.println("Your score: " + score);
    }

    public int getScore() {
        return score;
    }
}
