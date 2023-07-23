from tkinter import  *
from tkinter import messagebox


root = Tk()
root.geometry("900x600")
root.title("Classes")

class CreateElements:
    def _init_(self):
        print("This Is A CreateElements Class")
        
    def createNewElement(self):
        label = Label(root, text = "A New Label Is Been Created Using Class", fg = "red")
        label.pack()
        btn = Button(root, text = "Button", command = self.message)
        btn.pack(padx = 20, pady = 10)
        
    def message(self):
        messagebox.showinfo("showinfo", "You Clicked The Button That Has Been Created By Using Class")
        
obj_of_CreateElements = CreateElements()

btn = Button(root, text = "Click To Create A Label And A Button Element", command = obj_of_CreateElements.createNewElement)
btn.pack(padx = 20, pady = 10)
root.mainloop()             