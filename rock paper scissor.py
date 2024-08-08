import tkinter as tk
import random
from tkinter import messagebox

# Initialize scores
user_score = 0
computer_score = 0

def play_game(user_choice):
    global user_score, computer_score
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    
    if (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper'):
        result = f'You chose {user_choice}, computer chose {computer_choice}. You win!!!'
        user_score += 1
    elif user_choice == computer_choice:
        result = f'You chose {user_choice}, computer chose {computer_choice}. It\'s a draw!!! Try Again.'
    else:
        result = f'You chose {user_choice}, computer chose {computer_choice}. You lose!!!'
        computer_score += 1
    
    user_score_label.config(text=f"User Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")
    result_label.config(text=result)

    root.update_idletasks()

    if not messagebox.askyesno("Play Again", "Do you want to play another round?"):
        root.quit()

# Create main window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
root.geometry("600x600")
root.configure(bg="#E8F6F3")

# Title label
title_label = tk.Label(root, text="Welcome to the Rock, Paper, Scissors Game!", font=("Helvetica", 22, "bold"), bg="#E8F6F3", fg="#154360")
title_label.pack(pady=30)

# Instructions label
instructions_label = tk.Label(root, text="Choose one of the options below to play:", font=("Helvetica", 18), bg="#E8F6F3", fg="#154360")
instructions_label.pack(pady=10)

# Result label
result_label = tk.Label(root, font=("Helvetica", 20), bg="#E8F6F3", wraplength=500, fg="#154360")
result_label.pack(pady=20)

# Score labels frame
score_frame = tk.Frame(root, bg="#E8F6F3")
score_frame.pack(pady=10)

user_score_label = tk.Label(score_frame, text=f"User Score: {user_score}", font=("Helvetica", 18), bg="#ADD8E6", fg="#154360", width=20, anchor="w")
user_score_label.grid(row=0, column=0, padx=10, pady=5)

computer_score_label = tk.Label(score_frame, text=f"Computer Score: {computer_score}", font=("Helvetica", 18), bg="#ADD8E6", fg="#154360", width=20, anchor="w")
computer_score_label.grid(row=0, column=1, padx=10, pady=5)

# Button frame
button_frame = tk.Frame(root, bg="#E8F6F3")
button_frame.pack(pady=30)

# Rock button
rock_button = tk.Button(button_frame, text="Rock", font=("Helvetica", 18), bg="#90EE90", command=lambda: play_game('rock'))
rock_button.grid(row=0, column=0, padx=20, pady=10)

# Paper button
paper_button = tk.Button(button_frame, text="Paper", font=("Helvetica", 18), bg="#90EE90", command=lambda: play_game('paper'))
paper_button.grid(row=0, column=1, padx=20, pady=10)

# Scissors button
scissors_button = tk.Button(button_frame, text="Scissors", font=("Helvetica", 18), bg="#90EE90", command=lambda: play_game('scissors'))
scissors_button.grid(row=0, column=2, padx=20, pady=10)

# Exit button
exit_button = tk.Button(root, text="Exit", font=("Helvetica", 18), bg="#FF6347", command=root.quit)
exit_button.pack(pady=20)

root.mainloop()
