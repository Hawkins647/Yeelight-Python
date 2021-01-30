from yeelight import Bulb, RGBTransition, Flow
from yeelight.transitions import *
import tkinter
from tkinter import TOP

bulb_ip = "" # Please add your bulb's IP here.

bulb = Bulb(bulb_ip)

root = tkinter.Tk()
root.geometry("300x200")
root.title("Yeelight Bulb Operator")
root.resizable(0, 0)
root.iconbitmap("code_icon.ico")

disco_flow = Flow(
    count=0,  # Cycle forever.
    transitions=disco()
)

christmas_flow = Flow(
    count=0,  # Cycle forever.
    transitions=christmas()
)

alarm_flow = Flow(
    count=0,  # Cycle forever.
    transitions=alarm()
)

lsd_flow = Flow(
    count=0,  # Cycle forever.
    transitions=lsd()
)

police_flow = Flow(
    count=0,  # Cycle forever.
    transitions=police()
)

random_flow = Flow(
    count=0,  # Cycle forever.
    transitions=random_loop(count=9)
)

strobe_flow = Flow(
    count=0,  # Cycle forever.
    transitions=strobe_color()
)

police1_flow = Flow(
    count=0,  # Cycle forever.
    transitions=police2()
)

temp_flow = Flow(
    count=0,  # Cycle forever.
    transitions=temp()
)


def bulb_colour(colour):
    """Change the bulb's colour with the passed argument"""
    if colour == "red":
        bulb.set_rgb(255, 0, 0)
    if colour == "dark blue":
        bulb.set_rgb(51, 51, 255)
    if colour == "light blue":
        bulb.set_rgb(0, 255, 255)
    if colour == "orange":
        bulb.set_rgb(255, 128, 0)
    if colour == "blue":
        bulb.set_rgb(51, 153, 255)
    if colour == "yellow":
        bulb.set_rgb(255, 255, 0)
    if colour == "light green":
        bulb.set_rgb(0, 255, 0)
    if colour == "dark green":
        bulb.set_rgb(0, 102, 0)
    if colour == "pink":
        bulb.set_rgb(255, 0, 255)
    if colour == "purple":
        bulb.set_rgb(255, 153, 255)
    if colour == "white":
        bulb.set_rgb(255, 255, 255)
    if colour == "hot pink":
        bulb.set_rgb(255, 0, 127)


def flow_window():
    """Open a window with various flow options."""
    bulb_flow_window = tkinter.Toplevel()
    bulb_flow_window.title("Flow")
    bulb_flow_window.geometry("350x200")
    bulb_flow_window.resizable(0, 0)
    bulb_flow_window.iconbitmap("code_icon.ico")

    options_colour_frame = tkinter.Frame(bulb_flow_window, bg="grey")
    options_colour_frame.pack(padx=5, pady=5)

    disco_button = tkinter.Button(options_colour_frame, text="Disco", font=("Rubrik", 10), command=lambda: bulb.start_flow(disco_flow), width=8)
    disco_button.grid(row=0, column=0, padx=5, pady=5)

    christmas_button = tkinter.Button(options_colour_frame, text="Christmas", font=("Rubrik", 10), command=lambda: bulb.start_flow(christmas_flow), width=8)
    christmas_button.grid(row=0, column=1, padx=5, pady=5)

    alarm_button = tkinter.Button(options_colour_frame, text="Alarm", font=("Rubrik", 10), command=lambda: bulb.start_flow(alarm_flow), width=8,)
    alarm_button.grid(row=0, column=2, padx=5, pady=5)

    lsd_button = tkinter.Button(options_colour_frame, text="LSD", font=("Rubrik", 10), command=lambda: bulb.start_flow(lsd_flow), width=8)
    lsd_button.grid(row=1, column=0, padx=5, pady=5)

    police_button = tkinter.Button(options_colour_frame, text="Police", font=("Rubrik", 10), command=lambda: bulb.start_flow(police_flow), width=8)
    police_button.grid(row=1, column=1, padx=5, pady=5)

    random_button = tkinter.Button(options_colour_frame, text="Random", font=("Rubrik", 10), command=lambda: bulb.start_flow(random_flow), width=8)
    random_button.grid(row=1, column=2, padx=5, pady=5)

    strobe_button = tkinter.Button(options_colour_frame, text="Strobe", font=("Rubrik", 10), command=lambda: bulb.start_flow(strobe_flow), width=8)
    strobe_button.grid(row=2, column=0, padx=5, pady=5)

    temp_button = tkinter.Button(options_colour_frame, text="Temp", font=("Rubrik", 10), command=lambda: bulb.start_flow(temp_flow), width=8)
    temp_button.grid(row=2, column=1, padx=5, pady=5)

    police1_button = tkinter.Button(options_colour_frame, text="Police 2", font=("Rubrik", 10), command=lambda: bulb.start_flow(police1_flow), width=8)
    police1_button.grid(row=2, column=2, padx=5, pady=5)

    flow_off_button = tkinter.Button(bulb_flow_window, text="Flow Off", font=("Rubrik", 10), command=bulb.stop_flow, width=30)
    flow_off_button.pack(side=TOP)

    bulb_flow_window.mainloop()


