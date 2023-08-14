# Flipkart Web-scraper

## Used for scraping product data from Flipkart

### Uses the scraping script built by [Ankit Tiwari](https://github.com/ankit25821/flipkart-scrapper)

## Dependencies

- Python 3.6 or above ( ideally python 3.10+ )

## Installation Steps

### 1. Clone/Download this repository

You can either clone it using git or download the zip file and then unpack it. (Click on the drop down arrow next to Code > Download ZIP)

### 2. Create a Virtual Environment

```zsh
python3 -m venv ./venv
```

- Alternatively, any other suitable way to create a virtual environment ( such as `virtualenv` or `conda` ) can be used as per convenience.

### 3. Activate the Virtual Environment

For Mac/Linux:

- `zsh` or `bash`

 ```zsh
source ./venv/bin/activate
 ```

For Windows:

- `powershell`

```zsh
venv/Scripts/Activate.ps1
```

### 4. Install all Required Packages

```zsh
pip install -r requirements.txt
```

You're Good to go!

## 3. Usage

1. Open a terminal window in the root directory of the project
2. Execute 'main.py'

    ```zsh
    python main.py
    ```

3. Enter a search query
4. The list of products will be displayed as a JSON string after some time. A CSV file will  also be generated in ./output/
