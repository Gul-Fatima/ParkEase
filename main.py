import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import cv2
import pickle
import cvzone
import numpy as np
from tkinter import messagebox
import pyodbc
# user registration(sign up)
def database(user,code,confirm_password,m):
    # if the entry boxes are empty
    if user=="" or code=="" or confirm_password=="" or user=="Username" or code=="Password" or confirm_password=="Confirm Password":
        messagebox.showinfo("Enter data")

    elif code!=confirm_password:
        messagebox.showerror("Enter the same password")

    else:
        con=pyodbc.connect((r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                            r'DBQ=E:\plproj.accdb;'))
        cursor1=con.cursor()
        # Enter the data into database
        cursor1.execute(f"INSERT INTO signin(Username,Password) values ('{user}','{code}')")


        con.commit() # To make the changes permanent in the database
        messagebox.showinfo("Signed in")#Display signed-in message box.
        m.destroy()#To close the current(sign in) window
        getstarted() # now the function for opening the video of car parking
        con.close()#to close the database connection

def signup(n):
    n.destroy()#in order to destroy(close) sign in window
    m = Tk()
    m.title("Sign up")
    m.geometry("500x500")
    m.config(bg="gold2")
    m.resizable("False", "False")
    l = Label(m, text="S i g n  u p  t o  y o u r  a c c o u n t", bg="gold2", fg="black", font=("bold", 16))
    l.place(x=110, y=60)
# Entry box (user name) formattings:
    def on_enter(e):
        user.delete(0, "end")

    def on_leave(e):
        name = user.get()
        if name =="":
            user.insert(0, "Username")

    # Entry box for the user name
    user = Entry(m, width=22, fg="black", border=0, bg="gold2", font=("Microsoft YaHei UI Light", 14))
    user.place(x=130, y=130)
    user.insert(0, "Username")
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)
    Frame(m, width=240, height=2, bg="black").place(x=130, y=160)

# Entry box (Password) formattings:
    def on_enter(e):
        code.delete(0, "end")

    def on_leave(e):
        name = code.get()
        if name =="":
            code.insert(0, "Password")

    # Entry box for user password
    code = Entry(m, width=22, fg="black", border=0, bg="gold2", font=("Microsoft YaHei UI Light", 14))
    code.place(x=130, y=200)
    code.insert(0, "Password")
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)
    Frame(m, width=240, height=2, bg="black").place(x=130, y=230)
# Entry box (Confirm Password) formattings:
    def on_enter(e):
        confirm_password.delete(0, "end")

    def on_leave(e):
        name = confirm_password.get()
        if name =="":
            code.insert(0, "Confirm Password")

    # Entry box for confirming the password
    confirm_password = Entry(m, width=22, fg="black", border=0, bg="gold2", font=("Microsoft YaHei UI Light", 14))
    confirm_password.place(x=130, y=280)
    confirm_password.insert(0, "Confirm Password")
    confirm_password.bind('<FocusIn>', on_enter)
    confirm_password.bind('<FocusOut>', on_leave)
    Frame(m, width=240, height=2, bg="black").place(x=130, y=310)

    # Function for entering the data(ussername, password,confirm password) in database file name "plproj"
    b = Button(m, text="sign up", width=20, bg="black", fg="gold2",command=lambda: database(user.get(),code.get(),confirm_password.get(),m))
    b.place(x=160, y=370)

    m.mainloop()

def getstarted():
    # saving the video to variable
    cap = cv2.VideoCapture("car video.mp4")
    # Get the position's list
    with open('CarParkPos', 'rb') as f:    #rb:to read file in binary mode
        pos = pickle.load(f)
    # Defining width and height
    width, height = 107, 48

    def checkparkingspace(imgPro):

        spaceCounter = 0
        for position in pos:
            x, y = position

            # Cropping the rectangle
            imgCrop = imgPro[y:y + height, x:x + width]
            # cv2.imshow(str(x*y),imgCrop)
            # Count the pixel for each crop picture
            count = cv2.countNonZero(imgCrop)

            if count < 900:
                color = (0, 255, 0)
                thickness = 5
                spaceCounter += 1
            else:
                color = (0, 0, 255)#color code for green
                thickness = 2
            # Creating the rectangle
            cv2.rectangle(img, position, (position[0] + width, position[1] + height), color, thickness)
            # Showing the pixel on the video
            cvzone.putTextRect(img, str(count), (x, y + height - 3), scale=1, thickness=2, offset=0, colorR=color)


    while True:

        # Checking the current and total number of frames
        if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
            # For again starting the video
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        # success- for showing frames of video
        success, img = cap.read()
        # Convert the video to grey color
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Blur the video
        imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
        # Convert the video to binary video
        imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                             cv2.THRESH_BINARY_INV, 25, 16)

        imgMedium = cv2.medianBlur(imgThreshold, 5)
        kernel = np.ones((3, 3), np.uint8)
        # To make the pixel little thick
        imgDilate = cv2.dilate(imgMedium, kernel, iterations=1)

        checkparkingspace(imgDilate)

        # Opening the video
        cv2.imshow("Image", img)
        key = cv2.waitKey(10)
        if key == ord('q'):
            break
        # cv2.imshow("ImageBlur",imgBlur)
        # cv2.imshow("ImageThres",imgThreshold)
        # cv2.imshow("ImageMedium", imgMedium)
        # cv2.waitKey(10)
    cap.release()

