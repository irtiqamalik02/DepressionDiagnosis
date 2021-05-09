# Depression Diagnosis
Using ML models and a BERT based model to diagnose depression.

## Overview

Depression is ranked as the largest contributor to global disability and is also a major reason for
suicide. It often co-occurs with anxiety or other psychological and physical disorders and has an
impact on feelings and behaviour of the affected individuals. Detecting earlier depression can be a huge step to address the mental illness and offer support to the people suffering from this terrible mental illness.

This application aims to reduce depression by monitoring chrome activity and instil mental peace and serenity.


---
## Dependencies

Make sure you have these installed on your system before running the application

**Prediction using Machine Learning
(dep1.py, dep2.py)**
- `$ sudo apt-get install python3.6`
- `$ sudo apt-get install pip3`
- `$ sudo pip3 install -U nltk`
- `$ sudo pip3 install pandas`
- `$ sudo pip3 install numpy`

**For extracting Chrome History
(browserhistory.py, gethistory.py, setup.py)
Libraries used**
- `import csv`
- `import os`
- `import sqlite3`
- `import sys`
- `from datetime import datetime`
- `import copy`
- `import shutil`

**Connection of Python Backend to Front end:**
- Install Flask
		- `$ sudo pip3 install Flask`
- File structure: app.py
  - Templates(dir) - `index.html`
                   - `response.html`

---

## Running the Application

Clone this repository or download it as a zip file.

**Start the backend server**
- Open the terminal
- Type the command
  - `sudo python3 app.py`
- Wait for some time for the server to be completely up and running

**Loading the Chrome Extension**
- Open `Google Chrome` browser
- Click on the 3 dots on top right corner of the browser window
- Choose `More tools > Extensions`
- In the `extensions` browser tab, switch-on the `Developer mode` on the top right side
- Choose `Load unpacked`
- Locate and choose the `extension` folder from extracted file

The extension icon appears. You can navigate through the extension and view its features! 



---


## Developer

- Irtiqa Malik

---



