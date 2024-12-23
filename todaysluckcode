import webbrowser
import tkinter as tk

def open_horoscope_link():
    url = "https://www.horoscope.com/us/index.aspx"  # Replace with your preferred horoscope site
    webbrowser.open(url)

# Create the main window
root = tk.Tk()
root.title("오늘의 운세")
root.geometry("300x150")

# Add a label
label = tk.Label(root, text="화면의 버튼을 눌러 오늘의 운세를 확인하세요!", wraplength=250, font=("Arial", 12))
label.pack(pady=20)

# Add a button
button = tk.Button(root, text="오늘의 운세 알아보기", command=open_horoscope_link, font=("Arial", 12))
button.pack(pady=10)

# Run the application
root.mainloop()
