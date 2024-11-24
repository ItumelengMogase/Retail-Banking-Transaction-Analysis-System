# **Retail Banking Data Warehouse**

## **Project Overview**
This project demonstrates the implementation of a retail banking data warehouse using Kimball's dimensional modelling methodology. The objective is to create a scalable and efficient system to analyse customer transactions, account information, and transaction trends using Azure cloud services. The project includes ETL pipelines, star schema design, and a Power BI dashboard for visualisation.

---

## **Key Features**
1. **Star Schema Data Warehouse**:
   - Built using Kimball's methodology for high-performance reporting.
2. **ETL Pipeline**:
   - Extract, transform, and load data from raw CSV files into the data warehouse.
3. **Cloud-Based Implementation**:
   - Utilises Azure services such as PostgreSQL, Blob Storage, and Databricks.
4. **Interactive Dashboard**:
   - Power BI dashboard visualising key banking metrics like transaction trends and customer segmentation.

---

## **Project Structure**
```
retail_banking_analysis/
├── datasets/
│   ├── customers.csv          # Mock dataset for customer details
│   ├── accounts.csv           # Mock dataset for account details
│   ├── transactions.csv       # Mock dataset for transactions
│   ├── time.csv               # Mock dataset for time dimension
├── etl/
│   ├── extract.py             # Script to extract data from source files
│   ├── transform.py           # Script to clean and transform data
│   ├── load.py                # Script to load data into PostgreSQL
├── schemas/
│   ├── star_schema.sql        # SQL script to create the star schema
├── terraform/
│   ├── main.tf                # Terraform script to provision Azure services
├── notebooks/
│   ├── spark_etl.ipynb        # Databricks notebook for transformation
├── dashboards/
│   ├── power_bi.pbix          # Power BI dashboard file
├── README.md                  # Project documentation
└── LICENSE                    # License for project
```

---

## **Star Schema Design**
The data warehouse uses the following schema:
- **Fact Table**: `transactions_fact` – stores transaction details.
- **Dimension Tables**:
  - `customers_dim`: Stores customer demographic details.
  - `accounts_dim`: Stores account information.
  - `time_dim`: Stores calendar-based attributes.
  - `transaction_types_dim`: Stores transaction categories.

---

## **ETL Pipeline**
The ETL pipeline extracts data from CSV files, performs transformations, and loads it into the PostgreSQL database. 

### **Pipeline Workflow**
1. **Extract**:
   - Load raw datasets from `datasets/` folder or Azure Blob Storage.
2. **Transform**:
   - Clean, normalise, and map data to dimension and fact tables.
   - Use PySpark in Databricks for heavy transformations.
3. **Load**:
   - Load transformed data into Azure PostgreSQL using SQLAlchemy.

---

## **Azure Services Used**
1. **Azure Database for PostgreSQL**:
   - Serves as the data warehouse backend.
2. **Azure Blob Storage**:
   - Stores raw datasets for ETL ingestion.
3. **Azure Databricks**:
   - Used for data transformation using PySpark.
4. **Azure Terraform**:
   - Automates provisioning of resources.

---

## **Power BI Dashboard**
The dashboard connects to the Azure PostgreSQL database and provides the following insights:
- **Transaction Trends**: Line chart showing transaction volumes over time.
- **Regional Analysis**: Map visualisation of transaction volume by region.
- **Top Transaction Types**: Bar chart of the most common transaction categories.

---

## **Setup Instructions**
### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/Retail-Banking-Transaction-Analysis-System.git
cd     Retail-Banking-Transaction-Analysis-System

```

### **2. Set Up Azure Services**
- Provision the following services:
  - **Azure Database for PostgreSQL**: Create a database named `banking_dw`.
  - **Azure Blob Storage**: Create a container for raw data.
  - **Azure Databricks**: Create a workspace for data transformations.

### **3. Create the Data Warehouse Schema**
Run the SQL script to set up the star schema:
```bash
psql -h <your-postgresql-host> -U <your-username> -d banking_dw -f schemas/star_schema.sql
```

### **4. Run ETL Pipeline**
1. Install dependencies:
   ```bash
   pip install pandas sqlalchemy psycopg2
   ```
2. Execute the pipeline:
   ```bash
   python etl/extract.py
   python etl/transform.py
   python etl/load.py
   ```

### **5. Visualise Data with Power BI**
1. Open `dashboards/power_bi.pbix` in Power BI Desktop.
2. Configure the connection to the Azure PostgreSQL database.
3. Publish the dashboard.

---

## **Datasets**
The project uses mock datasets stored in the `datasets/` folder.

---

## **Key Technologies**
- **Cloud**: Azure PostgreSQL, Blob Storage, Databricks.
- **ETL**: Python, PySpark.
- **Database**: PostgreSQL.
- **Visualisation**: Power BI.
- **IaC**: Terraform.

---

## **Future Enhancements**
1. Add support for real-time data ingestion using Azure Event Hubs.
2. Implement CI/CD pipelines for automated ETL deployments.
3. Extend dashboards with predictive analytics using Azure Machine Learning.

---

## **License**
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## **Contributors**
- **[Itumeleng Mogase](https://github.com/ItumelengMogase)**: Data Engineering and Dashboard Development.
- Open to collaborators! Fork the repo and submit pull requests.

--- 

Let me know if you'd like help tailoring this further!
