# Tools
Scripts that I use to automate my workflow in Windows. 

## Autohotkey 
### Select text, then search in Chrome
### Select text, then search in Everything


## Document processing
### Split pdf file by its bookmakrs (Python)
I use this python script to break 1 book pdf file into multiple chapter pdf files. [split PDF by bookmarks](https://github.com/Xianzhi-Li/Tools/blob/main/split%20pdf%20by%20bookmarks.py)
1. Put both "split pdf by bookmarks.py" and target pdf files on desktop.
2. Open Command Prompt by search cmd.
3. In Command Prompt, navigate to desktop folder by typing `cd Desktop`.

<p align="center">
  <img src="https://github.com/Xianzhi-Li/Tools/blob/main/pic/cd_desktop.jpg?raw=true">
</p>

4. Type `python "split pdf by bookmarks.py" "targetPDF.pdf"`

A folder called "output" was created on your desktop. A folder called "targetPDF" was created inside the "output" folder. The splited pdf files "targetPDF_bookmark name" should be inside. 
### Edit resume.docx by inputing variables (Python)
In an original resume template.docx, I put in a few text replacement holders, such as {job position}, {company name}, {company location}, {company mission}. This script asks input for each text replacement holder, then fill-in the blanks. [resume template editor.py](https://github.com/Xianzhi-Li/Tools/blob/main/resume%20template%20editor.py) 

### auto generate bookmarks of chapters (Python) 
A script that automatically generate bookmarks based on chapters. 
