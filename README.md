# 🏥 Pharma AI Requirements Monitor (Pharma AI Requirements Monitor)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)

A smart platform for tracking and analyzing pharma companies' AI requirements, collecting public project needs and providing data-driven job recommendations.

## ✨ Key features

- Intelligent monitoring of open AI requirements across platforms (GitHub, job boards)
- Smart categorization and trend analysis
- Data visualization dashboards and statistical reports
- Job recommendations based on AI skills and project fit
- Docker support for easy deployment

## Quickstart

Requirements:
- Python 3.8+
- Flask 2.0+

Install:
```bash
pip install -r requirements.txt
```

Run (standalone):
```bash
python standalone_server.py
```

Docker:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "standalone_server.py"]
```

## API endpoints

- `GET /api/requirements` - fetch requirements list
- `GET /api/stats` - fetch statistics
- `GET /api/jobs` - fetch job recommendations
- `GET /api/scheduler/status` - fetch scheduler status

## Contributing
Please read `CONTRIBUTING.md` for contribution guidelines.
