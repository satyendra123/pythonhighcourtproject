import tkinter as tk
import pymysql
import serial
import time
from tkinter import font
from PIL import Image, ImageTk
from threading import Timer
display_1_welcome = 0
display_2_welcome = 0
display_3_welcome = 0
display_4_welcome = 0
display_5_welcome = 0
display_6_welcome = 0
display_7_welcome = 0
display_8_welcome = 0
display_9_welcome = 0
display_10_welcome = 0
display_1_maint = 0
display_2_maint = 0
display_3_maint = 0
display_4_maint = 0
display_5_maint = 0
display_6_maint = 0
display_7_maint = 0
display_8_maint = 0
display_9_maint = 0
display_10_maint = 0
root = tk.Tk()
root.title("Houston Systems")
root.geometry("600x250")
root.resizable(True, True)


def update_display_data():
    global display_1_welcome
    global display_2_welcome
    global display_3_welcome
    global display_4_welcome
    global display_5_welcome
    global display_6_welcome
    global display_7_welcome
    global display_8_welcome
    global display_9_welcome
    global display_10_welcome

    global display_1_maint
    global display_2_maint
    global display_3_maint
    global display_4_maint
    global display_5_maint
    global display_6_maint
    global display_7_maint
    global display_8_maint
    global display_9_maint
    global display_10_maint

    try:
        conn_1 = pymysql.connect(host="10.25.197.201", user="housys", password="housys", database="housys")
        y = conn_1.cursor()
        sql = """SELECT vacancy FROM vacancy_status WHERE system_id='01';"""
        y.execute(sql)
        system1_data = y.fetchall()[0][0]

        sql = """SELECT vacancy FROM vacancy_status WHERE system_id='02';"""
        y.execute(sql)
        system2_data = y.fetchall()[0][0]

        sql = """SELECT vacancy FROM vacancy_status WHERE system_id='03';"""
        y.execute(sql)
        system3_data = y.fetchall()[0][0]

        sql = """SELECT vacancy FROM vacancy_status WHERE system_id='04';"""
        y.execute(sql)
        system4_data = y.fetchall()[0][0]

        sql = """SELECT vacancy FROM vacancy_status WHERE system_id='05';"""
        y.execute(sql)
        system5_data = y.fetchall()[0][0]

        sql = """SELECT vacancy FROM vacancy_status WHERE system_id='06';"""
        y.execute(sql)
        system6_data = y.fetchall()[0][0]

        sql = """SELECT vacancy FROM vacancy_status WHERE system_id='07';"""
        y.execute(sql)
        system7_data = y.fetchall()[0][0]

        sql = """SELECT vacancy FROM vacancy_status WHERE system_id='08';"""
        y.execute(sql)
        system8_data = y.fetchall()[0][0]

        sql = """SELECT vacancy FROM vacancy_status WHERE system_id='09';"""
        y.execute(sql)
        system9_data = y.fetchall()[0][0]

        sql = """SELECT vacancy FROM vacancy_status WHERE system_id='10';"""
        y.execute(sql)
        system10_data = y.fetchall()[0][0]
        y.close()

        if  (display_1_welcome == 0 and display_1_maint == 0):
            send_to_rs485(f"@ID1@STDFDATA@DX0@SE{system1_data}@SS")
        
        if (display_2_welcome == 0 and display_2_maint == 0):
            send_to_rs485(f"@ID2@STDFDATA@DX0@SE{system2_data}@SS")

        if (display_3_welcome == 0 and display_3_maint == 0):
            send_to_rs485(f"@ID3@STDFDATA@DX0@SE{system3_data}@SS")
        
        if (display_4_welcome == 0 and display_4_maint == 0):
            send_to_rs485(f"@ID4@STDFDATA@DX0@SE{system4_data}@SS")
        
        if (display_5_welcome == 0 and display_5_maint == 0):
            send_to_rs485(f"@ID5@STDFDATA@DX0@SE{system5_data}@SS")
        
        if (display_6_welcome == 0 and display_6_maint == 0):
            send_to_rs485(f"@ID6@STDFDATA@DX0@SE{system6_data}@SS")
        
        if (display_7_welcome == 0 and display_7_maint == 0):
            send_to_rs485(f"@ID7@STDFDATA@DX0@SE{system7_data}@SS")
        
        if (display_8_welcome == 0 and display_8_maint == 0):
            send_to_rs485(f"@ID8@STDFDATA@DX0@SE{system8_data}@SS")
        
        if (display_9_welcome == 0 and display_9_maint == 0):
            send_to_rs485(f"@ID9@STDFDATA@DX0@SE{system9_data}@SS")
        
        if (display_10_welcome == 0 and display_10_maint == 0):
            send_to_rs485(f"@ID10@STDFDATA@DX0@SE{system10_data}@SS")
           
        system_total = system1_data + system2_data + system3_data + system4_data + system5_data + system6_data + system7_data + system8_data + system9_data + system10_data

        send_to_rs485(f"@ID11@STDFDATA@DX0@SE{system1_data + system2_data }@SS", ser_com6)
        send_to_rs485(f"@ID12@STDFDATA@DX0@SE{system3_data + system4_data }@SS", ser_com6)
        send_to_rs485(f"@ID13@STDFDATA@DX0@SE{system5_data + system6_data }@SS", ser_com6)
        send_to_rs485(f"@ID14@STDFDATA@DX0@SE{system7_data + system8_data }@SS", ser_com6)
        send_to_rs485(f"@ID15@STDFDATA@DX0@SE{system9_data + system10_data }@SS", ser_com6)
        send_to_rs485(f"@ID16@STDFDATA@DX20@SE{system_total}@SS", ser_com6)

        time.sleep(5)
        # root.after(25, update_display_data)
    except:
        time.sleep(5)

