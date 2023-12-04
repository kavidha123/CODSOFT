import tkinter as tk
import random
from PIL import Image, ImageTk

# Function to open and resize image using Pillow
def open_image(path, base_width, base_height):
    img = Image.open(path)
    img = img.resize((base_width, base_height), Image.Resampling.LANCZOS)
    tk_image = ImageTk.PhotoImage(img)
    return tk_image

# Function to choose rock, paper, or scissors
def user_choice(choice):
    global user_score, comp_score
    user_label.config(text="You Selected: " + choice)
    comp_choice = random.choice(['rock', 'paper', 'scissors'])
    comp_label.config(text="Computer Selected: " + comp_choice)

    if choice == comp_choice:
        result_label.config(text="It's a tie!")
    elif (choice == "rock" and comp_choice == "scissors") or \
         (choice == "scissors" and comp_choice == "paper") or \
         (choice == "paper" and comp_choice == "rock"):
        user_score += 1
        result_label.config(text="You win!")
    else:
        comp_score += 1
        result_label.config(text="You lose!")

    score_label.config(text=f"Score: You - {user_score}, Computer - {comp_score}")

# Function to play again
def play_again():
    user_label.config(text="Choose your option")
    comp_label.config(text="Waiting for your choice")
    result_label.config(text="")

# Setting up the main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")

# Set the background color to light green
root.configure(bg='light green')

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the size and position of the window to 50% of the screen
window_width = screen_width // 2
window_height = screen_height // 2
x_coordinate = screen_width // 4
y_coordinate = screen_height // 4
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Initialize scores
user_score = 0
comp_score = 0

# Load images for the buttons
rock_image = open_image("images/rock.jpg", window_width // 3, window_height // 5)
paper_image = open_image("images/paper.jpg", window_width // 3, window_height // 5)
scissors_image = open_image("images/scissors.jpg", window_width // 3, window_height // 5)
play_again_image = open_image("images/playagain.jpg", window_width // 3, window_height // 5)

# Labels with light green background
user_label = tk.Label(root, text="Choose your option", font=("Helvetica", 14), bg='light green')
user_label.pack(fill='both')

comp_label = tk.Label(root, text="Waiting for your choice", font=("Helvetica", 14), bg='light green')
comp_label.pack(fill='both')

result_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"), bg='light green')
result_label.pack(fill='both')

score_label = tk.Label(root, text=f"Score: You - {user_score}, Computer - {comp_score}", font=("Helvetica", 14), bg='light green')
score_label.pack(fill='both')

# Calculate additional padding to reduce button length by 50%
additional_padding = window_width * 0.25

# Buttons with dark green background
rock_button = tk.Button(root, image=rock_image, text="Rock", compound="top", command=lambda: user_choice("rock"), font=("Helvetica", 14), bg='dark green')
rock_button.pack(fill='both', padx=(additional_padding, additional_padding))

paper_button = tk.Button(root, image=paper_image, text="Paper", compound="top", command=lambda: user_choice("paper"), font=("Helvetica", 14), bg='dark green')
paper_button.pack(fill='both', padx=(additional_padding, additional_padding))

scissors_button = tk.Button(root, image=scissors_image, text="Scissors", compound="top", command=lambda: user_choice("scissors"), font=("Helvetica", 14), bg='dark green')
scissors_button.pack(fill='both', padx=(additional_padding, additional_padding))

play_again_button = tk.Button(root, image=play_again_image, text="Play Again", compound="top", command=play_again, font=("Helvetica", 14), bg='dark green')
play_again_button.pack(fill='both', padx=(additional_padding, additional_padding))

# Start the GUI
root.mainloop()
