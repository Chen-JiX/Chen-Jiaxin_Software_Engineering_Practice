# This is a automatic test checking system by Chen Jiaxin
The code includes two main parts:
- **Apply Fastapi to upload right answer and student tests answer.**

  Before run the codes, we should install some required packages.
  ```python
  from fastapi import FastAPI, UploadFile
  import uvicorn
  ```
  The upload screen is shown in the figure
  ![](https://github.com/Chen-JiX/Chen-Jiaxin_Software_Engineering_Practice/blob/main/operating_results/upload_func.png)
  teachers can upload the right answer here and students can upload their test answers here.
  
- **Apply tkinter to creat a GUI to help users to use the functions.**
  Before run the codes, we should install some required packages.
  ```python
  import tkinter as tk
  import os
  from PIL import Image, ImageTk
  ```
  
  **The GUI page looks as below**
  ![](https://github.com/Chen-JiX/Chen-Jiaxin_Software_Engineering_Practice/blob/main/operating_results/GUI.png)
  
  - **one function is to check the list of students who submitted their answers.**
    ![](https://github.com/Chen-JiX/Chen-Jiaxin_Software_Engineering_Practice/blob/main/operating_results/func1.png)

  - **the second function is to check the details of students' test answers.**
    ![](https://github.com/Chen-JiX/Chen-Jiaxin_Software_Engineering_Practice/blob/main/operating_results/func2.png)

  - **the third function is to check the scores of students.**
    
    ![](https://github.com/Chen-JiX/Chen-Jiaxin_Software_Engineering_Practice/blob/main/operating_results/func3.png)

  - **the fourth function is to analyse the students' test answers, and collect the wrong answers**
    ![](https://github.com/Chen-JiX/Chen-Jiaxin_Software_Engineering_Practice/blob/main/operating_results/func4.png)

  **The main functions are shown above**

    