while True:
    try:
        conn = pymysql.connect(host="10.25.197.201", user="housys", password="housys", database="housys")
        x = conn.cursor()
        ser_com5 = serial.Serial('COM5', baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=10)
        ser_com6 = serial.Serial('COM6', baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=10)
        x.close()
        break
    except Exception as e:
        print("Not able to connect to database / RJ 45 port")
        time.sleep(10)
def send_to_rs485(data, ser=ser_com5):
    ser.write(data.encode())
    time.sleep(1.5)


def on_checkbox_checked(checkbox_var, display_id, message):
    global display_1_welcome
    global display_2_welcome
    global display_3_welcome
    global display_4_welcome
    global display_5_welcome
    global display_6_welcome
    global display_7_welcome
    global display_8_welcome
    global display_9_welcome
    global display_10_welcome

    if display_id == "ID1" and display_1_welcome == 0:
        send_to_rs485("@ID1@STMSAPP@DX96@SEWELCOME@SS")
        display_1_welcome = 1
    elif display_id == "ID1" and display_1_welcome == 1:
        send_to_rs485("@ID1@STMSAPP@DX96@SEAVAILABLE @SS")
        display_1_welcome = 0

    if display_id == "ID2" and display_2_welcome == 0:
        send_to_rs485("@ID2@STMSAPP@DX96@SEWELCOME@SS")
        display_2_welcome = 1
    elif display_id == "ID2" and display_2_welcome == 1:
        send_to_rs485("@ID2@STMSAPP@DX96@SEAVAILABLE @SS")
        display_2_welcome = 0
    
    if display_id == "ID3" and display_3_welcome == 0:
        send_to_rs485("@ID3@STMSAPP@DX96@SEWELCOME@SS")
        display_3_welcome = 1
    elif display_id == "ID3" and display_3_welcome == 1:
        send_to_rs485("@ID3@STMSAPP@DX96@SEAVAILABLE @SS")
        display_3_welcome = 0
    
    if display_id == "ID4" and display_4_welcome == 0:
        send_to_rs485("@ID4@STMSAPP@DX96@SEWELCOME@SS")
        display_4_welcome = 1
    elif display_id == "ID4" and display_4_welcome == 1:
        send_to_rs485("@ID4@STMSAPP@DX96@SEAVAILABLE @SS")
        display_4_welcome = 0
    
    if display_id == "ID5" and display_5_welcome == 0:
        send_to_rs485("@ID5@STMSAPP@DX96@SEWELCOME@SS")
        display_5_welcome = 1
    elif display_id == "ID5" and display_5_welcome == 1:
        send_to_rs485("@ID5@STMSAPP@DX96@SEAVAILABLE @SS")
        display_5_welcome = 0
    
    if display_id == "ID6" and display_6_welcome == 0:
        send_to_rs485("@ID6@STMSAPP@DX96@SEWELCOME@SS")
        display_6_welcome = 1
    elif display_id == "ID6" and display_6_welcome == 1:
        send_to_rs485("@ID6@STMSAPP@DX96@SEAVAILABLE @SS")
        display_6_welcome = 0
    
    if display_id == "ID7" and display_7_welcome == 0:
        send_to_rs485("@ID7@STMSAPP@DX96@SEWELCOME@SS")
        display_7_welcome = 1
    elif display_id == "ID7" and display_7_welcome == 1:
        send_to_rs485("@ID7@STMSAPP@DX96@SEAVAILABLE @SS")
        display_7_welcome = 0
    
    if display_id == "ID8" and display_8_welcome == 0:
        send_to_rs485("@ID8@STMSAPP@DX96@SEWELCOME@SS")
        display_8_welcome = 1
    elif display_id == "ID8" and display_8_welcome == 1:
        send_to_rs485("@ID8@STMSAPP@DX96@SEAVAILABLE @SS")
        display_8_welcome = 0
    
    if display_id == "ID9" and display_9_welcome == 0:
        send_to_rs485("@ID9@STMSAPP@DX96@SEWELCOME@SS")
        display_9_welcome = 1
    elif display_id == "ID9" and display_9_welcome == 1:
        send_to_rs485("@ID9@STMSAPP@DX96@SEAVAILABLE @SS")
        display_9_welcome = 0
    
    if display_id == "ID10" and display_10_welcome == 0:
        send_to_rs485("@ID10@STMSAPP@DX96@SEWELCOME@SS")
        display_10_welcome = 1
    elif display_id == "ID10" and display_10_welcome == 1:
        send_to_rs485("@ID10@STMSAPP@DX96@SEAVAILABLE @SS")
        display_10_welcome = 0


