import vlc
import os
import tkinter as tk
from tkinter import messagebox
quiz_scores = []
video_path = r"C:\Users\Lenovo\Downloads\mini_proj_vid.mp4"
def play_video_with_controls():
    if not os.path.exists(video_path):
        messagebox.showerror("Error", f"Video file not found at {video_path}")
        return
    video_window = tk.Toplevel(root)
    video_window.title("Video Player")
    video_window.geometry("600x400")
    instance = vlc.Instance()
    player = instance.media_player_new()
    media = instance.media_new(video_path)
    player.set_media(media)
    video_frame = tk.Frame(video_window)
    video_frame.pack(fill="both", expand=True)
    player.set_hwnd(video_frame.winfo_id())
    player.play()
    control_frame = tk.Frame(video_window)
    control_frame.pack(pady=10)
    def play_pause():
        if player.is_playing():
            player.pause()
        else:
            player.play()
    def forward():
        current_time = player.get_time()
        player.set_time(current_time + 10000)
    def backward():
        current_time = player.get_time()
        player.set_time(max(0, current_time - 10000))
    def stop_video():
        player.stop()
        video_window.destroy()
    play_pause_btn = tk.Button(control_frame, text="Play/Pause", command=play_pause, font=("Arial", 12))
    play_pause_btn.pack(side="left", padx=10)
    forward_btn = tk.Button(control_frame, text="Forward 10s", command=forward, font=("Arial", 12))
    forward_btn.pack(side="left", padx=10)
    backward_btn = tk.Button(control_frame, text="Backward 10s", command=backward, font=("Arial", 12))
    backward_btn.pack(side="left", padx=10)
    stop_btn = tk.Button(control_frame, text="Stop", command=stop_video, font=("Arial", 12))
    stop_btn.pack(side="left", padx=10)
    video_window.protocol("WM_DELETE_WINDOW", stop_video)
def play_quiz():
    quiz_window = tk.Toplevel(root)
    quiz_window.title("Quiz")
    quiz_window.geometry("500x400")
    questions = [
        ("Lord Malhari is believed to be an incarnation of which Hindu God?",
         ["a) Lord Shiva", "b) Lord Vishnu", "c) Lord Brahma", "d) Lord Ganesh"],
         "a"),
        ("What is the meaning of the name 'Malhari'?",
         ["a) Protector of devotees", "b) Slayer of demons Malla and Mani", "c) The great warrior", "d) King of Gods"],
         "b"),
        ("What was the name of the two demon brothers defeated by Lord Malhari?",
         ["a) Ravan and Kumbhakarna", "b) Malla and Mani", "c) Shumbh and Nishumbh", "d) Kaliya and Mahishasura"],
         "b"),
        ("On which vehicle did Lord Malhari ride during the battle?",
         ["a) Horse", "b) Elephant", "c) Nandi (Bull)", "d) Chariot"],
         "c"),
        ("What color is associated with Lord Malhari's body during the battle?",
         ["a) Red", "b) Yellow (Turmeric-covered)", "c) Blue", "d) Green"],
         "b"),
        ("On which day is Lord Malhari's victory over the demons celebrated?",
         ["a) Diwali", "b) Kartik Amavasya", "c) Makar Sankranti", "d) Gudi Padwa"],
         "b"),
        ("What form did Lord Shiva take to defeat the demons?",
         ["a) Rudra", "b) Martand Bhairav", "c) Shankara", "d) Kalabhairav"],
         "b"),
        ("What is the primary offering made by devotees of Lord Malhari in many regions?",
         ["a) Milk", "b) Goat meat", "c) Fruits", "d) Flowers"],
         "b"),
        ("What is the significance of Mani's request to Lord Malhari?",
         ["a) To grant him a place near the deity", "b) To forgive him", "c) To give him wealth", "d) To release him from the curse"],
         "a"),
        ("What form of sacrifice was practiced in the name of Lord Malhari in earlier times?",
         ["a) Animal sacrifice", "b) Human self-sacrifice", "c) Fire sacrifice", "d) Water sacrifice"],
         "b"),
        ("What is the other name by which Lord Malhari is known in Maharashtra?",
         ["a) Khandoba", "b) Shankar", "c) Bhairav", "d) Mahadev"],
         "a"),
        ("In which regions is Lord Malhari primarily worshipped?",
         ["a) Gujarat", "b) Rajasthan", "c) Maharashtra and Karnataka", "d) Madhya Pradesh"],
         "c"),
    ]
    score = 0
    question_index = 0
    def submit_answer():
        nonlocal question_index, score
        user_answer = answer_entry.get().strip().lower()
        if user_answer == questions[question_index][2]:
            score += 1
        question_index += 1
        if question_index < len(questions):
            question_label.config(text=f"Q{question_index + 1}: {questions[question_index][0]}")
            option_1.config(text=questions[question_index][1][0])
            option_2.config(text=questions[question_index][1][1])
            option_3.config(text=questions[question_index][1][2])
            option_4.config(text=questions[question_index][1][3])
            answer_entry.delete(0, tk.END) 
        else:
            quiz_scores.append(score)
            messagebox.showinfo("Quiz Finished", f"You scored: {score}/{len(questions)}")
            quiz_window.destroy()
    question_label = tk.Label(quiz_window, text=f"Q1: {questions[0][0]}", font=("Arial", 14), wraplength=450)
    question_label.pack(pady=10)
    option_1 = tk.Label(quiz_window, text=questions[0][1][0], font=("Arial", 12))
    option_1.pack(pady=5)
    option_2 = tk.Label(quiz_window, text=questions[0][1][1], font=("Arial", 12))
    option_2.pack(pady=5)
    option_3 = tk.Label(quiz_window, text=questions[0][1][2], font=("Arial", 12))
    option_3.pack(pady=5)
    option_4 = tk.Label(quiz_window, text=questions[0][1][3], font=("Arial", 12))
    option_4.pack(pady=5)
    instruction_label = tk.Label(quiz_window, text="Enter the option letter (a, b, c, or d) in the textbox below:", font=("Arial", 10))
    instruction_label.pack(pady=5)
    answer_entry = tk.Entry(quiz_window, font=("Arial", 12))
    answer_entry.pack(pady=10)
    submit_btn = tk.Button(quiz_window, text="Submit", command=submit_answer, font=("Arial", 12))
    submit_btn.pack(pady=10)
def show_dashboard():
    dashboard_window = tk.Toplevel(root)
    dashboard_window.title("Dashboard")
    dashboard_window.geometry("300x200")
    if quiz_scores:
        scores_text = "\n".join(f"Quiz {i + 1}: {score}" for i, score in enumerate(quiz_scores))
    else:
        scores_text = "No quizzes played yet."
    tk.Label(dashboard_window, text="Quiz Scores", font=("Arial", 16)).pack(pady=10)
    tk.Label(dashboard_window, text=scores_text, font=("Arial", 14), justify="left").pack(pady=10)
root = tk.Tk()
root.title("Main Menu")
root.geometry("300x200")
tk.Label(root, text="Choose an option:", font=("Arial", 16)).pack(pady=20)
video_btn = tk.Button(root, text="See Video", font=("Arial", 14), command=play_video_with_controls)
video_btn.pack(pady=10)
quiz_btn = tk.Button(root, text="Play Quiz", font=("Arial", 14), command=play_quiz)
quiz_btn.pack(pady=10)
dashboard_btn = tk.Button(root, text="See Dashboard", font=("Arial", 14), command=show_dashboard)
dashboard_btn.pack(pady=10)
root.mainloop()