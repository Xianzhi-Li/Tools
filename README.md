# Tools
Scripts that I use to automate my workflow in Windows. 

## Autohotkey 

## Python 
### Split pdf file by its bookmakrs 
I use this python script to break 1 book pdf file into multiple chapter pdf files. 
1. Put both "split pdf by bookmarks.py" and target pdf files on desktop.
2. Open Command Prompt by search cmd.
3. In Command Prompt, navigate to desktop folder by typing `cd Desktop`.
https://github.com/Xianzhi-Li/Tools/blob/main/cd_desktop.jpg
![cd_desktop](https://github.com/Xianzhi-Li/Tools/blob/main/cd_desktop.jpg?raw=true)

5. Type `python "split pdf by bookmarks.py" "targetPDF.pdf"`
A folder called "output" was created on your desktop. A folder called "targetPDF" was created inside the "output" folder. The splited pdf files "targetPDF_bookmark name" should be inside. 
