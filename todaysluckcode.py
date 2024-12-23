import webbrowser
import tkinter as tk

def open_horoscope_link():
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%98%A4%EB%8A%98%EC%9D%98+%EC%9A%B4%EC%84%B8"
    webbrowser.open(url)


root = tk.Tk()
root.title("오늘의 운세")
root.geometry("300x150")


label = tk.Label(root, text="화면의 버튼을 눌러 오늘의 운세를 확인하세요!", wraplength=250, font=("Arial", 12))
label.pack(pady=20)


button = tk.Button(root, text="오늘의 운세 알아보기", command=open_horoscope_link, font=("Arial", 12))
button.pack(pady=10)


root.mainloop()
