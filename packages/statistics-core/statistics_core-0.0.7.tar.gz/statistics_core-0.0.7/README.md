# statistics-core
[![PyPI version](https://badge.fury.io/py/statistics-core.svg)](https://badge.fury.io/py/statistics-core)

Installing `statistics-core` 📊
-------------------------------

### Using `pip` 🐍

To install `statistics-core` using `pip`, follow these steps:

1.  Open a command prompt or terminal window 💻.
    
2.  Type the following command and press Enter to install `statistics-core`:
    

``` bash
pip install statistics-core
```

3.  After the installation is complete, you can use `statistics-core` in your Python program by simply importing it using the following command:

``` python
import statistics_core
```

After importing the library, you can use the functions and tools provided by `statistics-core` in your Python programs.

### Using `requirements.txt` 📋

`statistics-core` can also be installed using a `requirements.txt` file. A `requirements.txt` file contains a list of all the libraries needed to run a Python program. This file can be created manually or generated using a requirements file generation tool (such as `pipreqs` or `pip-compile`).

To install `statistics-core` using `requirements.txt`, follow these steps:

1.  Create a new `requirements.txt` file (if it does not already exist) in your project directory.
    
2.  Add the line `statistics-core` to your `requirements.txt` file.
    
``` bash
statistics-core
```

3.  Open a command prompt or terminal window in your project directory 💻.
    
4.  Type the following command and press Enter to install all the libraries specified in your `requirements.txt` file, including `statistics-core`:
    

``` bash
pip install -r requirements.txt
```

5.  After the installation is complete, you can use `statistics-core` in your Python program by simply importing it using the following command:

``` python
import statistics_core
```
After importing the library, you can use the functions and tools provided by `statistics-core` in your Python programs. 🚀

👋 Welcome to this code repository!
-------------------------------
Here you'll find a set of classes that allow you to fetch data from a database and display it in a table on a wiki page.

🗃️ The `Database` class connects to a database and runs a query to retrieve data. The results are stored in the `result` attribute, which can be accessed by other classes.

📄 The `File` class reads the contents of a file and stores it in the `contents` attribute. It can also construct a file path based on the location of the script.

📝 The `Page` class represents a wiki page and allows you to set its contents and save it.

📊 The `ArticleTable` class defines a table with columns, a sort column, and optional header and footer text. It can build the table based on the contents of the `result` attribute of the `Database` class.

📚 The `ArticleTables` class allows you to define multiple `ArticleTable` instances and add them to a list.

🔄 The `UpdatePage` class takes a `Database` instance, a file path, a wiki page name, and an `ArticleTables` instance. It reads the contents of the file, replaces a placeholder string with the table content, and saves the updated content to the wiki page.

👨‍💻 Have fun exploring and using these classes in your own projects!

## شرح الاستخدام 
## اسئله شائعه 