# user authentication(sign in)
def check_data_in_database(user,code,m):
  # when either of the entry boxes are empty
    if user=="" or user=="Username" or code=="" or code=="Password":
        messagebox.showinfo("Please enter the data")

    else:
        connection_string = 'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=E:\\plproj.accdb;' # Path for the database connection
        table_name = 'signin'
        user_column = 'Username'
        code_column = 'Password'

        try:

            # Connect to the database
            with pyodbc.connect(connection_string) as connection:
                cursor = connection.cursor()

                # Execute a query to check if the data exists
                username_query = f"SELECT * FROM {table_name} WHERE {user_column} = ?"
                cursor.execute(username_query, user)
                username_row = cursor.fetchone()

                if username_row:
                    # Username exists, now check the password
                    password_query = f"SELECT * FROM {table_name} WHERE {user_column} = ? AND {code_column} = ?"
                    cursor.execute(password_query, user, code)
                    password_row = cursor.fetchone()

                    if password_row:
                        # For both the password and username are correct then close the signup window
                        m.destroy()
                        getstarted()

                    else:
                        # The given password is wrong
                        messagebox.showinfo("Wrong password")
                        m.destroy()
                else:
                    # The given username is not exist
                    messagebox.showinfo("Wrong username")
                    m.destroy()


        except pyodbc.Error as e:

            print(f"Database Error: {e}")

def signin():
    m = Tk()
    m.title("Sign in")
    m.geometry("450x500")
    m.config(bg="grey12")
    m.resizable("False", "False")
    # "login to your account" label
    l_main = Label(m, text="L o g   i n t o   y o u r   a c c o u n t", bg="grey12", fg="gold2",
                   font=("callibri", 14, "bold"))
    l_main.place(x=68, y=80)
    # "Not signed yet" label
    l_main = Label(m, text="N o t    s i g n e d    y e t ?", bg="grey12", fg="gold4", font=("callibri", 10, "bold"))
    l_main.place(x=72, y=341)

    def on_enter(e):
        user.delete(0, "end")
    # entrybox(username) formattings
    def on_leave(e):
        name = user.get()
        if name =="":
            user.insert(0, "Username")

    # Entry box for the user name
    user = Entry(m, width=27, fg="gold2", border=0, bg="grey12", font=("Microsoft YaHei UI Light", 14))
    user.place(x=74, y=170)
    user.insert(0, "Username")
    # bind method is used to associate an event with a function or method.
    # Focusin- when the user click on it
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)
    Frame(m, width=308, height=2, bg="gold2").place(x=70, y=200)

    # entrybox(password) formattings
    def on_enter(e):
        code.delete(0, "end")

    def on_leave(e):
        name = code.get()
        if name == "":
            code.insert(0, "Password")

    # Entry box for the user password
    code = Entry(m, width=27, fg="gold2", border=0, bg="grey12", font=("Microsoft YaHei UI Light", 14))
    code.place(x=74, y=220)
    code.insert(0, "Password")
    # Focusout : When the user click outside the entry box
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)
    Frame(m, width=308, height=2, bg="gold2").place(x=70, y=250)

    # button for sign up(if user not registered)
    b2 = Button(m, text="S i g n   u p !", width=12, bg="grey12", fg="skyblue4", bd=0,command=lambda: signup(m), font=("bold", 15))
    b2.place(x=240, y=335)

    # create a button(sign in), that check if the user registered or not
    b1 = Button(m, text="S i g n   i n", width=33, bg="gold2", fg="black",
                command=lambda: check_data_in_database(user.get(), code.get(), m), font=("bold", 13))
    b1.place(x=72, y=300)
    Frame(m, width=170, height=2, bg="gold4").place(x=72, y=340)
    m.mainloop()


def contactus():
    # Another window that provide information about parkease
    x = Tk()
    x.title("Contact us")
    x.geometry("350x160")
    x.resizable(False, False)
    x.config(bg="gold2")
    l = Label(x, text="About Us", bg="gold2", fg="#556B2F")
    l.place(x=10, y=15)
    l1 = Label(x, text="ParkEase.@gmail.com", bg="gold2", fg="dark green", font=("bold", 15))
    l1.place(x=10, y=40)
    l2 = Label(x, text="03302734537", bg="gold2", fg="dark green", font=("bold", 15))
    l2.place(x=10, y=80)
    l3 = Label(x, text="https://www.linkedin.com/ParkEase", bg="gold2", fg="dark green", font=("bold", 15))
    l3.place(x=10, y=120)

    x.mainloop()


# for creating main window
root = Tk()
root.title("Car Parking System")
original_image = Image.open("mainwin.png")#image.open is the method of PIL

# Lanczos is known for providing high-quality results when resizing images
resized_image = original_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
background_image = ImageTk.PhotoImage(resized_image)

# Create a Label widget to display the image
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)# relwidth is the relative width

B1=Button(root,text="Get Started",bg="gold2",fg="black",font=("Bold",20),width=14,command=signin)
B1.place(x=155,y=462)

# Another button in the main window
b2=Button(root,text="Contact us",bd=0,bg="gray1",fg="gold2",font=("Bold",15),width=15,command=contactus)
b2.place(x=1100,y=30)

root.mainloop()
