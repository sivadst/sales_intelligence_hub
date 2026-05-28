<div align="center">
<br/>
<!-- LOGO / HERO -->
<img src="https://img.shields.io/badge/⬡-SalesIntel_Pro-1f6feb?style=for-the-badge&labelColor=0d1117&color=1f6feb" alt="SalesIntel Pro" height="48"/>
<br/><br/>
SalesIntel Pro
Full-Stack Sales Intelligence Dashboard
Real-time revenue analytics · payment tracking · pipeline management · team performance
<br/>
Show Image
 
Show Image
 
Show Image
 
Show Image
<br/>
Show Image
Show Image
Show Image
Show Image
</div>
<br/>

<br/>
Why This Project Matters

Most small businesses make critical sales decisions based on spreadsheets, gut feelings, and fragmented data.
SalesIntel Pro changes that — by turning raw transaction data into a real-time command center.

Traditional BI tools like Tableau or Power BI are expensive, complex, and gated behind enterprise budgets. This project proves that a solo developer, armed with Python and a clear vision, can build a production-grade analytics platform that rivals commercial solutions — without the license fees.
This is not a tutorial project. It is a fully functional business application with:

Secure multi-role authentication — no third-party OAuth needed
Live MySQL integration — real relational data, not mock CSV files
PDF invoice generation — customer-ready deliverables, on demand
Responsive, dark-mode UI — designed for real-world daily use

<br/>

<br/>
Screenshots
<br/>
🔐 Login & Authentication
<div align="center">
  <img src="assets/screenshots/login.png" alt="SalesIntel Pro — Login Page" width="90%" style="border-radius: 12px; border: 1px solid #30363d;"/>
  <br/>
  <sub><i>Role-based login with Admin and Sales Rep access levels</i></sub>
</div>
<br/><br/>
📊 Dashboard Overview
<div align="center">
  <img src="assets/screenshots/dashboard.png" alt="SalesIntel Pro — Dashboard" width="90%" style="border-radius: 12px; border: 1px solid #30363d;"/>
  <br/>
  <sub><i>Live KPIs · Revenue trend chart · Sales pipeline donut · Recent transactions ledger</i></sub>
</div>
<br/><br/>
💳 Payments & Transactions
<div align="center">
  <img src="assets/screenshots/payments.png" alt="SalesIntel Pro — Payments" width="90%" style="border-radius: 12px; border: 1px solid #30363d;"/>
  <br/>
  <sub><i>Full payment ledger with invoice tracking, overdue flags, and partial payment states</i></sub>
</div>
<br/><br/>
📈 Reports & Analytics
<div align="center">
  <img src="assets/screenshots/reports.png" alt="SalesIntel Pro — Reports" width="90%" style="border-radius: 12px; border: 1px solid #30363d;"/>
  <br/>
  <sub><i>Monthly revenue bars · Top performers leaderboard · Quarterly forecast vs actuals</i></sub>
</div>
<br/><br/>
🔬 Advanced Analytics
<div align="center">
  <img src="assets/screenshots/analytics.png" alt="SalesIntel Pro — Advanced Analytics" width="90%" style="border-radius: 12px; border: 1px solid #30363d;"/>
  <br/>
  <sub><i>Activity heatmap · Conversion funnel · Revenue vs target trend · Win rate & CAC KPIs</i></sub>
</div>
<br/>

<br/>
Core Features
<br/>
ModuleCapabilityDetails🔐 Auth SystemRole-based loginAdmin vs Sales Rep — pure Python + MySQL, no OAuth📊 DashboardLive KPI cardsRevenue, active clients, pending deals, conversion rate📊 DashboardRevenue trendMonthly bar chart with Plotly interactivity📊 DashboardPipeline viewDonut chart — Prospecting / Qualified / Proposal / Closed💳 PaymentsPayment ledgerInvoice tracking with Paid / Partial / Pending / Overdue states💳 PaymentsFinancial KPIsTotal collected, pending balance, overdue, current month📈 ReportsMonthly revenueBar chart with current-month highlight📈 ReportsTop performersLeaderboard with revenue, deals, and conversion %📈 ReportsForecast vs actualsQuarterly target tracking with variance and achievement %🔬 AnalyticsActivity heatmapCalls & demos by day/hour — spot your peak performance windows🔬 AnalyticsConversion funnelLead → Qualified → Proposal → Negotiation → Closed🔬 AnalyticsDaily trendRevenue vs target, plotted over time📄 InvoicingPDF generationClean, customer-ready invoices generated on demand via FPDF🎛 FiltersGlobal sidebarFilter by region, city, category, rep, date range — all charts update live
<br/>

<br/>
Tech Stack
<br/>
LayerTechnologyPurposeFrontendStreamlit 1.xUI framework — pages, layout, sidebar, stateChartsPlotly ExpressInteractive bar, line, pie, funnel, heatmapDataPandasData wrangling, filtering, aggregationDatabaseMySQL 8.0Users, products, sales, invoice dataDB Drivermysql-connector-pythonPython ↔ MySQL bridgePDF EngineFPDF2Invoice generation and downloadAuthCustom PythonSession state + role logic, no external librariesDeploymentStreamlit CloudOne-click deploy from GitHubRuntimePython 3.10+Core language
<br/>

