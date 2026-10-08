# Customer Segmentation

A Python-based Data Science project that analyzes e-commerce customer transactions and groups customers based on their purchasing behavior using **RFM Analysis and K-Means Clustering**.

## Project Overview

The project uses the **Online Retail Dataset** from Kaggle to analyze customer behavior.

Main techniques used:

* Data cleaning and preprocessing
* File and exception handling
* Web scraping
* RFM Analysis
* SQLite CRUD operations
* Statistical analysis
* Data visualization
* Probability analysis
* K-Means clustering
* PCA visualization
* Hypothesis testing
* Confidence interval

## Dataset

**Online Retail Dataset – Kaggle**

https://www.kaggle.com/datasets/carrie1/ecommerce-data

The dataset contains information such as:

* Invoice Number
* Product Description
* Quantity
* Invoice Date
* Unit Price
* Customer ID
* Country

## RFM Analysis

Customers are analyzed using:

* **Recency** – How recently the customer purchased
* **Frequency** – Number of orders made
* **Monetary** – Total amount spent

## Machine Learning

**K-Means Clustering** is used to segment customers based on their RFM values.

The project uses:

* StandardScaler
* Elbow Method
* Silhouette Score
* PCA

Four customer segments are created:

| Segment    | Description                  |
| ---------- | ---------------------------- |
| Champions  | Highest-value customers      |
| Loyal      | Strong purchasing behavior   |
| Occasional | Moderate purchasing behavior |
| Low Value  | Relatively low spending      |

## Database

SQLite is used for customer data and demonstrates:

* Create
* Read
* Update
* Delete

Database file:

`customers.db`

## Statistical Analysis

The project calculates:

* Mean
* Median
* Standard Deviation
* Skewness
* Correlation
* Probability
* 95% Confidence Interval
* T-Test
* ANOVA
* Chi-Square Test

## Output Files

The project generates:

* `customers_segmented.csv` – Segmented customer data
* `segment_summary.json` – Segment summary
* `report.txt` – Customer segment report

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* SciPy
* Scikit-learn
* BeautifulSoup
* Requests
* SQLite
* KaggleHub
* Jupyter Notebook

## Project Files

```text
Customer-Segmentation-Python/
│
├── Customer_Segmentation.ipynb
├── my_utils.py
├── data.csv
└── README.md
```

## Conclusion
This project demonstrates the practical application of **Python and Data Science** techniques to real-world e-commerce data. RFM analysis and K-Means clustering are used to identify meaningful customer segments and understand their purchasing behavior.
