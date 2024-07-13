# Data-Cleaning
<br/>
Data cleaning is one of the important parts of machine learning. It plays a significant part in building a model.<br/>
<br/>
What is Data Cleaning <br/>
Data cleaning is a crucial step in the machine learning (ML) pipeline, as it involves identifying and removing any **missing, duplicate, or irrelevant data**. The goal of data cleaning is to ensure that the data is accurate, consistent, and free of errors, as incorrect or inconsistent data can negatively impact the performance of the ML model. Professional data scientists usually invest a very large portion of their time in this step because of the belief that **“Better data beats fancier algorithms”**.<br/>
<br/>

**Why is Data Cleaning Important?**<br/>
Data cleansing is a crucial step in the data preparation process, playing an important role in ensuring the accuracy, reliability, and overall quality of a dataset.<br/>
For decision-making, the integrity of the conclusions drawn heavily relies on the cleanliness of the underlying data. Without proper data cleaning, inaccuracies, outliers, missing values, and inconsistencies can compromise the validity of analytical results. Moreover, clean data facilitates more effective modeling and pattern recognition, as algorithms perform optimally when fed high-quality, error-free input.<br/>
Additionally, clean datasets enhance the interpretability of findings, aiding in the formulation of actionable insights.<br/>
<br/>

**Steps to Perform Data Cleanliness**<br/>
*   **Removal of Unwanted Observations**: Identify and eliminate irrelevant or redundant observations from the dataset. The step involves scrutinizing data entries for duplicate records, irrelevant information, or data points that do not contribute meaningfully to the analysis. Removing unwanted observations streamlines the dataset, reducing noise and improving the overall quality.

*   **Fixing Structure errors**: Address structural issues in the dataset, such as inconsistencies in data formats, naming conventions, or variable types. Standardize formats, correct naming discrepancies, and ensure uniformity in data representation. Fixing structure errors enhances data consistency and facilitates accurate analysis and interpretation.

*   **Managing Unwanted outliers**: Identify and manage outliers, which are data points significantly deviating from the norm. Depending on the context, decide whether to remove outliers or transform them to minimize their impact on analysis. Managing outliers is crucial for obtaining more accurate and reliable insights from the data.

* **Handling Missing Data**: Devise strategies to handle missing data effectively. This may involve imputing missing values based on statistical methods, removing records with missing values, or employing advanced imputation techniques. Handling missing data ensures a more complete dataset, preventing biases and maintaining the integrity of analyses. <br/>
<br/>

**Usage**<br/>
Follow these steps to clean your data:<br/>
1. Load Data: Load your raw data using the load_data.py script.
2. Clean Data: Use the clean_data.py script to handle missing values, remove duplicates, and correct errors.
3. Transform Data: Apply necessary transformations using the transform_data.py script.
4. Save Data: Save the cleaned data using the save_data.py script.<br/>
<br/>

**Features**<br/>
1. Missing Values Handling: Impute or remove missing values.
2. Duplicate Removal: Detect and remove duplicate entries.
3. Error Correction: Identify and correct errors in data entries.
4. Data Transformation: Apply transformations such as scaling, encoding, etc.