<br/>
Architecture
<br/>
#mermaid-raj-r1{font-family:"Anthropic Sans",system-ui,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;font-size:16px;fill:#E5E5E5;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-raj-r1 .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-raj-r1 .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-raj-r1 .error-icon{fill:#CC785C;}#mermaid-raj-r1 .error-text{fill:#3387a3;stroke:#3387a3;}#mermaid-raj-r1 .edge-thickness-normal{stroke-width:1px;}#mermaid-raj-r1 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-raj-r1 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-raj-r1 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-raj-r1 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-raj-r1 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-raj-r1 .marker{fill:#A1A1A1;stroke:#A1A1A1;}#mermaid-raj-r1 .marker.cross{stroke:#A1A1A1;}#mermaid-raj-r1 svg{font-family:"Anthropic Sans",system-ui,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;font-size:16px;}#mermaid-raj-r1 p{margin:0;}#mermaid-raj-r1 .label{font-family:"Anthropic Sans",system-ui,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;color:#E5E5E5;}#mermaid-raj-r1 .cluster-label text{fill:#3387a3;}#mermaid-raj-r1 .cluster-label span{color:#3387a3;}#mermaid-raj-r1 .cluster-label span p{background-color:transparent;}#mermaid-raj-r1 .label text,#mermaid-raj-r1 span{fill:#E5E5E5;color:#E5E5E5;}#mermaid-raj-r1 .node rect,#mermaid-raj-r1 .node circle,#mermaid-raj-r1 .node ellipse,#mermaid-raj-r1 .node polygon,#mermaid-raj-r1 .node path{fill:transparent;stroke:#A1A1A1;stroke-width:1px;}#mermaid-raj-r1 .rough-node .label text,#mermaid-raj-r1 .node .label text,#mermaid-raj-r1 .image-shape .label,#mermaid-raj-r1 .icon-shape .label{text-anchor:middle;}#mermaid-raj-r1 .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#mermaid-raj-r1 .rough-node .label,#mermaid-raj-r1 .node .label,#mermaid-raj-r1 .image-shape .label,#mermaid-raj-r1 .icon-shape .label{text-align:center;}#mermaid-raj-r1 .node.clickable{cursor:pointer;}#mermaid-raj-r1 .root .anchor path{fill:#A1A1A1!important;stroke-width:0;stroke:#A1A1A1;}#mermaid-raj-r1 .arrowheadPath{fill:#0b0b0b;}#mermaid-raj-r1 .edgePath .path{stroke:#A1A1A1;stroke-width:1px;}#mermaid-raj-r1 .flowchart-link{stroke:#A1A1A1;fill:none;}#mermaid-raj-r1 .edgeLabel{background-color:transparent;text-align:center;}#mermaid-raj-r1 .edgeLabel p{background-color:transparent;}#mermaid-raj-r1 .edgeLabel rect{opacity:0.5;background-color:transparent;fill:transparent;}#mermaid-raj-r1 .labelBkg{background-color:rgba(0, 0, 0, 0.5);}#mermaid-raj-r1 .cluster rect{fill:#CC785C;stroke:hsl(15, 12.3364485981%, 48.0392156863%);stroke-width:1px;}#mermaid-raj-r1 .cluster text{fill:#3387a3;}#mermaid-raj-r1 .cluster span{color:#3387a3;}#mermaid-raj-r1 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:"Anthropic Sans",system-ui,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;font-size:12px;background:#CC785C;border:1px solid hsl(15, 12.3364485981%, 48.0392156863%);border-radius:2px;pointer-events:none;z-index:100;}#mermaid-raj-r1 .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#E5E5E5;}#mermaid-raj-r1 rect.text{fill:none;stroke-width:0;}#mermaid-raj-r1 .icon-shape,#mermaid-raj-r1 .image-shape{background-color:transparent;text-align:center;}#mermaid-raj-r1 .icon-shape p,#mermaid-raj-r1 .image-shape p{background-color:transparent;padding:2px;}#mermaid-raj-r1 .icon-shape .label rect,#mermaid-raj-r1 .image-shape .label rect{opacity:0.5;background-color:transparent;fill:transparent;}#mermaid-raj-r1 .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#mermaid-raj-r1 .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#mermaid-raj-r1 .node .neo-node{stroke:#A1A1A1;}#mermaid-raj-r1 [data-look="neo"].node rect,#mermaid-raj-r1 [data-look="neo"].cluster rect,#mermaid-raj-r1 [data-look="neo"].node polygon{stroke:url(#mermaid-raj-r1-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#mermaid-raj-r1 [data-look="neo"].node path{stroke:url(#mermaid-raj-r1-gradient);stroke-width:1px;}#mermaid-raj-r1 [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#mermaid-raj-r1 [data-look="neo"].node .neo-line path{stroke:#A1A1A1;filter:none;}#mermaid-raj-r1 [data-look="neo"].node circle{stroke:url(#mermaid-raj-r1-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#mermaid-raj-r1 [data-look="neo"].node circle .state-start{fill:#000000;}#mermaid-raj-r1 [data-look="neo"].icon-shape .icon{fill:url(#mermaid-raj-r1-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#mermaid-raj-r1 [data-look="neo"].icon-shape .icon-neo path{stroke:url(#mermaid-raj-r1-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#mermaid-raj-r1 :root{--mermaid-font-family:"Anthropic Sans",system-ui,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;}⬡ SalesIntel Pro — Application LayerHTTPSAdminSales RepDownloadmysql-connectormysql-connectormysql-connectormysql-connector🗄 Data Layer — MySQL 8.0usersproductssalesinvoices👤 User BrowserStreamlit Cloud🔐 Auth ModuleFull AccessLimited Access🎛 Sidebar FiltersRegion · City · Date · Rep📊 DashboardKPIs + Charts💳 PaymentsLedger + Invoices📈 ReportsRevenue + Performers🔬 AnalyticsFunnel + Heatmap📄 PDF InvoiceFPDF Generator
<br/>

