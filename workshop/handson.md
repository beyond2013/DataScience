# Toolboxes for Data Scientists
- Python
- R
- Matlab / Octave

# Fundamental Python Libraries for Data Scientists

1. Numeric and Scientific Computation: NumPy and SciPy
2. Machine Learning in Python: SCIKIT-Learn
3. Python Data Analysis: PANDAS

# Data Science Ecosystem Installation
- All in one bundle [Anaconda](https://www.anaconda.com/products/individual) 

# Getting Started
1. After installing Anaconda launch jupyter notebook from windows start menu
2. On linux run jupyter notebook from terminal
3. It will launch browser displaying jupyter homepage
4. To start a new notebook press New -> Notebooks -> Python 3
5. A blank notebook Untitled will be created 
6. Click "Untitled" to rename and save the notebook
7. import tool boxes by adding the following lines in first cell

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```
8. To execute a single cell press the `Run` button or click on Cell -> Run or press Ctrl + Enter

# The DataFrame data structure
- key data structure in Pandas is DataFrame object.
- a tabular structure with rows and columns(can be seen as flexible spreadsheet).
- rows have specific index to access them, which can be any name or value
- columns are called "Series", a special type of data
- Following code can be used to create a dataframe
```python
data = {'year': [2010, 2011, 2012, 2010, 2011, 2012, 2010, 2011, 2012],
        'team': ['FCBarcelona', 'FCBarcelona', 'FCBarcelona', 'RMadrid', 
				         'RMadrid', 'RMadrid', 'ValenciaCF',
                 'ValenciaCF', 'ValenciaCF'],
        'wins':   [30, 28, 32, 29, 32, 26, 21, 17, 19],
        'draws':  [6, 7, 4, 5, 4, 7, 8, 10, 8],
        'losses': [2, 3, 2, 4, 2, 5, 9, 11, 11]
        }
football = pd.DataFrame(
    data, columns=['year', 'team', 'wins', 'draws', 'losses'])
```

# Getting data
- plenty of online resources offering all sorts of datasets in various formats
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets.php)
- [Kaggle](https://www.kaggle.com/)
	+ [Titanic Machine learning from disaster](https://www.kaggle.com/c/titanic/data)
	

# Reading data
- Use pandas `read_csv` method to read csv(comma separated values)
  + titanic = pd.read_csv('dataset/titanic/train.csv', na_values = '')
- read_excel() to read excel files
- read_hdf() for HDF5
- read_table() read tabulated files
- read_clipboard() to read contents from the clipboard


# See how to the data looks
- titanic.head() to see first 5 rows
- titanic.tail() to see the last 5 rows
- titanic.describe() for quick statistical information on numeric columns

# Selecting Data
- to select a subset of data from a DataFrame, several ways available
- titanic['Name'] to select the Name Series.
- titanic[10:14] to select slice of rows from 10 to 13, 14 is exclusive
- titanic.ix[10:14, ['Name','Sex','Age']] using labels as reference instead of positions




 

