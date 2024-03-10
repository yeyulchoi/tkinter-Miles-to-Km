from tkinter import *

def converter():
    miles_input = float(entry.get())
    result_km = round(miles_input * 1.609,2)
    result_label.config(text=result_km)



window = Tk()
window.minsize(width=250, height=100)
window.title("Mile to Km Converter")
window.config(padx=10, pady=20)
entry = Entry(window)
entry.grid(row=0,column=1)

miles_label = Label(window, text="Miles")
miles_label.grid(row=0,column =2)

equal_abel = Label(window, text="is equal to")
equal_abel.grid(row=1,column=0)

result_label= Label(window, text="0")
result_label.grid(row=1, column=1)

km_label=Label(window, text="Km")
km_label.grid(row=1, column=2)

calc_button = Button(window, text="Calculate", command=converter)
calc_button.grid(row=2,column=1)





window.mainloop()








