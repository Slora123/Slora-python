import tkinter as tk
from tkinter import messagebox
import webbrowser
from tkcalendar import Calendar
def open_calendar():
    webbrowser.open("https://www.canva.com/design/DAGXRrNH9r4/zPobD63zBBMepiMCVyld6Q/edit?utm_content=DAGXRrNH9r4&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton")
def start_quiz():
    webbrowser.open("https://quizizz.com/join?gc=35785024")
def open_flipbook():
    webbrowser.open("https://heyzine.com/flip-book/555e022e12.html")
def open_shopping():
    shopping_window = tk.Toplevel(root)
    shopping_window.title("Traditional Shopping")
    shopping_var = tk.StringVar()
    shopping_var.set("Select Category")
    shopping_options = ["Desi Toys", "Desi Clothes", "Desi Food"]
    shopping_menu = tk.OptionMenu(shopping_window, shopping_var, *shopping_options)
    shopping_menu.pack(pady=10)
    def go_to_shopping():
        selected_category = shopping_var.get()
        if selected_category == "Desi Toys":
            webbrowser.open("https://www.desitoys.in/?srsltid=AfmBOoq5qSZfNKvNbdqs7s4laSR9kO2kzp4eK7ypj2kZwNafinq6VCdt")
        elif selected_category == "Desi Clothes":
            webbrowser.open("https://www.globaldesi.in/?srsltid=AfmBOooE_cdkNVPFBZ0Os9Ar6vmtEbqBuGmIm4VahzVklNnQW8Pm9-OI")
        elif selected_category == "Desi Food":
            webbrowser.open("https://thedesifood.com/?srsltid=AfmBOorCJ8LVEeo6gENW0t4RNK15Y80Dton12qKC7DTt0SaukIhqc5RF")
        else:
            messagebox.showerror("Error", "Please select a valid category.")
    btn_shopping_category = tk.Button(shopping_window, text="Go to Selected Shopping Category", command=go_to_shopping)
    btn_shopping_category.pack(pady=10)
def show_videos():
    videos_window = tk.Toplevel(root)
    videos_window.title("Traditional Videos")
    video_var = tk.StringVar()
    video_var.set("Select Video")
    video_options = [
        "Video 1: Cultural Practices",
        "Video 2: Traditional Crafts",
        "Video 3: Heritage and Art"
    ]
    video_menu = tk.OptionMenu(videos_window, video_var, *video_options)
    video_menu.pack(pady=10)
    def play_video():
        selected_video = video_var.get()
        if selected_video == "Video 1: Cultural Practices":
            webbrowser.open("https://youtu.be/pPhyjOtxKXA?si=glTKzGULVTtIOx7Y")
        elif selected_video == "Video 2: Traditional Crafts":
            webbrowser.open("https://youtu.be/Tj3UvoKutUo?si=B7zg9fBAYwOeJdux")
        elif selected_video == "Video 3: Heritage and Art":
            webbrowser.open("https://youtu.be/vYE4oDT3vDs?si=cbioYRu2nUlEGEIO")
        else:
            messagebox.showerror("Error", "Please select a valid video.")
    btn_play_video = tk.Button(videos_window, text="Watch Selected Video", command=play_video)
    btn_play_video.pack(pady=10)
root = tk.Tk()
root.title("Culture Connect")
btn_calendar = tk.Button(root, text="Heritage Highlights", command=open_calendar)
btn_calendar.pack(pady=10)
btn_quiz = tk.Button(root, text="Heritage Hunt", command=start_quiz)
btn_quiz.pack(pady=10)
btn_flipbook = tk.Button(root, text="Tradition Tales", command=open_flipbook)
btn_flipbook.pack(pady=10)
btn_shopping = tk.Button(root, text="Cultural Bazaar", command=open_shopping)
btn_shopping.pack(pady=10)
btn_videos = tk.Button(root, text="Heritage Frames", command=show_videos)
btn_videos.pack(pady=10)
root.mainloop()