def bulb_brightness_window1():
    """Open a window with options to change the bulb's brightness"""
    bulb_brightness_window = tkinter.Toplevel()
    bulb_brightness_window.title("Colour Change")
    bulb_brightness_window.geometry("350x200")
    bulb_brightness_window.resizable(0, 0)
    bulb_brightness_window.iconbitmap("code_icon.ico")

    brightness_label = tkinter.Label(bulb_brightness_window, text="Please select your brightness percentage: ", font=("Rubrik", 10))
    brightness_label.pack(padx=5, pady=5)

    button_frame = tkinter.Frame(bulb_brightness_window, bg="grey")
    button_frame.pack(padx=5, pady=5)

    one_button = tkinter.Button(button_frame, text="1%", font=("Rubrik", 10), width=7, command=lambda: bulb.set_brightness(1))
    one_button.grid(row=0, column=0, padx=5, pady=5)

    fifteen_button = tkinter.Button(button_frame, text="15%", font=("Rubrik", 10), width=7, command=lambda: bulb.set_brightness(15))
    fifteen_button.grid(row=0, column=1, padx=5, pady=5)

    twentyfive_button = tkinter.Button(button_frame, text="25%", font=("Rubrik", 10), width=7, command=lambda: bulb.set_brightness(25))
    twentyfive_button.grid(row=1, column=0, padx=5, pady=5)

    fifty_button = tkinter.Button(button_frame, text="50%", font=("Rubrik", 10), width=7, command=lambda: bulb.set_brightness(50))
    fifty_button.grid(row=1, column=1, padx=5, pady=5)

    seventyfive_button = tkinter.Button(button_frame, text="75%", font=("Rubrik", 10), width=7, command=lambda: bulb.set_brightness(75))
    seventyfive_button.grid(row=2, column=0, padx=5, pady=5)

    onehundred_button = tkinter.Button(button_frame, text="100%", font=("Rubrik", 10), width=7, command=lambda: bulb.set_brightness(100))
    onehundred_button.grid(row=2, column=1, padx=5, pady=5)

    bulb_brightness_window.mainloop()


