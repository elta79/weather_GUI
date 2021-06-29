from tkinter import *
from tkinter import font
import requests

HEIGHT = 500
WIDTH = 600
bkPic = "/Users/emilyarnold/Desktop/Python/projects/weather_GUI/lighting.gif"#"weather_GUI/lighting.gif"

#852a207149c79fe4e28dd51cab085e2c
#api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
def get_weather(city):
    weather_key='852a207149c79fe4e28dd51cab085e2c'
    url='https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'} #can find params on openweathermap.org
    response = requests.get(url, params=params) #get API info
    #print(response.json()) #use to see which things we want for response ie ['weather'][0]['description']
    weather = response.json()#json converts to python dict

    label['text'] = format_response(weather)

def format_response(weather):
    try:  #try/except in case bad value
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        #final_str = str(name) + ' ' + str(desc) + ' ' + str(temp)
        final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s' %(name, desc, temp)
    except:
        final_str = 'Cannot retrieve info'

    return final_str

root = Tk()

canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = PhotoImage(file=bkPic)
background_label = Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = Frame(root, bg = "#ccffff", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = Button(frame, text='Get Weather', font=40, command=lambda: get_weather(entry.get())) #use lambda to update the entry and get current state of text box
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = Frame(root, bg = "#ccffff", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = Label(lower_frame, text="", font=('Courier', 20), justify=LEFT)
label.place(relwidth=1, relheight=1)


root.mainloop()
