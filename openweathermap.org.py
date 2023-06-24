import requests
from tkinter import *
from tkinter import messagebox


window = Tk()
window.title("Weather Forecast (by Volkan)")
window.minsize(width=425, height=400)
window.config(padx=20, pady=10, background="yellow")


def weather_func():
    if entry_city.get() != "":
        try:
            weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={entry_city.get()}&appid=de83d9fb4fd506c17d49bdb0e75f972c"

            resource = requests.get(weather_url)
            weather_info = resource.json()

            temp = str(round(weather_info["main"]["temp"] - 273.15, 2))

            # Label Result
            label_result = Label(text=temp + " °C", bg="yellow", font=('Helvetica', 15, 'italic'), fg="blue", padx=0, pady=10)
            label_result.place(x=160, y=220)

            print(temp)
        except:
            messagebox.showerror("Weather Error", "City name not found!")
    else:
        messagebox.showwarning(title="Hata!", message="Please enter city name.")


# Label Main Title
label_title = Label(text="Weather Forecast", bg="yellow", font=('Helvetica', 30, 'bold'), fg="black", padx=40, pady=20)
label_title.grid(row=1, column=0)

# Label City Title
label_title = Label(text="Enter city name:  ", bg="yellow", font=('Helvetica', 15, 'italic'), fg="blue", padx=0, pady=10)
label_title.grid(row=3, column=0)

# Entry City
entry_city = Entry(width=30, font=('Helvetica', 14, 'italic'), bg="powder blue")
entry_city.grid(row=4, column=0)
entry_city.focus()

# Button Search
encrypt_button = Button(text="Search", command=weather_func, font=('Helvetica', 12, 'italic'), bg="powder blue", padx=10, pady=5)
encrypt_button.place(x=160, y=180)

window.mainloop()