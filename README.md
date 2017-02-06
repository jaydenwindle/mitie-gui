# MITIE GUI - MITIE training made easy

MITIE GUI is a browser-based tool for generating the python code to train a custom MITIE model. Simply input the raw data which you would like to train on, then use the tool to select which tokens correspond to which entities. The tool will generate the python code required to train your model, just copy, paste and run. 

## Usage

```bash
git clone https://github.com/jaydenwindle/mitie-gui.git && cd mitie-gui
pip install -r requirements.txt
python app.py
```

## Notes
The tool is built with Flask as a back end and vue.js as a front end framework. This is because when I built it I had a route which would automatically generate the required JSON input for the tool. I'm working on making the tool totally generic, so it will likely not use Flask in the future, and will be 100% Vue.js based.

This tool uses python 2.7
