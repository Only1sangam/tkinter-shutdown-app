# Import the tkinter library & os module
from tkinter import *
import os

# Define 4 methods for our 4 buttons
def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 10")
def log_out():
    os.system("shutdown -l")
def shut_down():
    os.system("shutdown /s /t 1")

# Create window object
st = Tk()

# Add a title to the window
st.title("ShutDown App")

# Decides the size Width x Height
st.geometry("500x500")

# Configure certain options in widgets
st.config(bg="Blue")

# Creating r_button variable & use Button widget method on it
r_button = Button(st, text="Restart", font=("bold", 25), command=restart)

# Set the position and size of a r_button window using place method
r_button.place(x=150, y=50, height=50, width=200)

# Creating rt_button variable & use Button widget method on it
rt_button = Button(st, text="Restart Time", font=("bold", 25), command=restart_time)

# Set the position and size of a rt_button window using place method
rt_button.place(x=150, y=150, height=50, width=200)

# Creating lg_button variable & use Button widget method on it
lg_button = Button(st, text="Log Out", font=("bold", 25), command=log_out)

# Set the position and size of a lg_button window using place method
lg_button.place(x=150, y=250, height=50, width=200)

# Creating st_button variable & use Button widget method on it
st_button = Button(st, text="Shut Down", font=("bold", 25), command=shut_down)

# Set the position and size of a st_button window using place method
st_button.place(x=150, y=350, height=50, width=200)

# Start program
st.mainloop()
