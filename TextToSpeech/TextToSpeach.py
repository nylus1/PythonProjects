import pyttsx3, tkinter
from tkinter.filedialog import askdirectory
from tkinter import messagebox

# Inicio del tts
engine = pyttsx3.init()
engine.setProperty('rate', 140)
engine.setProperty('voice', 'spanish')

# Funcion principal
def play(texto):
    texto = text.get()
    engine = pyttsx3.init()
    engine.setProperty('rate', 140)
    engine.say(texto)
    engine.runAndWait()
    if not texto:
        messagebox.showerror("Error", "Por favor introduce un texto antes de reproducir un audio.")

# Función para obtener la ruta de guardado
def ruta():
    return askdirectory(title='Selecciona donde quieres guardar tu archivo', initialdir=r'C:\Users')

# Funcion para guardar audio
def save(texto, ruta, name:str):
    engine = pyttsx3.init()
    engine.setProperty('rate', 140)
    engine.save_to_file(texto, ruta + '/' + name + '.mp3')
    engine.runAndWait()

    if not texto:
        messagebox.showerror("Error", "Por favor introduce un texto antes de guardar.")
    elif not ruta:
        messagebox.showerror("Error", "Por favor selecciona una ruta antes de guardar.")
    else:
        messagebox.showinfo("Guardado","Archivo guardado con éxito.")

# Función para cambiar el idioma
# def change_language():
#     current_voice = engine.getProperty('voice')
#     voices = engine.getProperty('voices')
#     if current_voice == 'spanish':
#         engine.setProperty('voice', voices[0].id)
#         langlabel.config(text="Idioma actual: inglés")
#     else:
#         engine.setProperty('voice',  voices[1].id)
#         langlabel.config(text="Idioma actual: español")


# Ventana principal
root = tkinter.Tk()
root.config(width=500, height=350)
root.title("TTs")

# Placeholder para introducir el texto 
textlabel=tkinter.Label(text="Introduce el texto:")
textlabel.place(x=20, y=50)
text=tkinter.Entry()
text.place(x=135, y=50)

# Nombre del archivo
namelabel=tkinter.Label(text="Nombre del archivo:")
namelabel.place(x=20, y=100)
name=tkinter.Entry()
name.place(x=135, y=100)

# Boton ruta del archivo
rutaButton=tkinter.Button(text='Ruta de Guardado', command=lambda: rutalabel.config(text=ruta()))
rutaButton.place(x=300, y=50)

# Label para mostrar la ruta de guardado
rutalabel=tkinter.Label(text="")
rutalabel.place(x=20, y=150)

# Boton de play
playButton=tkinter.Button(text='Reproducir', command=lambda: play(text.get()))
playButton.place(x=300, y=150)

# Boton para guardar audio
saveButton=tkinter.Button(text='Guardar', command=lambda: save(text.get(), rutalabel.cget('text'), name.get()))
saveButton.place(x=300, y=100)

# Boton para cambiar el idioma
# langButton=tkinter.Button(text='Cambiar idioma', command=change_language)
# langButton.place(x=20, y=200)

# # Label para mostrar el idioma actual
# langlabel=tkinter.Label(text="Idioma actual: español")
# langlabel.place(x=150, y=200)

root.mainloop()