def on_checkbox_checked1(checkbox_var, display_id, message):

    global display_1_maint
    global display_2_maint
    global display_3_maint
    global display_4_maint
    global display_5_maint
    global display_6_maint 
    global display_7_maint
    global display_8_maint
    global display_9_maint
    global display_10_maint
    

    if display_id == "ID1" and display_1_maint == 0:
        send_to_rs485("@ID1@STMSAPP@DX96@SEMAINTENANCE@SS")
        display_1_maint = 1
    elif display_id == "ID1" and display_1_maint == 1:
        send_to_rs485("@ID1@STMSAPP@DX96@SEAVAILABLE @SS")
        display_1_maint = 0
    

    if display_id == "ID2" and display_2_maint == 0:
        send_to_rs485("@ID2@STMSAPP@DX96@SEMAINTENANCE@SS")
        display_2_maint = 1
    elif display_id == "ID2" and display_2_maint == 1:
        send_to_rs485("@ID2@STMSAPP@DX96@SEAVAILABLE @SS")
        display_2_maint = 0
    
    if display_id == "ID3" and display_3_maint == 0:
        send_to_rs485("@ID3@STMSAPP@DX96@SEMAINTENANCE@SS")
        display_3_maint = 1
    elif display_id == "ID3" and display_3_maint == 1:
        send_to_rs485("@ID3@STMSAPP@DX96@SEAVAILABLE @SS")
        display_3_maint = 0

    if display_id == "ID4" and display_4_maint == 0:
        send_to_rs485("@ID4@STMSAPP@DX96@SEMAINTENANCE@SS")
        display_4_maint = 1
    elif display_id == "ID4" and display_4_maint == 1:
        send_to_rs485("@ID4@STMSAPP@DX96@SEAVAILABLE @SS")
        display_4_maint = 0
    
    if display_id == "ID5" and display_5_maint == 0:
        send_to_rs485("@ID5@STMSAPP@DX96@SEMAINTENANCE@SS")
        display_5_maint = 1
    elif display_id == "ID5" and display_5_maint == 1:
        send_to_rs485("@ID5@STMSAPP@DX96@SEAVAILABLE @SS")
        display_5_maint = 0
    
    if display_id == "ID6" and display_6_maint == 0:
        send_to_rs485("@ID6@STMSAPP@DX96@SEMAINTENANCE@SS")
        display_6_maint = 1
    elif display_id == "ID6" and display_6_maint == 1:
        send_to_rs485("@ID6@STMSAPP@DX96@SEAVAILABLE @SS")
        display_6_maint = 0
    
    if display_id == "ID7" and display_7_maint == 0:
        send_to_rs485("@ID7@STMSAPP@DX96@SEMAINTENANCE@SS")
        display_7_maint = 1
    elif display_id == "ID7" and display_7_maint == 1:
        send_to_rs485("@ID7@STMSAPP@DX96@SEAVAILABLE @SS")
        display_7_maint = 0
    
    if display_id == "ID8" and display_8_maint == 0:
        send_to_rs485("@ID8@STMSAPP@DX96@SEMAINTENANCE@SS")
        display_8_maint = 1
    elif display_id == "ID8" and display_8_maint == 1:
        send_to_rs485("@ID8@STMSAPP@DX96@SEAVAILABLE @SS")
        display_8_maint = 0
    
    if display_id == "ID9" and display_9_maint == 0:
        send_to_rs485("@ID9@STMSAPP@DX96@SEMAINTENANCE@SS")
        display_9_maint = 1
    elif display_id == "ID9" and display_9_maint == 1:
        send_to_rs485("@ID9@STMSAPP@DX96@SEAVAILABLE @SS")
        display_9_maint = 0
    
    if display_id == "ID10" and display_10_maint == 0:
        send_to_rs485("@ID10@STMSAPP@DX96@SEMAINTENANCE@SS")
        display_10_maint = 1
    elif display_id == "ID10" and display_10_maint == 1:
        send_to_rs485("@ID10@STMSAPP@DX96@SEAVAILABLE @SS")
        display_10_maint = 0

def clear_buttons(new_window):
    for widget in new_window.winfo_children():
        widget.destroy()


