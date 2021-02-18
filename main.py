from tkinter import *

window = Tk()

window.title("Mile to Km Converter")
window.minsize()
window.config(padx=35, pady=25)


mile_input = Entry(text="0")
mile_input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 16))
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to", font=("Arial", 16))
equal_label.grid(column=0, row=1)

km_result_label = Label(text="0", font=("Arial", 16))
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km", font=("Arial", 16))
km_label.grid(column=2, row=1)


def convert():
    total = round(float(mile_input.get()) * 1.6)
    km_result_label["text"] = total


button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)




window.mainloop()