Automated Unix/Linux CLI Data Pipeline (ETL)

A lightweight, automated ETL (Extract, Transform, Load) data pipeline executed in a Unix/Linux terminal environment (Bash). The pipeline orchestrates environment setup, containerized database provisioning via Docker, automated data fetching, Python-based data cleaning, and automated loading into an MS SQL Server database.

🛠️ Tech Stack & Concepts

Environment & Automation: Unix/Linux CLI, Bash scripting

Containerization: Docker, Docker Compose

Data Processing & ETL: Python 3, Pandas, SQLAlchemy

Database: Microsoft SQL Server 2022

Data Source: World Bank GDP Public Data (CSV via curl)

⚙️ Architecture & Pipeline Flow

The entire workflow is automated via a single shell script (run_pipeline.sh):

Directories Setup: Ensures project structure (./data directory).

Infrastructure Provisioning: Launches an MS SQL Server 2022 instance in a detached Docker container (docker compose up -d).

Automated Extraction: Downloads raw GDP economic dataset directly using Unix curl.

Data Transformation & Loading: Executes load_data.py:

Normalizes column names (lowercase, underscore spaces).

Handles missing records (dropna).

Loads cleaned records into the target database table stg_ecommerce_events via SQLAlchemy.

System Metrics Verification: Inspects downloaded raw payload size and row counts using Unix system commands (wc -l).

🚀 Getting Started

Prerequisites

Docker Desktop installed and running.

Git Bash (on Windows) or any Linux/Unix Terminal.

Python 3.x installed locally.

Installation & Execution

Clone the repository:

git clone https://github.com/Jaimardio/Automated-Unix.git
cd Automated-Unix


Install required Python packages:

pip install -r requirements.txt


Grant execution permissions to the script (Unix CLI):

chmod +x run_pipeline.sh


Run the pipeline:

./run_pipeline.sh


📊 Database Verification

You can connect to the running database instance using SQL Server Management Studio (SSMS) or Azure Data Studio:

Host: localhost,1433

User: sa

Password: YourStrongPassword123!

Sample Query:

SELECT TOP 10 * 
FROM stg_ecommerce_events;