<br/>
Installation
<br/>
Prerequisites

Python 3.10 or higher
MySQL 8.0 server running locally or remotely
Git

<br/>
1 — Clone the repository
bashgit clone https://github.com/afisaralam07022/salesintelligence07.git
cd salesintelligence07
2 — Create and activate a virtual environment
bash# macOS / Linux
python3 -m venv venv && source venv/bin/activate

# Windows
python -m venv venv && venv\Scripts\activate
3 — Install dependencies
bashpip install -r requirements.txt
4 — Configure your database
bashcp config.example.py config.py
# Open config.py and set your MySQL credentials
python# config.py
DB_HOST     = "localhost"
DB_PORT     = 3306
DB_USER     = "your_mysql_user"
DB_PASSWORD = "your_mysql_password"
DB_NAME     = "salesintel"
5 — Initialize the database
bashmysql -u your_user -p < schema/init.sql
6 — Run the application
bashstreamlit run app.py
The app will open at http://localhost:8501. Default demo credentials:
RoleUsernamePasswordAdminadminadmin123Sales Repsalessales123
<br/>

<br/>
Project Structure
<br/>
salesintelligence07/
│
├── app.py                  # Entry point — routing and session management
├── requirements.txt        # Python dependencies
├── config.py               # DB credentials (gitignored)
│
├── pages/
│   ├── dashboard.py        # KPI cards, revenue trend, pipeline chart
│   ├── payments.py         # Payment ledger, invoice list
│   ├── reports.py          # Monthly revenue, top performers, forecast
│   ├── analytics.py        # Heatmap, funnel, daily trend
│   ├── clients.py          # Client management
│   └── targets.py          # Sales targets and progress
│
├── modules/
│   ├── auth.py             # Login, signup, role management
│   ├── db.py               # MySQL connection and query helpers
│   └── pdf_gen.py          # FPDF invoice generator
│
├── schema/
│   └── init.sql            # Database schema + seed data
│
└── assets/
    └── screenshots/        # README visuals
<br/>

<br/>
Future Roadmap
<br/>
PriorityFeatureStatus🔥 HighEmail notifications for overdue invoicesPlanned🔥 HighREST API layer (FastAPI) for external integrationsPlanned⚡ MediumWhatsApp / Slack alerts for deal stage changesPlanned⚡ MediumCSV + Excel export for all reportsPlanned⚡ MediumForecasting module with Prophet / ARIMAPlanned🌱 LowMulti-tenant SaaS architectureExploring🌱 LowMobile-native app (React Native)Exploring🌱 LowAI-powered deal scoring with scikit-learnExploring
<br/>

<br/>
What I Learned
Building SalesIntel Pro taught me how the full stack actually flows in production — from a user clicking a button all the way down to a SQL query and back. Specific growth areas:

Designing clean relational schemas that survive real-world filtering and joins
Managing Streamlit session state for authentication without page reloads
Making Plotly charts update reactively when sidebar filters change
Writing FPDF layouts that produce professional customer invoices
Structuring a multi-page Streamlit app cleanly for maintainability

Most importantly: I learned that you don't need a team or a budget to ship something real.
<br/>

<br/>
Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.
bash# Fork → Clone → Branch → PR
git checkout -b feature/your-feature-name
git commit -m "feat: add your feature"
git push origin feature/your-feature-name
<br/>

<br/>
Connect
<div align="center">
Afisar Alam — Final-year BCA student · Aspiring Data Analyst
Show Image
 
Show Image
</div>
<br/>

<br/>
<div align="center">
<sub>
SalesIntel Pro  ·  MIT License  ·  2025
Built with ambition, analytics, and engineering precision.
</sub>
</div>
