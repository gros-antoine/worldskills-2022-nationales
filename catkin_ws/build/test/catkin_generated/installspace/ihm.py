import rospy
import tkinter as tk
import tkinter.font as font
from std_msgs.msg import String

pub_interface = rospy.Publisher('pub_interface', String, queue_size=10)
rospy.init_node('pub_interface', anonymous=True)

top = tk.Tk()
top.geometry("1024x500")

state_aru = False

state = String()

def helloCallBack():
   pass

def start():
   global state_aru
   if not state_aru:
      Ledc.itemconfig(Leds[0], fill="green")
      Ledc.itemconfig(Leds[1], fill="#2E2E2E")
      Ledc.itemconfig(Leds[2], fill="#2E2E2E")
      Start.config(bg="green")
      Reset.config(bg="#979797")
      Stop.config(bg="#979797")
       
      state = "1"
      pub_interface.publish(state)

def stop():
   global state_aru
   if not state_aru:
      Ledc.itemconfig(Leds[0], fill="#2E2E2E")
      Ledc.itemconfig(Leds[1], fill="#2E2E2E")
      Ledc.itemconfig(Leds[2], fill="red")
      Start.config(bg="#979797")
      Reset.config(bg="#979797")
      Stop.config(bg="red")
      
      state = "3"
      pub_interface.publish(state)      

def reset():
   global state_aru
   if not state_aru:
      Ledc.itemconfig(Leds[0], fill="#2E2E2E")
      Ledc.itemconfig(Leds[1], fill="yellow")
      Ledc.itemconfig(Leds[2], fill="#2E2E2E")
      Start.config(bg="#979797")
      Reset.config(bg="yellow")
      Stop.config(bg="#979797")
      Start.config(state   = 'disabled')
      Reset.config(state   = 'disabled')
      Stop.config(state   = 'disabled')
      
      state = "2"
      pub_interface.publish(state)        

def aru():
   global state_aru
   if not state_aru:
      state_aru = True
      Ledc.itemconfig(Leds[0], fill="#2E2E2E")
      Ledc.itemconfig(Leds[1], fill="#2E2E2E")
      Ledc.itemconfig(Leds[2], fill="#2E2E2E")
      Start.config(bg="#979797")
      Reset.config(bg="#979797")
      Stop.config(bg="#979797")
      ARU.config(bg = "red", activebackground = "red")
      Start.config(state   = 'disabled')
      Reset.config(state   = 'disabled')
      Stop.config(state   = 'disabled')
      state = "4"
      pub_interface.publish(state) 
   else:
      state_aru = False
      ARU.config(bg="#2E2E2E", activebackground = "#2E2E2E")
      Start.config(state   = 'normal')
      Reset.config(state   = 'normal')
      Stop.config(state   = 'normal')
      stop()



myFont = font.Font(size=30)

Fp = tk.Frame(top)
F = tk.Frame(Fp)
F1 = tk.Frame(F)
F2 = tk.Frame(top)
Start = tk.Button(F1, text ="Start", width = 10, height = 1, bg = "#979797", activebackground = "green", command = start)
Reset = tk.Button(F1, text ="Reset", width = 10, height = 1, bg = "#979797", activebackground = "yellow", command = reset)
Stop = tk.Button(F1, text ="Stop", width = 10, height = 1, bg = "red", activebackground = "red", command = stop)
ARU = tk.Button(F2, text ="Arrêt\nd'Urgence", width = 10, height = 5, bg = "#2E2E2E", activebackground = "#2E2E2E", command = aru)
Ledc = tk.Canvas(F, width = 65, height = 200)
Label = tk.Label(Fp, text = "---- Interface Homme-Machine ---- \nLucas Si Larbi & Antoine Gros")

Leds = [Ledc.create_oval(10, 20, 55, 65, fill = "#2E2E2E", width = 7), Ledc.create_oval(10, 80, 55, 125, fill = "#2E2E2E", width = 7), Ledc.create_oval(10, 140, 55, 185, fill = "red", width = 7)]

Start['font'] = myFont
Stop['font'] = myFont
Reset['font'] = myFont
ARU['font'] = myFont

F1.pack(side = "left", expand=False)
Start.pack(side = "top")
Reset.pack(side = "top")
Stop.pack(side = "top")
Reset.pack(side = "top")
ARU.pack(side = "top")
Ledc.pack(side = "left")
F.pack(side = "top")
Label.pack(side = 'top', pady = 15, anchor = "w", padx = 26)
Fp.pack(side = "left", padx = 110, pady = 125, anchor = "nw")
F2.pack(side =  "left", padx = 60, expand=False)


top.mainloop()