def bulb_colour_window1():
    """Open a window with options to change the bulb's colour"""
    bulb_colour_window = tkinter.Toplevel()
    bulb_colour_window.title("Colour Change")
    bulb_colour_window.geometry("350x200")
    bulb_colour_window.resizable(0, 0)
    bulb_colour_window.iconbitmap("code_icon.ico")

    options_colour_frame = tkinter.Frame(bulb_colour_window, bg="grey")
    options_colour_frame.pack(padx=5, pady=5)

    red_button = tkinter.Button(options_colour_frame, text="Red", font=("Rubrik", 10), command=lambda: bulb_colour(colour="red"), width=8, bg="red")
    red_button.grid(row=0, column=0, padx=5, pady=5)

    dark_blue_button = tkinter.Button(options_colour_frame, text="Dark Blue", font=("Rubrik", 10), command=lambda: bulb_colour(colour="dark blue"), width=8, bg="dark blue")
    dark_blue_button.grid(row=0, column=1, padx=5, pady=5)

    blue_button = tkinter.Button(options_colour_frame, text="Turquoise", font=("Rubrik", 10), command=lambda: bulb_colour(colour="light blue"), width=8, bg="turquoise")
    blue_button.grid(row=0, column=2, padx=5, pady=5)

    orange_button = tkinter.Button(options_colour_frame, text="Orange", font=("Rubrik", 10), command=lambda: bulb_colour(colour="orange"), width=8, bg="orange")
    orange_button.grid(row=1, column=0, padx=5, pady=5)

    blue_button1 = tkinter.Button(options_colour_frame, text="Blue", font=("Rubrik", 10), command=lambda: bulb_colour(colour="blue"), width=8, bg="blue")
    blue_button1.grid(row=1, column=1, padx=5, pady=5)

    yellow_button = tkinter.Button(options_colour_frame, text="Yellow", font=("Rubrik", 10), command=lambda: bulb_colour(colour="yellow"), width=8, bg="yellow")
    yellow_button.grid(row=1, column=2, padx=5, pady=5)

    light_green_button = tkinter.Button(options_colour_frame, text="Light Green", font=("Rubrik", 10), command=lambda: bulb_colour(colour="light green"), width=8, bg="light green")
    light_green_button.grid(row=2, column=0, padx=5, pady=5)

    dark_green_button = tkinter.Button(options_colour_frame, text="Dark Green", font=("Rubrik", 10), command=lambda: bulb_colour(colour="dark green"), width=8, bg="dark green")
    dark_green_button.grid(row=2, column=1, padx=5, pady=5)

    pink_button = tkinter.Button(options_colour_frame, text="Pink", font=("Rubrik", 10), command=lambda: bulb_colour(colour="pink"), width=8, bg="pink")
    pink_button.grid(row=2, column=2, padx=5, pady=5)

    purple_button = tkinter.Button(options_colour_frame, text="Purple", font=("Rubrik", 10), command=lambda: bulb_colour(colour="purple"), width=8, bg="purple")
    purple_button.grid(row=3, column=0, padx=5, pady=5)

    white_button = tkinter.Button(options_colour_frame, text="White", font=("Rubrik", 10), command=lambda: bulb_colour(colour="white"), width=8)
    white_button.grid(row=3, column=1, padx=5, pady=5)

    hot_pink_button = tkinter.Button(options_colour_frame, text="Hot Pink", font=("Rubrik", 10), command=lambda: bulb_colour(colour="hot pink"), width=8, bg="hot pink")
    hot_pink_button.grid(row=3, column=2, padx=5, pady=5)

    bulb_colour_window.mainloop()


title_label = tkinter.Label(root, text="Bulb Operator", font=("Rubrik", 25))
title_label.pack(padx=5, pady=5)

options_frame = tkinter.Frame(root, bg="grey")
options_frame.pack(padx=5, pady=5)

bulb_on_button = tkinter.Button(options_frame, text="Turn On", font=("Rubrik", 12), command=bulb.turn_on, width=8)
bulb_on_button.grid(row=0, column=0, padx=5, pady=5)

bulb_off_button = tkinter.Button(options_frame, text="Turn Off", font=("Rubrik", 12), command=bulb.turn_off, width=8)
bulb_off_button.grid(row=0, column=1, padx=5, pady=5)

bulb_colour_button = tkinter.Button(options_frame, text="Colours", font=("Rubrik", 12), command=bulb_colour_window1, width=8)
bulb_colour_button.grid(row=1, column=0, padx=5, pady=5)

bulb_brightness_button = tkinter.Button(options_frame, text="Brightness", font=("Rubrik", 12), command=bulb_brightness_window1, width=8)
bulb_brightness_button.grid(row=1, column=1, padx=5, pady=5)

flow_on_button = tkinter.Button(options_frame, text="Flow", font=("Rubrik", 12), command=flow_window, width=8)
flow_on_button.grid(row=2, column=0, padx=5, pady=5)


root.mainloop()