def display_buttons(new_window):
    # Load the image for the new window
    conn = pymysql.connect(host="10.25.197.201", user="housys", password="housys", database="housys")
    x = conn.cursor()
    sql = """SELECT vacancy FROM vacancy_status WHERE system_id='01';"""
    x.execute(sql)
    system1_data = x.fetchall()[0][0]
    sql = """SELECT vacancy FROM vacancy_status WHERE system_id='02';"""
    x.execute(sql)
    system2_data = x.fetchall()[0][0]
    sql = """SELECT vacancy FROM vacancy_status WHERE system_id='03';"""
    x.execute(sql)
    system3_data = x.fetchall()[0][0]
    sql = """SELECT vacancy FROM vacancy_status WHERE system_id='04';"""
    x.execute(sql)
    system4_data = x.fetchall()[0][0]
    sql = """SELECT vacancy FROM vacancy_status WHERE system_id='05';"""
    x.execute(sql)
    system5_data = x.fetchall()[0][0]
    sql = """SELECT vacancy FROM vacancy_status WHERE system_id='06';"""
    x.execute(sql)
    system6_data = x.fetchall()[0][0]
    sql = """SELECT vacancy FROM vacancy_status WHERE system_id='07';"""
    x.execute(sql)
    system7_data = x.fetchall()[0][0]
    sql = """SELECT vacancy FROM vacancy_status WHERE system_id='08';"""
    x.execute(sql)
    system8_data = x.fetchall()[0][0]
    sql = """SELECT vacancy FROM vacancy_status WHERE system_id='09';"""
    x.execute(sql)
    system9_data = x.fetchall()[0][0]
    sql = """SELECT vacancy FROM vacancy_status WHERE system_id='10';"""
    x.execute(sql)
    system10_data = x.fetchall()[0][0]
    x.close()
    system11_total = system1_data + system2_data + system3_data + system4_data + system5_data + system6_data + system7_data + system8_data + system9_data + system10_data
    test_new_window = tk.PhotoImage(file="logo 4.png")
    label_new_window = tk.Label(new_window, image=test_new_window)
    label_new_window.image = test_new_window
    label_new_window.pack()

    test_new_window = ImageTk.PhotoImage(file="sedan-car-front1.png")
    label_new_window = tk.Label(new_window, image=test_new_window)
    label_new_window.image = test_new_window
    label_new_window.place(x=100, y=340)  # Position image

    test_new_window = ImageTk.PhotoImage(file="next.png")
    label_new_window = tk.Label(new_window, image=test_new_window)
    label_new_window.image = test_new_window
    label_new_window.place(x=210, y=340)

    test_new_window = ImageTk.PhotoImage(file="next.png")
    label_new_window = tk.Label(new_window, image=test_new_window)
    label_new_window.image = test_new_window
    label_new_window.place(x=650, y=340)
    #for car2
    test_new_window = ImageTk.PhotoImage(file="sedan-car-front1.png")
    label_new_window = tk.Label(new_window, image=test_new_window)
    label_new_window.image = test_new_window
    label_new_window.place(x=330, y=340)  # Position image
    #for car3
    test_new_window = ImageTk.PhotoImage(file="sedan-car-front1.png")
    label_new_window = tk.Label(new_window, image=test_new_window)
    label_new_window.image = test_new_window
    label_new_window.place(x=400, y=340)  # Position image
    #for car4
    test_new_window = ImageTk.PhotoImage(file="sedan-car-front1.png")
    label_new_window = tk.Label(new_window, image=test_new_window)
    label_new_window.image = test_new_window
    label_new_window.place(x=500, y=340)  # Position image
    #for car5
    test_new_window = ImageTk.PhotoImage(file="sedan-car-front1.png")
    label_new_window = tk.Label(new_window, image=test_new_window)
    label_new_window.image = test_new_window
    label_new_window.place(x=840, y=340)  # Position image  
    #for car6
    test_new_window = ImageTk.PhotoImage(file="sedan-car-front1.png")
    label_new_window = tk.Label(new_window, image=test_new_window)
    label_new_window.image = test_new_window
    label_new_window.place(x=920, y=340)  # Position image  
    #for car7
    test_new_window = ImageTk.PhotoImage(file="sedan-car-front1.png")
    label_new_window = tk.Label(new_window, image=test_new_window)
    label_new_window.image = test_new_window
    label_new_window.place(x=1020, y=340)  # Position image
    #for car8
    test_new_window = ImageTk.PhotoImage(file="sedan-car-front1.png")
    label_new_window = tk.Label(new_window, image=test_new_window)
    label_new_window.image = test_new_window
    label_new_window.place(x=1120, y=340)

    # for display to use car1
    display_box3_new_window = tk.Label(new_window, text=f"LIFT1E={system2_data}", relief=tk.SUNKEN, width=12, height=4)
    display_box3_new_window.place(x=80, y=380)
    display_box3_new_window['bg']='#8ABF62'
        # for display to use car2,3
    display_box4_new_window = tk.Label(new_window, text=f"LIFTID={system2_data}", relief=tk.SUNKEN, width=12, height=4)
    display_box4_new_window.place(x=300, y=380)
    display_box4_new_window['bg']='#8ABF62'

    display_box5_new_window = tk.Label(new_window, text=f"LIFT1C={system2_data}", relief=tk.SUNKEN, width=12, height=4)
    display_box5_new_window.place(x=390, y=380)
    display_box5_new_window['bg']='#8ABF62'
    #for controller room
    display_box6_new_window = tk.Label(new_window, text="CONTROOL ROOM", relief=tk.SUNKEN, width=37, height=4)
    display_box6_new_window.place(x=550, y=380)
    display_box6_new_window['bg']='#E59F65'
    # for display to use car2,3
    display_box7_new_window = tk.Label(new_window, text=f"LIFT1B={system1_data}", relief=tk.SUNKEN, width=12, height=4)
    display_box7_new_window.place(x=810, y=380)
    display_box7_new_window['bg']='#8ABF62'

    display_box8_new_window = tk.Label(new_window, text=f"LIFT1A={system1_data}", relief=tk.SUNKEN, width=12, height=4)
    display_box8_new_window.place(x=900, y=380)
    display_box8_new_window['bg']='#8ABF62'

    display_box9_new_window = tk.Label(new_window, text="EXIT", relief=tk.SUNKEN, width=12, height=4)
    display_box9_new_window.place(x=1100, y=380)
    display_box9_new_window['bg']='#8ABF62'

    # for main Display
    bold_font = font.Font(family="Helvetica", size=16, weight="bold")
    label_new_window = tk.Label(new_window, text="DELHI HIGH COURT PARKING AVAILABILITY STATUS", font=bold_font)
    label_new_window.pack()
    label_new_window.place(x=400, y=10)

    # test_new_window = tk.PhotoImage(file="logo 2.png")
    label_new_window = tk.Label(new_window, image=test_new_window)
    label_new_window.image = test_new_window
    label_new_window.place(x=10, y=10)

    bold_font = font.Font(family="Helvetica", size=13, weight="bold")
    label_new_window = tk.Label(new_window, text=f"BAY 1 AVAILABLE: {system1_data+system2_data}",font=bold_font)
    label_new_window.pack()
    label_new_window.place(x=140, y=60)
    bold_font = font.Font(family="Helvetica", size=13, weight="bold")
    label_new_window = tk.Label(new_window, text=f"BAY 1-1A :{system1_data}",font=bold_font)
    label_new_window.pack()
    label_new_window.place(x=140, y=85)
    bold_font = font.Font(family="Helvetica", size=13, weight="bold")
    label_new_window = tk.Label(new_window, text=f"BAY 1-1B :{system1_data}",   font=bold_font)
    label_new_window.pack()
    label_new_window.place(x=140, y=110)
    bold_font = font.Font(family="Helvetica", size=13, weight="bold")
    label_new_window = tk.Label(new_window, text=f"BAY 1-1C :{system2_data}", font=bold_font)
    label_new_window.pack()
    label_new_window.place(x=140, y=138)
    bold_font = font.Font(family="Helvetica", size=13, weight="bold")
    label_new_window = tk.Label(new_window, text=f"BAY 1-1D :{system2_data}",font=bold_font)
    label_new_window.pack()
    label_new_window.place(x=140, y=165)
    bold_font = font.Font(family="Helvetica", size=13, weight="bold")
    label_new_window = tk.Label(new_window, text=f"BAY 1-1E :{system2_data}",font=bold_font)
    label_new_window.pack()
    label_new_window.place(x=140, y=195)
    bold_font = font.Font(family="Helvetica", size=13, weight="bold")
    label_new_window = tk.Label(new_window, text=f"BAY 2 AVAILABLE: {system3_data + system4_data}",font=bold_font)
    label_new_window.pack()
    label_new_window.place(x=350, y=60)
    bold_font = font.Font(family="Helvetica", size=13, weight="bold")
    label_new_window = tk.Label(new_window, text=f"BAY 2-3A: {system3_data}",font=bold_font)
    label_new_window.pack()
    label_new_window.place(x=350, y=85)
    bold_font = font.Font(family="Helvetica", size=13, weight="bold")
    label_new_window = tk.Label(new_window, text=f"BAY 2-3B: {system3_data}",font=bold_font)
    label_new_window.pack()
    label_new_window.place(x=350, y=122)
    bold_font = font.Font(family="Helvetica", size=13, weight="bold")
    label_new_window = tk.Label(new_window, text=f"BAY 2-3C: {system4_data}",font=bold_font)
    label_new_window.pack()
    label_new_window.place(x=350, y=160)
    bold_font = font.Font(family="Helvetica", size=13, weight="bold")
    label_new_window = tk.Label(new_window, text=f"BAY 2-3D: {system4_data}",font=bold_font)
    label_new_window.pack()
    label_new_window.place(x=350, y=195)
    bold_font = font.Font(family="Helvetica", size=13, weight="bold")
    label_new_window = tk.Label(new_window, text=f"BAY 3 AVAILABLE: {system5_data + system6_data}",font=bold_font)
    label_new_window.pack()
    label_new_window.place(x=540, y=60)
    bold_font = font.Font(family="Helvetica", size=13, weight="bold")
    label_new_window = tk.Label(new_window, text=f"BAY 3-2A: {system5_data}",font=bold_font)
    label_new_window.pack()
    label_new_window.place(x=540, y=85)
    bold_font = font.Font(family="Helvetica", size=13, weight="bold")
    label_new_window = tk.Label(new_window, text=f"BAY 3-2B: {system5_data}",font=bold_font)
    label_new_window.pack()
    label_new_window.place(x=540, y=112)
    bold_font = font.Font(family="Helvetica", size=13, weight="bold")
    label_new_window = tk.Label(new_window, text=f"BAY 3-2C: {system6_data}",font=bold_font)
    label_new_window.pack()
    label_new_window.place(x=540, y=140)
    bold_font = font.Font(family="Helvetica", size=13, weight="bold")
    label_new_window = tk.Label(new_window, text=f"BAY 4 AVAILABLE: {system7_data + system8_data}",font=bold_font)
    label_new_window.pack()
    label_new_window.place(x=780, y=60)
    bold_font = font.Font(family="Helvetica", size=13, weight="bold")
    label_new_window = tk.Label(new_window, text=f"BAY 4-5A: {system7_data}",font=bold_font)
    label_new_window.pack()
    label_new_window.place(x=780, y=85)
    bold_font = font.Font(family="Helvetica", size=13, weight="bold")
    label_new_window = tk.Label(new_window, text=f"BAY 4-5B: {system7_data}",font=bold_font)
    label_new_window.pack()
    label_new_window.place(x=780, y=113)
    bold_font = font.Font(family="Helvetica", size=13, weight="bold")
    label_new_window = tk.Label(new_window, text=f"BAY 4-5C: {system8_data}",font=bold_font)
    label_new_window.pack()
    label_new_window.place(x=780, y=140)
    bold_font = font.Font(family="Helvetica", size=13, weight="bold")
    label_new_window = tk.Label(new_window, text=f"BAY 4-5D: {system8_data}",font=bold_font)
    label_new_window.pack()
    label_new_window.place(x=780, y=170)
    bold_font = font.Font(family="Helvetica", size=13, weight="bold")
    label_new_window = tk.Label(new_window, text=f"BAY 5 AVAILABLE: {system9_data + system10_data}",font=bold_font)
    label_new_window.pack()
    label_new_window.place(x=1020, y=60)
    bold_font = font.Font(family="Helvetica", size=13, weight="bold")
    label_new_window = tk.Label(new_window, text=f"BAY 5-4A: {system9_data}",font=bold_font)
    label_new_window.pack()
    label_new_window.place(x=1020, y=85)
    bold_font = font.Font(family="Helvetica", size=13, weight="bold")
    label_new_window = tk.Label(new_window, text=f"BAY 5-4B: {system9_data}",font=bold_font)
    label_new_window.pack()
    label_new_window.place(x=1020, y=113)
    bold_font = font.Font(family="Helvetica", size=13, weight="bold")
    label_new_window = tk.Label(new_window, text=f"BAY 5-4C: {system10_data}",font=bold_font)
    label_new_window.pack()
    label_new_window.place(x=1020, y=140)
    bold_font = font.Font(family="Helvetica", size=13, weight="bold")
    label_new_window = tk.Label(new_window, text=f"BAY 5-4D: {system10_data}",font=bold_font)
    label_new_window.pack()
    label_new_window.place(x=1020, y=170)
    bold_font = font.Font(family="Helvetica", size=13, weight="bold")
    label_new_window = tk.Label(new_window, text="TOTAL PARKING AVAILABLE:0227",font=bold_font)
    label_new_window.pack()
    label_new_window.place(x=490, y=220)
    bold_font = font.Font(family="Helvetica", size=13, weight="bold")
    label_new_window = tk.Label(new_window, text=" TOTAL PARKING SPACE : 1547 ",font=bold_font)
    label_new_window.pack()
    label_new_window.place(x=160, y=520)
    bold_font = font.Font(family="Helvetica", size=13, weight="bold")
    label_new_window = tk.Label(new_window, text=f" TOTAL SPACE AVAILABLE : {system11_total} ",font=bold_font)
    label_new_window.pack()
    label_new_window.place(x=160, y=570)
    bold_font = font.Font(family="Helvetica", size=13, weight="bold")
    label_new_window = tk.Label(new_window, text=f"BAY1 AVAILABLE : {system1_data + system2_data} ",font=bold_font)
    label_new_window.pack()
    label_new_window.place(x=500, y=510)
    bold_font = font.Font(family="Helvetica", size=13, weight="bold")
    label_new_window = tk.Label(new_window, text=f"BAY2 AVAILABLE : {system3_data + system4_data}",font=bold_font)
    label_new_window.pack()
    label_new_window.place(x=500, y=560)
    bold_font = font.Font(family="Helvetica", size=13, weight="bold")
    label_new_window = tk.Label(new_window, text=f"BAY3 AVAILABLE : {system5_data + system6_data}",font=bold_font)
    label_new_window.pack()
    label_new_window.place(x=500, y=610)
    bold_font = font.Font(family="Helvetica", size=13, weight="bold")
    label_new_window = tk.Label(new_window, text=f"BAY4 AVAILABLE : {system7_data + system8_data}",font=bold_font)
    label_new_window.pack()
    label_new_window.place(x=800, y=505)
    bold_font = font.Font(family="Helvetica", size=13, weight="bold")
    label_new_window = tk.Label(new_window, text=f"BAY5 AVAILABLE : {system9_data + system10_data}",font=bold_font)
    label_new_window.pack()
    label_new_window.place(x=800, y=540)


