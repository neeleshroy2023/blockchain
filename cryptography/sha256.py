import hashlib
import tkinter as tk
from tkinter import filedialog

BUFFSIZE = 65536

sha1 = hashlib.sha256()

filepath = filedialog.askopenfilename(title="Select a file.")

root = tk.Tk()
root.title("File Dialog")

with open(filepath, 'rb') as f:
    while(True):
        data = f.read(BUFFSIZE)
        sha1.update(data)
        if not data:
            break
print(sha1.hexdigest())