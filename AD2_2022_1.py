import tkinter as ui
from tkinter import *
from tkinter import ttk
from Localtime import timezones_disponiveis
import pytz
from datetime import datetime
import math
window = ui.Tk()
window.title('Relogio GMT')
window.geometry("400x500")

listTimes = timezones_disponiveis()
lb_time=Label(window, text="Time Zones",bg='white')
lb_time.pack(expand=True, fill='both')
cb_time=ttk.Combobox(window,values=listTimes)
cb_time.set('America/Sao_Paulo')
cb_time.pack(expand=True, fill='both')

def update_zone():
    time = datetime.now()
    zone = cb_time.get()
    server_timezone = pytz.timezone(zone)
    timezone = time.now(server_timezone)
    new_zone = int(timezone.strftime("%H"))

    """Updating timezone hand per zone"""
    timezone_x = timezone_hand_len * math.sin(math.radians(new_zone * 15)) + center_x
    timezone_y = -1 * timezone_hand_len * math.cos(math.radians(new_zone * 15)) + center_y
    canvas.coords(timezone_hand, center_x, center_y, timezone_x, timezone_y)
    window.after(1000, update_zone)

"""btn_time=Button(window, text="Aplicar Time Zone Selecionado",command=update_zone)
btn_time.pack(expand=True, fill='both')"""
window.after(1, update_zone)


def update_clock():
    time = datetime.now()
    hours = int(time.strftime("%I"))
    minutes = int(time.strftime("%M"))
    seconds = int(time.strftime("%S"))


    """Updating hours hand per hours"""
    hours_x = hours_hand_len * math.sin(math.radians(hours * 30)) + center_x
    hours_y = -1 * hours_hand_len * math.cos(math.radians(hours * 30)) + center_y
    canvas.coords(hours_hand, center_x, center_y, hours_x, hours_y)

    """Updating minutes hand per ninutes"""
    minutes_x = minutes_hand_len * math.sin(math.radians(minutes * 6)) + center_x
    minutes_y = -1 * minutes_hand_len * math.cos(math.radians(minutes * 6)) + center_y
    canvas.coords(minutes_hand, center_x, center_y, minutes_x, minutes_y)

    """Updating seconds hand per second"""
    seconds_x = seconds_hand_len * math.sin(math.radians(seconds * 6)) + center_x
    seconds_y = -1 * seconds_hand_len * math.cos(math.radians(seconds * 6)) + center_y
    canvas.coords(seconds_hand, center_x, center_y, seconds_x, seconds_y)

    window.after(1000, update_clock)


canvas = ui.Canvas(window, width= 400, height=500, bg= "yellow")
canvas.pack(expand=True, fill='both')



"""
create background
"""

bg= ui.PhotoImage(file='B400.png')
canvas.create_image(200, 220, image=bg)


"""
Create clock hands
"""

center_x = 203
center_y = 217
seconds_hand_len = 100
minutes_hand_len = 85
hours_hand_len = 65
timezone_hand_len = 160

"""
Drawing clock hands
seconds hand
"""
seconds_hand = canvas.create_line(200, 200,
                                  200 + seconds_hand_len, 200 + seconds_hand_len,
                                  width=1.5, fill='red')


"""minute hand"""
minutes_hand = canvas.create_line(200, 200,
                                  200 + minutes_hand_len, 200 + minutes_hand_len,
                                  width= 3.5, fill ='black')


"""hours hand"""
hours_hand = canvas.create_line(200, 200,
                                200 + hours_hand_len, 200 + hours_hand_len,
                                width = 8, fill ='black')


"""time zone hand"""

timezone_hand = canvas.create_line(200, 200,
                                   200 + timezone_hand_len, 200 + timezone_hand_len,
                                   width = 3.5, fill = 'black')






update_clock()

window.mainloop()