def refresh_window(window):
    clear_buttons(window)
    display_buttons(window)
    window.after(5000, refresh_window, window)
        

def on_button6_click():
        
        new_window = tk.Toplevel(root)
        new_window.title("New Window")

        refresh_window(new_window)


def run_in_background():
    while True:
        # Call the function every second
        update_display_data()
        time.sleep(5)
def on_button9_click():
    run_in_background()


image1 = Image.open("logo 4.png")
test = ImageTk.PhotoImage(image1)
label1 = tk.Label(image=test)
label1.image = test
label1.height = 400
label1.place(x=380, y=60)

bold_font = font.Font(family="Helvetica", size=12, weight="bold") 
button6 = tk.Button(root, text="Click for the Graphic View ", command=on_button6_click,height=4,width=25,font=bold_font)
#button6 = tk.Button(width=30,height=2)
button6.pack()
button6.place(x=650, y=560)
button6['bg']='#BECEF7'

# bold_font = font.Font(family="Helvetica", size=12, weight="bold") 
# button9 = tk.Button(root, text="Start Data on Display ", command=on_button9_click,height=4,width=25,font=bold_font)
# #button6 = tk.Button(width=30,height=2)
# button9.pack()
# button9.place(x=750, y=560)
# button9['bg']='#BECEF7'

