# India Mandi Price Analytics System

A production-grade data engineering project analyzing agricultural wholesale market prices across India's 1,800+ regulated mandis.

## 📋 Project Overview

This project builds an end-to-end data pipeline that ingests daily mandi price data from government APIs, transforms it through multiple layers, and produces analytics-ready tables for price analysis, regional comparison, and trend identification.

**Why this project?**
- **Unique domain**: Rarely seen in data engineering portfolios
- **Real messiness**: Handles actual government data inconsistencies (naming, units, dates)
- **Production patterns**: Demonstrates scheduling, orchestration, monitoring, and testing
- **Clear business value**: Solves a real problem for farmers, traders, and policymakers

## 🏗️ Architecture

The project follows the **Medallion Architecture** pattern:
```
API Data → BRONZE (Raw) → PySpark Cleaning → SILVER (Clean) → dbt Models → GOLD (Analytics)
                                                                              ↓
                                                                    SQL Server Tables
                                                                    (Dimensions & Facts)
```

**Layers:**
- **Bronze**: Raw data exactly as received from APIs (Parquet format)
- **Silver**: Cleaned, standardized, deduplicated data (Parquet format)
- **Gold**: Business-ready dimensional model in SQL Server (staging, intermediate, marts schemas)

## 📊 Data Sources

| Source      | Type     | Coverage                     | Update Frequency |
|-------------|----------|------------------------------|------------------|
| data.gov.in | REST API | 1,800+ mandis, 10+ years     | Daily            |
| CEDA Ashoka | REST API | Pre-cleaned academic version | Daily            |
| FAOSTAT     | CSV      | Global FAO data (reference)  | Annual           |

## 🛠️ Tech Stack

| Component           | Technology     | Purpose                          |
|---------------------|----------------|----------------------------------|
| **Language**        | Python 3.10    | Scripting & ingestion            |
| **Big Data**        | PySpark 4.0.1  | Data transformation at scale     |
| **Orchestration**   | Dagster 1.12.3 | Pipeline scheduling & monitoring |
| **Transformation**  | dbt 1.4.3      | SQL transformations & testing    |
| **Database**        | SQL Server     | Analytics warehouse              |
| **Version Control** | Git + GitHub   | Code management                  |
| **Testing**         | pytest         | Unit & integration tests         |

## 📁 Project Structure
```
India Mandi Price Analytics System/
├── config/                          # Configuration files
│   ├── __init__.py
│   ├── settings.py                 # Environment variables & paths
│   ├── commodities.py              # Commodity name mappings
│   └── states.py                   # State name mappings
├── data/                           # Data storage (NOT committed)
│   ├── bronze/                     # Raw API data
│   │   ├── mandi_prices/
│   │   └── reference/
│   ├── silver/                     # Cleaned data
│   │   ├── mandi_prices_clean/
│   │   ├── commodities_dim/
│   │   └── markets_dim/
│   └── reference/                  # Static reference files
├── src/                            # Source code
│   ├── ingestion/                  # API data extraction
│   │   ├── mandi_api.py           # data.gov.in & CEDA API calls
│   │   └── reference_loader.py    # Reference data loading
│   ├── transformation/             # PySpark data cleaning
│   │   ├── clean_mandi_prices.py  # Standardization logic
│   │   └── create_dimensions.py   # Dimension table creation
│   ├── utils/                      # Reusable utilities
│   │   ├── logger.py              # Logging setup
│   │   ├── api_client.py          # Generic API client with retry logic
│   │   └── validators.py          # Data validation functions
│   └── pipelines/                  # Dagster orchestration
│       ├── definitions.py          # Asset & job definitions
│       └── assets/                 # Asset implementations
├── dbt_project/                    # dbt transformation project
│   ├── models/
│   │   ├── staging/               # Raw to cleaned (sources)
│   │   ├── intermediate/          # Staging to intermediate (CTEs)
│   │   └── marts/                 # Intermediate to gold (facts & dims)
│   ├── tests/                      # Data quality tests
│   ├── macros/                     # Custom SQL macros
│   └── dbt_project.yml            # dbt configuration
├── tests/                          # Python unit tests
│   ├── test_ingestion.py          # API ingestion tests
│   └── test_transformations.py    # PySpark transformation tests
├── notebooks/                      # Jupyter notebooks for exploration
├── .env                           # Environment variables (DO NOT COMMIT)
├── .env.example                   # Template for .env
├── .gitignore                     # Git ignore rules
├── README.md                      # This file
└── requirements.txt               # Python dependencies
```

## 🚀 Getting Started

### Prerequisites
- Python 3.10 (via Anaconda)
- SQL Server Express (local installation)
- Java JDK 17
- Git
- API keys from data.gov.in and CEDA Ashoka (free registration)

### Setup Instructions

**1. Clone repository & navigate to project:**
```powershell
cd "D:\Career\Computer Science\Data Engineering & Analytics\~My project\India Mandi Price Analytics System"
conda activate dataeng
```

