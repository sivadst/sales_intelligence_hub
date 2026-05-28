<div align="center">

# 🚀 Sales Intelligence Hub

**An Enterprise-Grade Sales Analytics & Financial Intelligence Platform** *Built for multi-branch scaling, real-time revenue tracking, and precision financial reconciliation.*

<br />

[![Live Deployment](https://img.shields.io/badge/Live_App-Access_Now-000000?style=for-the-badge&logo=streamlit&logoColor=FF4B4B)](https://salesintelligence07.streamlit.app/)
[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-000000?style=for-the-badge&logo=github&logoColor=white)](#)

[![Python](https://img.shields.io/badge/Python-3.10+-0B5394?style=flat-square&logo=python&logoColor=white)](#)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](#)
[![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)](#)
[![Plotly](https://img.shields.io/badge/Data_Viz-Plotly-3F4F75?style=flat-square&logo=plotly&logoColor=white)](#)

<br />

*Access the live deployment:* **[salesintelligence07.streamlit.app](https://salesintelligence07.streamlit.app/)**

</div>

<br />

---

<br />

## 🔐 Enterprise Demo Access

Experience the platform's **Role-Based Access Control (RBAC)** live. The system conditionally renders data, analytics, and permissions based on the active user session.

| Access Tier | Email | Password | Branch Visibility |
| :--- | :--- | :--- | :--- |
| 👑 **Super Admin** | `superadmin@gmail.com` | `admin123` | **Global** (All Branches, Full Analytics) |
| 📍 **Branch Admin** | `chennai@gmail.com` | `admin123` | **Chennai Only** (Isolated Data) |
| 📍 **Branch Admin** | `bangalore@gmail.com` | `admin123` | **Bangalore Only** (Isolated Data) |

<br />

---

<br />

## 📸 Platform Interface

<div align="center">

### 1. Global KPI Dashboard
<img src="assets/screenshots/dashboard.png" alt="Dashboard Interface" width="850" style="border-radius: 12px; box-shadow: 0 8px 16px rgba(0,0,0,0.15); margin-bottom: 20px;">

### 2. Secure Access Portal
<img src="assets/screenshots/login.png" alt="Login Portal" width="850" style="border-radius: 12px; box-shadow: 0 8px 16px rgba(0,0,0,0.15); margin-bottom: 20px;">

### 3. Payment Reconciliation Ledger
<img src="assets/screenshots/payments.png" alt="Payments Ledger" width="850" style="border-radius: 12px; box-shadow: 0 8px 16px rgba(0,0,0,0.15); margin-bottom: 20px;">

### 4. Advanced Reporting & Analytics
<img src="assets/screenshots/reports.png" alt="Reporting Interface" width="850" style="border-radius: 12px; box-shadow: 0 8px 16px rgba(0,0,0,0.15); margin-bottom: 20px;">

</div>

<br />

---

<br />

## 🌌 System Workflow

```mermaid
graph LR
    A[🔐 Secure Login] -->|Session State| B[📊 KPI Dashboard]
    B --> C[➕ Log Sales]
    C -->|Trigger Status| D[💳 Split Payments]
    D --> E[📈 Financial Reports]
    E --> F[🧠 BI Analytics]
    
    style A fill:#000000,stroke:#333,stroke-width:2px,color:#fff
    style B fill:#0B5394,stroke:#333,stroke-width:2px,color:#fff
    style C fill:#0B5394,stroke:#333,stroke-width:2px,color:#fff
    style D fill:#0B5394,stroke:#333,stroke-width:2px,color:#fff
    style E fill:#0B5394,stroke:#333,stroke-width:2px,color:#fff
    style F fill:#FF4B4B,stroke:#333,stroke-width:2px,color:#fff
💎 Why This Project MattersSales Intelligence Hub bridges the gap between basic ledger apps and heavy, unyielding ERP systems."Designed to transform raw transactional data into actionable, high-level business intelligence."Enterprise Analytics: Automates complex financial calculations to provide immediate insight into branch performance.Financial Integrity: Leverages advanced database triggers and generated columns to guarantee mathematically flawless reconciliation of pending revenues.Role-Based Architecture: Engineered for true SaaS multi-tenancy. Branch managers see localized data, while C-suite executives maintain a macro-level overview.Scalable Design: Built on a modular, loosely-coupled Python architecture primed for massive data infrastructures and future machine learning integrations.✨ Core FeaturesFeatureCapabilityDescription🛡️ Cryptographic SecurityAuth & IdentityPasswords hashed via bcrypt. Hardened session state management.🏢 Multi-Branch ArchitectureScalabilityCentralized administration for distributed franchise/branch operations.💳 Intelligent LedgerFinancial OpsTracks partial payments, aggregates splits, and auto-updates statuses.📈 Dynamic Data VizBusiness IntelInteractive Plotly charts engineered for responsive web environments.📥 One-Click PortabilityExport & SyncExport filtered financial reports instantly to raw CSV for accounting.⚡ Real-Time ComputationData IntegrityDatabase-level triggers ensure metrics are strictly consistent.🛠 Professional Tech StackDomainTechnologies UsedFrontend UIStreamlit, Streamlit Components, CSSBackend LogicPython 3.10+Relational DatabaseSQLite (ACID compliant, production-ready schema)Data EngineeringPandas (Vectorized computations, DataFrames)Business IntelligencePlotly Express (Interactive WebGL charts)Security & Authbcrypt, Python DotenvCloud DeploymentStreamlit Community Cloud🏗 Modern Project ArchitecturePlaintextsales_intelligence_hub/
├── 📄 app.py                  # Core application router & session manager
├── 📄 db.py                   # Data access layer & query execution engine
├── 📄 auth.py                 # Security wrapper & bcrypt hashing
├── 📄 requirements.txt        # Production dependency manifest
├── 📄 schema.sql              # DDL, constraints, generated columns & triggers
│
├── 📂 assets/                 # Static branding and interface previews
│   └── 📂 screenshots/        # Directory for application interface images
│
├── 📂 pages/                  # Modular view controllers
│   ├── 📊 dashboard.py        # Macro KPI computations & visualizations
│   ├── ➕ add_customer.py     # Data entry & sanitation logic
│   ├── 💳 payments.py         # Split payment reconciliation engine
│   ├── 📈 reports.py          # Data table rendering & CSV export
│   └── 🔍 queries.py          # Advanced BI filtering algorithms
│
└── 📂 utils/                  # Reusable engineering modules
    ├── 🛠️ helpers.py          # State management & component formatting
    ├── 📉 charts.py           # Plotly graph generators
    └── ✅ validators.py       # Input sanitation & error handling
⚡ Installation & Local DeploymentDeploy the system locally in under 60 seconds.Bash# 1. Clone the enterprise repository
git clone [https://github.com/yourusername/sales_intelligence_hub.git](https://github.com/yourusername/sales_intelligence_hub.git)

# 2. Traverse into the directory
cd sales_intelligence_hub

# 3. Initialize secure virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# 4. Install production dependencies
pip install -r requirements.txt

# 5. Launch the application server
streamlit run app.py
🚀 Future Roadmap & Scaling[ ] AI-Powered Analytics: Integrate LLM agents for natural-language querying of historical sales data.[ ] Predictive Forecasting: Implement ARIMA/Prophet machine learning models to predict Q3/Q4 branch revenue.[ ] PostgreSQL Migration: Transition from SQLite to highly-concurrent PostgreSQL via SQLAlchemy for enterprise scaling.[ ] Automated Alerts: Configure scheduled email digests (via SendGrid/AWS SES) for high-value deal closures.[ ] SaaS Multi-Tenancy: Upgrade database schema to support fully isolated, multi-company subscriptions.Built with ambition, analytics, and engineering precision.