#open_windows_button = tk.Button(root, text="Open Maintenance Windows")
#open_windows_button.pack()
#open_windows_button.place(x=700, y=750)


# Checkboxes
checkbox_var1 = tk.IntVar()
checkbox1 = tk.Checkbutton(root, text="Bay 1A",font=bold_font, variable=checkbox_var1, command=lambda: on_checkbox_checked(checkbox_var1, "ID1", "WELCOME"))
checkbox1.pack()
checkbox1.place(x=220, y=110)
checkbox_var2 = tk.BooleanVar()
checkbox2 = tk.Checkbutton(root, text="Bay 1B", font=bold_font,variable=checkbox_var2,command=lambda: on_checkbox_checked(checkbox_var2, "ID2", "WELCOME"))
checkbox2.pack()
checkbox2.place(x=220, y=170)
checkbox_var3 = tk.BooleanVar()
checkbox3 = tk.Checkbutton(root, text="Bay 2A",font=bold_font, variable=checkbox_var3,command=lambda: on_checkbox_checked(checkbox_var3, "ID3", "WELCOME"))
checkbox3.pack()
checkbox3.place(x=220, y=230)

checkbox_var11 = tk.BooleanVar()
checkbox11 = tk.Checkbutton(root, text="Bay 2B", font=bold_font,variable=checkbox_var11,command=lambda: on_checkbox_checked(checkbox_var11, "ID4", "WELCOME"))
checkbox11.pack()
checkbox11.place(x=520, y=110)
checkbox_var12 = tk.BooleanVar()
checkbox12 = tk.Checkbutton(root, text="Bay 3A",font=bold_font, variable=checkbox_var12,command=lambda: on_checkbox_checked(checkbox_var12, "ID5", "WELCOME"))
checkbox12.pack()
checkbox12.place(x=520, y=170)
checkbox_var13 = tk.BooleanVar()
checkbox13 = tk.Checkbutton(root, text="Bay 3B", font=bold_font,variable=checkbox_var13,command=lambda: on_checkbox_checked(checkbox_var13, "ID6", "WELCOME"))
checkbox13.pack()
checkbox13.place(x=520, y=220)
checkbox_var14 = tk.BooleanVar()
checkbox14 = tk.Checkbutton(root, text="Bay 4A", font=bold_font,variable=checkbox_var14,command=lambda: on_checkbox_checked(checkbox_var14, "ID7", "WELCOME"))
checkbox14.pack()
checkbox14.place(x=860, y=110)
checkbox_var15 = tk.BooleanVar()

