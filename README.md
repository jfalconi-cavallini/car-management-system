# Car Management System

[Live Demo](https://web-production-7bd52.up.railway.app)

---

## Project Overview

This **Car Management System** is a full-stack web application built with **Flask** and **Python** that automatically scrapes live car inventory data from the Clay Cooley dealership website and updates a local database every 24 hours. The system offers an intuitive web interface to search, add, edit, and delete car listings, providing real-time access to current vehicle inventory.

---

## Key Features

- **Automated Web Scraping:**  
  Utilizes `requests` and `BeautifulSoup` to scrape detailed car inventory data, including make, model, year, price, mileage, VIN, images, and listing links directly from [Clay Cooley](https://www.claycooley.com).

- **Scheduled Data Updates:**  
  Implements `APScheduler` to run the scraper every 24 hours, ensuring the local database remains synchronized with the live dealership inventory without manual intervention.

- **Robust Database Management:**  
  Uses `Flask-SQLAlchemy` with SQLite to store and manage car data efficiently, including duplicate detection via VIN numbers and other attributes.

- **User-Friendly Web Interface:**

  - Search cars by make, model, or availability status.
  - Add, edit, and delete car listings with ease.
  - View detailed listings with images and external links to the original dealer pages.

- **Deployment Ready:**  
  Hosted on Railway.app with `gunicorn` as the WSGI server, ensuring production-level reliability and scalability.

---

## Technologies Used

- **Backend:** Python, Flask, Flask-SQLAlchemy, APScheduler
- **Web Scraping:** requests, BeautifulSoup (bs4)
- **Database:** SQLite
- **Frontend:** Jinja2 templating, Bootstrap 5
- **Deployment:** Railway.app, Gunicorn

---

---

## How It Works

1. **Scraping:** The scraper fetches car inventory pages, parses relevant details, and compiles the data as JSON.

2. **Data Storage:** The Flask app reads scraped data and updates the database, avoiding duplicates by checking VIN or car attributes.

3. **Scheduling:** Using APScheduler, the scraping job is triggered automatically every 24 hours to keep the inventory current.

4. **User Interaction:** Users interact via the web UI to browse, search, and manage car listings.

---

## Setup & Installation

# To run locally:

git clone https://github.com/yourusername/car-management-system.git
cd car-management-system

# Create and activate a virtual environment

python3 -m venv venv
source venv/bin/activate # Windows: venv\Scripts\activate

# Install dependencies

pip install -r requirements.txt

# Run the app

python3 app.py

## Why This Project?

This project demonstrates my ability to:

- Build full-stack applications with real-world data integration
- Implement reliable scheduling and automation
- Work with databases and ORM to manage data integrity
- Deploy production-ready applications on cloud platforms
- Write clean, modular, and maintainable Python code

---

## Live Demo

Try the live version here:  
[https://web-production-7bd52.up.railway.app](https://web-production-7bd52.up.railway.app)

---

## Future Enhancements

- Add user authentication and role-based access
- Improve scraper resilience with retry and error handling
- Add advanced filtering and sorting options
- Use a more scalable database for larger datasets
- Implement REST API endpoints for integration with other systems

Email: jkfc87@gmail.com
LinkedIn: https://www.linkedin.com/in/jose-falconi-cavallini/
Github: github.com/jfalconi-cavallini
