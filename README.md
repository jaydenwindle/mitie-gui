# MITIE GUI - MITIE training made easy

MITIE GUI is a browser-based tool for generating the python code to train a custom [MITIE](https://github.com/mit-nlp/MITIE) model (Currently only named entity recognition models are supported, but I hope to support binary relation detection models soon too). Simply input the raw data which you would like to train on, then use the tool to select which tokens correspond to which entities. The tool will generate the python code required to train your model, just copy, paste and run. 

## Usage

```bash
git clone https://github.com/jaydenwindle/mitie-gui.git && cd mitie-gui
pip install -r requirements.txt
python app.py
```

## Notes
The tool is built with Flask as a back end. This is because when I built it I had a route which would automatically generate the required JSON input (from an api) and pass it to the training tool. Details on how to do that will be added here soon.

This tool uses python 2.7
