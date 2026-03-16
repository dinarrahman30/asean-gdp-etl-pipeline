# 🌍 ASEAN GDP Data Pipeline (World Bank API)

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org)
[![Prefect](https://img.shields.io/badge/Prefect-Orchestration-blueviolet.svg)](https://www.prefect.io)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Data%20Warehouse-blue.svg)](https://www.postgresql.org)
[![Podman](https://img.shields.io/badge/Podman-Containerization-892CA0.svg)](https://podman.io)
[![Grafana](https://img.shields.io/badge/Grafana-Visualization-F46800.svg)](https://grafana.com)

> An end-to-end Data Engineering portfolio project that extracts, transforms, and loads (ETL) Gross Domestic Product (GDP) data of ASEAN countries (1960-2024) using the **World Bank REST API**.

---

This project demonstrates how to build a modern data pipeline using **Python**, orchestrated with **Prefect**, stored in **PostgreSQL**, and visualized in **Grafana**, all containerized with **Podman** for easy and consistent deployment.

---

## 🏗️ Arsitektur Pipeline
 
```
World Bank REST API
        │
        ▼
 ┌─────────────┐
 │   EXTRACT   │  HTTP GET + retry otomatis (3x, delay 5s)
 └──────┬──────┘
        │ JSON
        ▼
 ┌─────────────┐
 │  TRANSFORM  │  Pandas — flatten nested fields, select kolom,
 │             │  drop null, konversi tipe data
 └──────┬──────┘
        │ DataFrame
        ▼
 ┌─────────────┐
 │    LOAD     │  SQLAlchemy → PostgreSQL (tabel: gdp_data)
 └──────┬──────┘
        │ SQL Query
        ▼
 ┌─────────────┐
 │  VISUALIZE  │  Grafana Dashboard — chart interaktif real-time
 └─────────────┘
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
