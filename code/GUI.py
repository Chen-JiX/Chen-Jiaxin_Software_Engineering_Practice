# coding=utf-8
import tkinter as tk
import os
from PIL import Image, ImageTk
from test_score import test_score_with_wrong
import numpy as np


def draw_bar_chart(canvas, data, width=500, height=300, padding=20):
    # calculate location
    bar_width = (width - 2 * padding) / len(data)
    max_value = max(data)
    scale = (height - 2 * padding) / max_value

    # plot
    for i, value in enumerate(data):
        x0 = padding + i * bar_width
        y0 = height - padding
        x1 = x0 + bar_width
        y1 = height - padding - value * scale
        canvas.create_rectangle(x0, y0, x1, y1, fill="lightblue")
        canvas.create_text((x0 + x1) / 2, y0+10, text=str(i+1))
        if value != 0:
            canvas.create_text((x0 + x1) / 2, y1-10, text=str(value))


def get_score():
    base_dir = './student_answers'
    scores = {}
    wrongs = [0 for i in range(10)]

    if len(os.listdir(base_dir)) != 0:
        files = [os.path.join(base_dir, file) for file in os.listdir(base_dir)]
    else:
        return 0
    for file in files:
        student = file[18:-4]
        score, wrong = test_score_with_wrong(file)
        scores[student] = score
        wrongs = [i + j for i, j in zip(wrongs, wrong)]
    return scores, wrongs


def display_tests(item):
    # Create a new Tkinter window
    details_window = tk.Toplevel()
    details_window.title(f"{item}'s Test")

    # open the image
    ima_dir = f'student_answers/{item}.png'
    image = Image.open(ima_dir)

    # get the score
    score = scores.get(item)

    photo = ImageTk.PhotoImage(image)

    # Display the selected item in the new window
    label1 = tk.Label(details_window, text=f"Name: {item}", justify=tk.LEFT, font=("Helvetica", 14))
    label2 = tk.Label(details_window, text=f"Score: {score}", justify=tk.LEFT, font=("Helvetica", 14))
    label3 = tk.Label(details_window, image=photo)
    label3.image = photo  # Keep a reference to the photo
    label1.pack(padx=10, pady=5, anchor=tk.W)
    label2.pack(padx=10, anchor=tk.W)
    label3.pack(padx=10, pady=10)


def check_student():
    def close_list():
        frame.destroy()
    # store students
    stu = []

    # Create a frame
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    # Create a listbox to display the extracted requirements
    student_list1= tk.Listbox(frame, width=20, height=15, bg="lightgray", font=("Helvetica", 14), selectbackground="blue", selectforeground="white", bd=3, relief=tk.GROOVE)

    close_button = tk.Button(frame, text="×", bg="red", width=1, font=("Helvetica", 12, "bold"), command=close_list)
    close_button.place(x=208, y=2)

    def on_select(event):
        # Get the selected item
        index = student_list1.curselection()[0]
        selected_item = stu[index]
        # Display details of the selected item
        display_tests(selected_item)

    for key in scores.keys():
        student_list1.insert(tk.END, key.strip())
        stu.append(key)

    # Bind the selection event to the student list
    student_list1.bind("<<ListboxSelect>>", on_select)
    student_list1.pack()


def check_score():
    stu = []

    # creat a new window
    window = tk.Tk()
    window.title("Student Scores！")

    # creat a frame to store listbox
    frame = tk.Frame(window)
    frame.pack(padx=20, pady=20)

    label1 = tk.Label(frame, text='Name', font=("Helvetica", 16))
    label2 = tk.Label(frame, text='Score', font=("Helvetica", 16))
    label1.grid(row=0, column=0)
    label2.grid(row=0, column=1)

    def on_select(event):
        # Get the selected item
        index = student_list.curselection()[0]
        selected_item = stu[index]
        # Display details of the selected item
        display_tests(selected_item)

    # Create a listbox to display the extracted requirements
    student_list = tk.Listbox(frame, width=10, height=15, bg="lightgray", font=("Helvetica", 16), bd=3, relief=tk.GROOVE)
    score_list = tk.Listbox(frame, width=10, height=15, bg="lightgray", font=("Helvetica", 16), bd=3, relief=tk.GROOVE)

    for key, value in scores.items():
        student_list.insert(tk.END, key.strip())
        score_list.insert(tk.END, value)
        stu.append(key)

        student_list.bind("<<ListboxSelect>>", on_select)
        student_list.grid(row=1, column=0)
        score_list.grid(row=1, column=1)


def test_analysis():
    sum = 0
    num = 0
    chart_window = tk.Tk()
    chart_window.title("Test Analysis！")

    frame = tk.Frame(chart_window)
    frame.pack()

    label = tk.Label(frame, text="Error Statistics", font=("Helvetica", 14))
    label.pack(padx=5, pady=10)

    canvas = tk.Canvas(frame, width=500, height=300)
    canvas.pack()
    draw_bar_chart(canvas, wrongs)

    for value in scores.values():
        sum += value
        num += 1
    # average
    average = round(sum/num, 1)

    label = tk.Label(frame, text=f"Average Score: {average}", font=("Helvetica", 14))
    label.pack(padx=10, pady=20, side=tk.LEFT)


def main_window():
    # Create the main window
    global root
    global scores
    global wrongs
    scores, wrongs = get_score()

    root = tk.Tk()
    root.title("Automatic test checking system")
    root.geometry('500x600')

    # Create a label widget
    label = tk.Label(root, text="Welcome to Automatic test checking system!!!", font=("Helvetica", 14, "bold"), fg="blue")

    # Pack the label into the main window
    label.pack(pady=30)

    # Button to load and display student list
    check_button = tk.Button(root, text="Students List", command=check_student, width=20, font=("Helvetica", 14), bd=5)
    check_button.pack(pady=15)

    score_button = tk.Button(root, text="Students Score", command=check_score, width=20, font=("Helvetica", 14), bd=5)
    score_button.pack(pady=15)

    score_button = tk.Button(root, text="Test Analysis", command=test_analysis, width=20, font=("Helvetica", 14), bd=5)
    score_button.pack(pady=15)

    # Start the Tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    main_window()