checkbox15 = tk.Checkbutton(root, text="Bay 4B", font=bold_font,variable=checkbox_var15,command=lambda: on_checkbox_checked(checkbox_var15, "ID8", "WELCOME"))
checkbox15.pack()
checkbox15.place(x=860, y=170)

checkbox_var16 = tk.BooleanVar()

checkbox16 = tk.Checkbutton(root, text="Bay 5A", font=bold_font,variable=checkbox_var15,command=lambda: on_checkbox_checked(checkbox_var15, "ID9", "WELCOME"))
checkbox16.pack()
checkbox16.place(x=860, y=230)
checkbox_var17 = tk.BooleanVar()

checkbox17 = tk.Checkbutton(root, text="Bay 5B",font=bold_font, variable=checkbox_var17,command=lambda: on_checkbox_checked(checkbox_var17, "ID10", "WELCOME"))
checkbox17.pack()
checkbox17.place(x=1100, y=170)
checkbox_var18 = tk.BooleanVar()


bold_font = font.Font(family="Helvetica", size=14, weight="bold")
label = tk.Label(root, text="SET STATUS AS WELCOME", font=bold_font)
label.pack()
label.place(x=500, y=40)

bold_font = font.Font(family="Helvetica", size=14, weight="bold")
labe2 = tk.Label(root,  text="SET STATUS AS MAINTENANCE", font=bold_font)
labe2.pack()
labe2.place(x=500, y=300)
# set status as maintinance
checkbox_var1 = tk.IntVar()
bold_font = font.Font(family="Helvetica", size=13, weight="bold")
checkbox1 = tk.Checkbutton(root, 
text=" Bay 1A", font=bold_font,variable=checkbox_var1, command=lambda: on_checkbox_checked1(checkbox_var1, "ID1", "MAINTENANCE"))
checkbox1.pack()
checkbox1.place(x=220, y=370)
checkbox_var2 = tk.BooleanVar()
checkbox2 = tk.Checkbutton(root, text=" Bay 1B", font=bold_font,variable=checkbox_var2,command=lambda: on_checkbox_checked1(checkbox_var2, "ID2", "MAINTENANCE"))
checkbox2.pack()
checkbox2.place(x=220, y=430)
checkbox_var3 = tk.BooleanVar()
checkbox3 = tk.Checkbutton(root, text="Bay 2A", font=bold_font,variable=checkbox_var3,command=lambda: on_checkbox_checked1(checkbox_var3, "ID3", "MAINTENANCE"))
checkbox3.pack()
checkbox3.place(x=220, y=490)
checkbox_var4 = tk.BooleanVar()
checkbox4 = tk.Checkbutton(root, text="Bay 2B", font=bold_font,variable=checkbox_var4,command=lambda: on_checkbox_checked1(checkbox_var4, "ID4", "MAINTENANCE"))
checkbox4.pack()
checkbox4.place(x=520, y=370)
checkbox_var5 = tk.BooleanVar()
checkbox5 = tk.Checkbutton(root, text="Bay 3A", font=bold_font,variable=checkbox_var5,command=lambda: on_checkbox_checked1(checkbox_var5, "ID5", "MAINTENANCE"))
checkbox5.pack()
checkbox5.place(x=520, y=430)
checkbox_var6 = tk.BooleanVar()
checkbox6 = tk.Checkbutton(root, text="Bay 3B",font=bold_font, variable=checkbox_var6,command=lambda: on_checkbox_checked1(checkbox_var6, "ID6", "MAINTENANCE"))
checkbox6.pack()
checkbox6.place(x=520, y=490)
checkbox_var7 = tk.BooleanVar()
checkbox7 = tk.Checkbutton(root, text="Bay 4A",font=bold_font, variable=checkbox_var7,command=lambda: on_checkbox_checked1(checkbox_var7, "ID7", "MAINTENANCE"))
checkbox7.pack()
checkbox7.place(x=860, y=370)
checkbox_var8 = tk.BooleanVar()
checkbox8 = tk.Checkbutton(root, text="Bay 4B",font=bold_font, variable=checkbox_var8,command=lambda: on_checkbox_checked1(checkbox_var8, "ID8", "MAINTENANCE"))
checkbox8.pack()
checkbox8.place(x=860, y=430)
checkbox_var9 = tk.BooleanVar()
checkbox9 = tk.Checkbutton(root, text="Bay 5A",font=bold_font, variable=checkbox_var9,command=lambda: on_checkbox_checked1(checkbox_var9, "ID9", "MAINTENANCE"))
checkbox9.pack()
checkbox9.place(x=860, y=490)
checkbox_var10 = tk.BooleanVar()
checkbox10 = tk.Checkbutton(root, text="Bay 5B",font=bold_font, variable=checkbox_var10,command=lambda: on_checkbox_checked1(checkbox_var10, "ID10", "MAINTENANCE"))
checkbox10.pack()
checkbox10.place(x=1100, y=430)

# root.after(0, update_display_data)


# Start the background thread
background_thread = Timer(5, run_in_background)
background_thread.start()


    

root.mainloop()
