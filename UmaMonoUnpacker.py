import os
import json
import tkinter
from tkinter import filedialog
import UnityPy

root = tkinter.Tk()
root.withdraw()
srcPath = filedialog.askopenfilename()
env = UnityPy.load(srcPath)
 
for obj in env.objects:
    if obj.type.name == "MonoBehaviour":
        if obj.serialized_type.nodes:
            tree = obj.read_typetree()
            
            with open("tmp.json", "w+",encoding='utf-8') as jsonFile:
                jsonFile.write(json.dumps(tree, indent = 4))
                jsonFile.close();

            os.startfile("tmp.json")
            input("修改后按任意键继续"); 

            with open("tmp.json", "r",encoding='utf-8') as jsonFile:
                tree = json.load(jsonFile)
                jsonFile.close();
            obj.save_typetree(tree)

with open(srcPath, "wb") as f:
    f.write(env.file.save())