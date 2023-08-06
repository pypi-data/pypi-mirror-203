
![Dymatrix Logo](/doc/png/pia_dymatrix.PNG)
# Dymatrix Analytik Customer Prediction Library </h1>
A Python Library for monitoring Dymatrix customer prediction services.

---
## Introduction 

The Dymatrix Analytik customer prediction package is an internal Python Library for machine learning monitoring and building a report table of models pipeline (including data load, features engineering, model training and scoring). It was designed to apply to Databricks environment and (currently) will not work on local machines. This repository contains various standardized functions which you can use to build a monitoring notebook for machine learning jobs or to create report tables for models results visualization. Beyond computing descriptive statistics for delta data load, machine learning features and scores, the library is also built to monitor your data schema. Hence, you can ensure that the new imported data contains the correct data structure.

---
## Getting Started
### Installation (Databricks :cloud:)

To use this library on your Databricks environment, please follow these steps:

1. Go to your Databricks environment
2. Go to **_Repos_** section
3. Click on `Add Repo` and add the repository using the following protocol:
 `https://dev.azure.com/dymatrix/_git/Dymatrix%20Analytik`
4. Select Git provider. *Azure DevOps Services* should be selected in this case
5. Name your Databricks repository and submit 
6. To install the package you need to add the repository to Databricks Python libraries
```Python
import sys
sys.path.append("/Workspace/Repos/your-account/your-repository-name/")

# Example imports
from dcg_analytics_log.report import report
from dcg_analytics_log.monitoring import meta_table

``` 
:rocket:

**Optional:**

6. `Pull` if something has been changed

### Example

The documentation of this repository is located at [Documentation](/doc/documentation.md).

For further examples of usage do not hesitate to visit our [Databricks development environment](https://adb-6936946357393751.11.azuredatabricks.net/?o=6936946357393751#folder/3690440801863555)

---
## Contribute

Dymatrix Analytik library is still in development. Hence you are welcome to give feedbacks and your contribution is very much appreciated.
If you want to contribute, please follow these steps:

1. Fork or clone the project 
2. Create your branch: `git checkout -b your-branch-name`
3. To check your new changes: `git status`
4. Commit your changes or new features: `git commit -a -m your-commit-message`
5. Push your commit to the branch: `git push -u origin your-branch-name`
6. Submit a new pull request :clap:


It is also possible to contribute directly from Databicks by following these steps:

1. Go to **_Repos_** and select your repository
2. Click on `Create branch` and enter `your-branch-name`
3. Make changes or add new features
4. Go back to **_Repos_** and make `Commit and Push` with `your-commit-message`
5. Submit a new pull request :clap:

---
