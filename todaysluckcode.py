import webbrowser
import tkinter as tk

def open_horoscope_link():
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%98%A4%EB%8A%98%EC%9D%98+%EC%9A%B4%EC%84%B8"
    webbrowser.open(url)

def open_new_year_horoscope():
    url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EC%8B%A0%EB%85%84%20%EC%9A%B4%EC%84%B8"
    webbrowser.open(url)

def open_zodiac_horoscope():
    url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjk0&qvt=0&query=%EB%9D%A0%EB%B3%84%20%EC%9A%B4%EC%84%B8"
    webbrowser.open(url)

def open_constellation_horoscope():
    url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EB%B3%84%EC%9E%90%EB%A6%AC%20%EC%9A%B4%EC%84%B8"
    webbrowser.open(url)

root = tk.Tk()
root.title("오늘의 운세")
root.geometry("300x300")

label = tk.Label(root, text="원하는 운세를 선택하세요!", wraplength=250, font=("Arial", 12))
label.pack(pady=20)

button_today = tk.Button(root, text="오늘의 운세", command=open_horoscope_link, font=("Arial", 12))
button_today.pack(pady=5)

button_new_year = tk.Button(root, text="신년운세", command=open_new_year_horoscope, font=("Arial", 12))
button_new_year.pack(pady=5)

button_zodiac = tk.Button(root, text="띠별운세", command=open_zodiac_horoscope, font=("Arial", 12))
button_zodiac.pack(pady=5)

button_constellation = tk.Button(root, text="별자리운세", command=open_constellation_horoscope, font=("Arial", 12))
button_constellation.pack(pady=5)

root.mainloop()
