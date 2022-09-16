from tkinter import *
pencere = Tk()

pencere.title("Find and Replace")

Label(pencere, text="Find:").grid(row=0, column=0, sticky="e")

Entry(pencere, width=60).grid(row=0, column=1,padx=2, pady=2, sticky="w", columnspan=9)

Label(pencere, text="Replace:").grid(row=1, column=0, sticky="e")

Entry(pencere).grid(row=1, column=1, padx=2, pady=2, sticky="w",columnspan=9)

Button(pencere, text="Find").grid(row=0, column=10, sticky="e" + "w", padx=2, pady=2)

Button(pencere, text="Find All").grid(row=1, column=10, sticky="e" + "w", padx=2)

Button(pencere, text="Replace").grid(row=2, column=10, sticky="e" +"w", padx=2)

Button(pencere, text="Replace All").grid(row=3, column=10, sticky="e" + "w", padx=2)

Checkbutton(pencere, text="Match whole word only").grid(row=2, column=1, columnspan=4, sticky="w")

Checkbutton(pencere, text="Match Case").grid(row=3, column=1, columnspan=4, sticky="w")

Checkbutton(pencere, text="Wrap around").grid(row=4, column=1, columnspan=4, sticky="w")

Label(pencere, text="Direction:").grid(row=2, column=6, sticky="w")

Radiobutton(pencere, text="Up", value=1).grid(row=3, column=6, columnspan=6, sticky="w")

Radiobutton(pencere, text="Down", value=2).grid(row=3, column=7, columnspan=2, sticky="e")

pencere.mainloop()
