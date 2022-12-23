Reference from https://www.analyticsvidhya.com/blog/2019/08/comprehensive-guide-language-model-nlp-python-code/

Created nwp.py with codings form online site
Created __main__.py, and invoking meth() present in nwp.py 
==============================
> pip3 install nltk

===============================
Downloaded two packages via cmd line
> python3 -m nltk.downloader reuters
> python3 -m nltk.downloader plunt

This will create folder data in /Users/enqos/nltk_data
This is the sample dataset to be used in the program

The default folders for each OS are:
    - Windows: C:\nltk_data\tokenizers
    - OSX: /usr/local/share/nltk_data/tokenizers
    - Unix: /usr/share/nltk_data/tokenizers


Downloading packages manually from website...
> http://www.nltk.org/nltk_data/


===============================
launch.json

{
    "name": "Working with ngram",
    "type": "python",
    "request": "launch",
    "program": "${workspaceFolder}/workingWith-ngram",
    "console": "integratedTerminal"
}