from tkinter import *
from tkinter import messagebox
import requests


window = Tk()
window.title("Weather App")
window.minsize(300,500)
window.config(background="#D17BF4",pady=10)

name_label = Label()
temp_label = Label()
def searchBtnClicked():
    if my_entry.get() != "":
        url = f"https://api.openweathermap.org/data/2.5/weather?q={my_entry.get()}&appid=de83d9fb4fd506c17d49bdb0e75f972c"
        try:
            response = requests.get(url)
            weather_info = response.json()
            name_label.config(text=weather_info["name"],bg="#D17BF4",fg="black",font=("Arial",10,"italic"))
            name_label.pack(pady=30)
            temp = str(round(float(weather_info["main"]["temp"]) - 273, 2))
            temp_label.config(text=temp+"C", bg="#D17BF4", fg="black",font=("Arial",15,"italic"))
            temp_label.pack(pady=5)
        except:
            messagebox.showerror("Weather Error","city not found!")


my_label = Label(text="Enter the city name",bg="white",font=("Arial", 7, "italic"))
my_label.pack()
my_entry = Entry(background="white",width=30)
my_entry.pack(pady=5)
my_button = Button(text="search",bg="blue",fg="white",command=searchBtnClicked)
my_button.pack(pady=15)
mainloop()