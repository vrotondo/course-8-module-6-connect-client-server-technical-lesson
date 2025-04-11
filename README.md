# Flask + Frontend Starter Project

## What You'll Learn

- Serve an HTML page using Flask
- Create a Flask API route that returns JSON
- Connect frontend JavaScript to backend Flask using fetch()
- Structure a full-stack project with clear separation between client and server

---

## Project Structure

```
.
├── client/
│   ├── index.html
│   ├── styles.css
│   └── script.js
├── server/
│   ├── app.py
│   ├── store.py
│   └── __init__.py
├── tests/
│   └── test_app.py
├── Pipfile or requirements.txt
└── README.md
```

---

## How to Start

1. Install dependencies:

**Using Pipenv:**
```bash
pipenv install
pipenv shell
```

**Using pip and venv:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Run the server:
```bash
python server/app.py
```

3. Open your browser and go to:
```
http://localhost:5000/
```

---

## Your Task

- Complete the backend route in `app.py` to serve the `index.html` file.
- Add a second route that returns JSON data at `/api/data`.
- Use `store.py` to generate the data.
- Make the frontend (in `script.js`) fetch data from the backend.
- Run `pytest` and pass all the tests in `test_app.py`.

---

Good luck!