**2. Install dependencies:**
```powershell
pip install -r requirements.txt
```

**3. Set up environment variables:**
- Copy `.env.example` to `.env`
- Fill in your API keys:
  - `DATA_GOV_API_KEY` from https://data.gov.in
  - `CEDA_API_KEY` from https://api.ceda.ashoka.edu.in

**4. Create SQL Server database & schemas:**
```powershell
# Run PowerShell commands to create mandi_analytics database with staging, intermediate, marts schemas
# (See SQL Server setup guide)
```

**5. Test dbt connection:**
```powershell
cd dbt_project
dbt debug
# Expected output: All checks passed!
```

**6. Run initial ingestion (Week 1-2):**
```powershell
python src/ingestion/mandi_api.py
```

## 📅 Implementation Timeline

| Week   | Focus                 | Deliverables                        |
|--------|-----------------------|-------------------------------------|
| 1-2    | Ingestion Layer       | API integration, Bronze layer data  |
| 3-4    | PySpark Cleaning      | Silver layer transformations        |
| 5-6    | dbt Models            | Staging, intermediate, marts models |
| 7      | Dagster Orchestration | Scheduled daily pipeline            |
| 8      | Testing & Polish      | Tests, documentation, cleanup       |

## 🧪 Testing

**Run Python tests:**
```powershell
pytest tests/ -v
pytest tests/ --cov=src  # With coverage report
```

**Run dbt tests:**
```powershell
cd dbt_project
dbt test
```

## 🔄 Running the Pipeline

**Manual execution:**
```powershell
# Ingest data
python src/ingestion/mandi_api.py

# Clean data with PySpark
python src/transformation/clean_mandi_prices.py

# Transform with dbt
cd dbt_project && dbt run
```

**Automated with Dagster (Week 7+):**
```powershell
dagster dev -f src/pipelines/definitions.py
# Open: http://localhost:3000
```

## 📚 Key Concepts Demonstrated

- **API Integration**: Pagination, retry logic, error handling, rate limiting
- **Data Quality**: Handling inconsistencies in naming, units, dates, missing values
- **Big Data Processing**: PySpark DataFrames, transformations, partitioning
- **SQL Transformations**: CTEs, window functions, aggregations
- **dbt Workflows**: Models, tests, documentation, incremental loads
- **Orchestration**: Dagster assets, dependencies, scheduling
- **Testing**: Unit tests, integration tests, data quality checks
- **Git Workflow**: Version control, commits, GitHub collaboration

## 🎯 Learning Outcomes

After completing this project, you'll understand:
- How production data pipelines handle real-world messiness
- End-to-end pipeline architecture (ingestion → transformation → loading)
- Local development workflow for data engineering
- How local tools map to cloud equivalents (Azure Databricks, Synapse)
- Interview-ready project explanation with concrete examples

## 📖 Documentation

- [SQL Server Setup Guide](./docs/sql-server-setup.md)
- [Data Dictionary](./docs/data-dictionary.md) - Field definitions & mappings
- [Architecture Diagram](./docs/architecture.md) - Visual system design
- [Troubleshooting Guide](./docs/troubleshooting.md) - Common issues & solutions

## 🔐 Security

- **Never commit `.env`** — it contains API keys
- **Use `.env.example`** as a template for new contributors
- **Rotate API keys** periodically
- **Review `.gitignore`** to ensure no secrets are exposed

## 🚢 Next Steps / Future Enhancements

- [ ] Add 5 more commodities (extend coverage)
- [ ] Add 10 more states (pan-India analytics)
- [ ] Build price prediction model (ML extension)
- [ ] Create Streamlit dashboard (visual demo)
- [ ] Migrate to cloud (Azure Data Lake + Databricks)
- [ ] Add data quality monitoring & alerting

## 🤝 Contributing

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Make changes and test: `pytest tests/`
3. Commit with clear message: `git commit -m "Add feature description"`
4. Push to GitHub: `git push origin feature/your-feature`

## 📞 Support

If you encounter issues:
1. Check [Troubleshooting Guide](./docs/troubleshooting.md)
2. Review logs in `src/utils/logger.py`
3. Check dbt debug: `dbt debug`
4. Search GitHub issues

## 📄 License

This project is for educational and portfolio purposes.

## 🎓 Learning Resources

- **dbt Documentation**: https://docs.getdbt.com
- **Dagster Documentation**: https://docs.dagster.io
- **PySpark SQL**: https://spark.apache.org/docs/latest/api/python/
- **India Mandi Data**: https://data.gov.in
- **CEDA Ashoka API**: https://api.ceda.ashoka.edu.in

---

**Status**: 🚧 In Development (Week 1-2 focus: Ingestion Layer)

**Last Updated**: January 2025

**Author**: Pradeep (Learning Data Engineering)
```

---