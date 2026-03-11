# 🌍 ASEAN GDP Data Pipeline (World Bank API)

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org)
[![Prefect](https://img.shields.io/badge/Prefect-Orchestration-blueviolet.svg)](https://www.prefect.io)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Data%20Warehouse-blue.svg)](https://www.postgresql.org)
[![Podman](https://img.shields.io/badge/Podman-Containerization-892CA0.svg)](https://podman.io)
[![Grafana](https://img.shields.io/badge/Grafana-Visualization-F46800.svg)](https://grafana.com)

An end-to-end Data Engineering portfolio project that extracts, transforms, and loads (ETL) Gross Domestic Product (GDP) data of ASEAN countries (1960-2024) using the **World Bank REST API**.

This project demonstrates how to build a modern data pipeline using **Python**, orchestrated with **Prefect**, stored in **PostgreSQL**, and visualized in **Grafana**, all containerized with **Podman** for easy and consistent deployment.

---

## 🏗️ Architecture & Data Flow

```mermaid
flowchart TD
    subgraph SOURCE ["📡 DATA SOURCE"]
        A["🌐 World Bank REST API\n/v2/country/.../indicator/NY.GDP.MKTP.CD"]
    end

    subgraph EXTRACT ["📥 EXTRACT"]
        B1["🔗 HTTP GET Request\nretries: 3 | delay: 5s"]
        B2["📦 Parse JSON Response"]
    end

    subgraph TRANSFORM ["🔄 TRANSFORM"]
        C1["🧹 Extract Nested Fields\ncountry.value → country"]
        C2["✂️ Select Columns\ncountry, gdp, year"]
        C3["🚫 Drop Null Values"]
        C4["🔢 Convert Data Types\nyear → int, gdp → float"]
    end

    subgraph LOAD ["📤 LOAD"]
        D1["🔐 Read .env Credentials"]
        D2["🔌 SQLAlchemy Engine"]
        D3[("🐘 PostgreSQL\ntable: gdp_data")]
    end

    subgraph VISUALIZE ["📊 VISUALIZE"]
        E1["📈 Grafana Dashboard\nReal-time Charts"]
    end

    A -->|"JSON"| B1
    B1 --> B2
    B2 -->|"Raw List"| C1
    C1 --> C2 --> C3 --> C4
    C4 -->|"Clean DataFrame"| D1
    D1 --> D2 --> D3
    D3 -->|"SQL Query"| E1

    style SOURCE fill:#E8F5E9,stroke:#4CAF50,stroke-width:2px,color:#1B5E20
    style EXTRACT fill:#EDE7F6,stroke:#7C4DFF,stroke-width:2px,color:#311B92
    style TRANSFORM fill:#FFF3E0,stroke:#FF9800,stroke-width:2px,color:#E65100
    style LOAD fill:#E3F2FD,stroke:#2196F3,stroke-width:2px,color:#0D47A1
    style VISUALIZE fill:#FBE9E7,stroke:#FF5722,stroke-width:2px,color:#BF360C
```

| Step | Process | Description |
|:---:|:---|:---|
| 📥 | **Extract** | Fetch raw JSON data from the World Bank API for ASEAN countries (Indonesia, Malaysia, Thailand, Singapore, Vietnam) with automatic retries. |
| 🔄 | **Transform** | Clean and reshape data using Pandas — extract nested values, select columns, drop nulls, and convert data types. |
| 📤 | **Load** | Connect via SQLAlchemy and load the clean DataFrame into a PostgreSQL Data Warehouse. |
| 📊 | **Visualize** | Connect Grafana to PostgreSQL to build interactive, real-time dashboards. |

---

## 🛠️ Tech Stack
- **Data Source**: World Bank REST API
- **Data Processing**: Python, Pandas
- **Orchestration**: Prefect
- **Data Warehouse**: PostgreSQL
- **Visualization**: Grafana
- **Infrastructure**: Podman & Podman Compose

---

## 📂 Repository Structure

```text
.
├── docker-compose.yml   # Container configuration for Postgres & Grafana
├── etl_worldbank.py     # Main ETL pipeline script using Prefect
├── requirements.txt     # Python dependencies
├── .env                 # Database credentials (ignored in git)
└── README.md            # Project documentation
```

## 📈 Dashboard Preview

![alt text](image.png)

Link Dashboard: https://snapshots.raintank.io/dashboard/snapshot/zfitkW0t1MeNaRIkAm9S723KP5jZOpi6

---
*Created for portfolio showcase. [Dinar W. Rahman](https://www.linkedin.com/in/dinar-wahyu-rahman)*. 2026
