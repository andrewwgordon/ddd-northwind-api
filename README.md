# Domain-Driven Design CQRS Microservice OpenAPI Demo
## Overview
This project is an example [Domain-Driven Design](https://martinfowler.com/bliki/DomainDrivenDesign.html) [Microservice](https://microservices.io/index.html) supporting [OpenAPI](https://www.openapis.org/). The purpose of the project is an education "toy" application to articulate DDD and Microservice best practices.
## Quick Start

### Prequisites
Python >= 3.7
### Install
Clone this repo.
```bash
git clone https://github.com/andrewwgordon/ddd-northwind-api.git
```
Create a Python virtual environment and activate it.
```bash
python -m venv venv
.\venv\Scripts\activate (Windows)
./venv/bin/activate (Linux)
```
Install dependencies
```bash
python -m pip install -r requirements.txt
```
### Deploy the Northwind SQLite Database
Download the [SQLite3 Northwind database](https://github.com/jpwhite3/northwind-SQLite3/blob/master/Northwind_large.sqlite.zip), unpack the archive and deploy to ./northwind/resources/database/Northwind.sqlite.
### Configure Logging
Note: You also may need to create a ./log/ directory in the root of the application directory. Logging path can be configured in ./northwind/resources/logging.conf.
### Run the Test Suite
```bash
python -m pytest -s -v
```
Note: The current e2e REST API test spins up a Flask App instance as a OS sub process. It attempts to terminate it on test completion, but you may need to kill the process.
### Start the Service
Start the service
```bash
python app.py
```


Navigate to the Swagger UI via your browser
```bash
http://localhost:8098/v1/ui
```
Note: The default port for the HTTP Server is 8098. You can change this setting in the northwind.properties file in ./northwind/resources/.
