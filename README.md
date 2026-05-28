<div align="center">

# 🚀 Sales Intelligence Hub

**An Enterprise-Grade Sales Analytics & Financial Intelligence Platform** *Built for multi-branch scaling, real-time revenue tracking, and precision financial reconciliation.*

[![Live Deployment](https://img.shields.io/badge/Live_App-Access_Now-000000?style=for-the-badge&logo=streamlit&logoColor=FF4B4B)](#)
[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-000000?style=for-the-badge&logo=github&logoColor=white)](#)

[![Python](https://img.shields.io/badge/Python-3.10+-0B5394?style=flat-square&logo=python&logoColor=white)](#)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](#)
[![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)](#)
[![Plotly](https://img.shields.io/badge/Data_Viz-Plotly-3F4F75?style=flat-square&logo=plotly&logoColor=white)](#)

<br/>

*Access the live deployment:* **[salesintelligence07.streamlit.app](https://salesintelligence07.streamlit.app/)**

</div>

---

## 🔐 Enterprise Demo Access
Experience the platform's Role-Based Access Control (RBAC) live. The system conditionally renders data, analytics, and permissions based on these roles:

| Access Tier | Email | Password | Branch Visibility |
| :--- | :--- | :--- | :--- |
| 👑 **Super Admin** | `superadmin@gmail.com` | `admin123` | **Global** (All Branches, Full Analytics) |
| 📍 **Branch Admin** | `chennai@gmail.com` | `admin123` | **Chennai Only** (Isolated Data) |
| 📍 **Branch Admin** | `bangalore@gmail.com` | `admin123` | **Bangalore Only** (Isolated Data) |

---

## 📸 Platform Interface

<div align="center">

### 1. Global KPI Dashboard
<img src="assets/screenshots/dashboard.png" alt="Dashboard Interface" width="850" style="border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">

### 2. Secure Access Portal
<img src="assets/screenshots/login.png" alt="Login Portal" width="850" style="border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">

### 3. Payment Reconciliation Ledger
<img src="assets/screenshots/payments.png" alt="Payments Ledger" width="850" style="border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">

### 4. Advanced Reporting & Analytics
<img src="assets/screenshots/reports.png" alt="Reporting Interface" width="850" style="border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">

*Note: If screenshots do not load, they will be automatically generated and mapped to the `/assets/screenshots/` directory upon first local runtime.*
</div>

---

## 🌌 System Workflow

```mermaid
graph LR
    A[🔐 Secure Login] -->|JWT / Session| B[📊 KPI Dashboard]
    B --> C[➕ Log Sales]
    C -->|Trigger Status| D[💳 Split Payments]
    D --> E[📈 Financial Reports]
    E --> F[🧠 AI Analytics]
    
    style A fill:#000000,stroke:#333,stroke-width:2px,color:#fff
    style B fill:#0B5394,stroke:#333,stroke-width:2px,color:#fff
    style C fill:#0B5394,stroke:#333,stroke-width:2px,color:#fff
    style D fill:#0B5394,stroke:#333,stroke-width:2px,color:#fff
    style E fill:#0B5394,stroke:#333,stroke-width:2px,color:#fff
    style F fill:#FF4B4B,stroke:#333,stroke-width:2px,color:#fff
💎 Why This Project MattersSales Intelligence Hub bridges the gap between basic ledger apps and heavy, unyielding ERP systems.Enterprise Analytics: Transforms raw transactional data into actionable, high-level business intelligence.Financial Integrity: Uses automated database triggers and generated columns to ensure mathematically flawless calculation of pending revenues and payment splits—eliminating human entry errors.Role-Based Architecture: Engineered for true SaaS multi-tenancy. Branch managers see only what they need to see, while C-suite executives maintain a macro-level overview.Scalable Design: Built on a modular, loosely-coupled architecture that is primed for migration to massive data infrastructures (like PostgreSQL and Cloud hosting) and advanced ML forecasting integration.✨ Core FeaturesFeatureDescription🛡️ Cryptographic SecurityPasswords hashed via bcrypt. Hardened session state management.🏢 Multi-Branch ArchitectureCentralized administration for distributed franchise/branch operations.💳 Intelligent LedgerTracks partial payments, aggregates splits, and auto-updates account statuses.📈 Dynamic Data VizInteractive Plotly charts engineered for responsive dark/light environments.📥 One-Click PortabilityExport filtered financial reports instantly to raw CSV for accounting sync.⚡ Real-Time ComputationDatabase-level triggers ensure metrics are strictly consistent across all views.🛠 Professional Tech StackDomainTechnologiesFrontend UIStreamlit, Streamlit ComponentsBackend LogicPython 3.10+Relational DatabaseSQLite (Production-ready via ACID compliance)Data EngineeringPandas (Vectorized computations, DataFrames)Business IntelligencePlotly Express (Interactive web-GL charts)Security & Authbcrypt, Python DotenvCloud DeploymentStreamlit Community Cloud🏗 Modern Project ArchitecturePlaintextsales_intelligence_hub/
├── 📄 app.py                  # Core application router & session manager
├── 📄 db.py                   # Data access layer & query execution engine
├── 📄 auth.py                 # Security wrapper & bcrypt hashing
├── 📄 requirements.txt        # Production dependency manifest
├── 📄 schema.sql              # DDL, constraints, generated columns & triggers
│
├── 📂 assets/                 # Static branding and interface previews
│   └── 📂 screenshots/        
│
├── 📂 pages/                  # Modular view controllers
│   ├── 📊 dashboard.py        # Macro KPI computations & visualizations
│   ├── ➕ add_customer.py     # Data entry & sanitation
│   ├── 💳 payments.py         # Split payment reconciliation engine
│   ├── 📈 reports.py          # Data table rendering & CSV export
│   └── 🔍 queries.py          # Advanced BI filtering
│
└── 📂 utils/                  # Reusable engineering modules
    ├── 🛠️ helpers.py          # State management & formatting
    ├── 📉 charts.py           # Plotly graph generators
    └── ✅ validators.py       # Input sanitation & error handling
⚡ Installation & Local DeploymentDeploy the system locally in under 60 seconds.Bash# 1. Clone the repository
git clone [https://github.com/yourusername/sales_intelligence_hub.git](https://github.com/yourusername/sales_intelligence_hub.git)

# 2. Traverse into the directory
cd sales_intelligence_hub

# 3. Initialize virtual environment (Recommended)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# 4. Install enterprise dependencies
pip install -r requirements.txt

# 5. Launch the application server
streamlit run app.py
🚀 Future Roadmap & Scaling[ ] AI-Powered Analytics: Integrate LLM agents for natural-language querying of sales data.[ ] Predictive Forecasting: Implement ARIMA/Prophet models to predict Q3/Q4 branch revenue.[ ] PostgreSQL Migration: Transition from SQLite to highly-concurrent PostgreSQL via SQLAlchemy.[ ] Automated Alerts: Send scheduled email digests (via SendGrid) for high-value closures.[ ] SaaS Multi-Tenancy: Upgrade schema to support isolated, multi-company subscriptions.
