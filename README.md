# HNG Submission Flask Cat Fact API

A simple Flask API that fetches random cat facts from [CatFact Ninja](https://catfact.ninja/fact) and returns them in JSON format with user info and timestamp.

---

## ⚙️ How It Works

- The `/me` endpoint sends a GET request to an external API.  
- It retrieves a random cat fact, adds your info and a UTC timestamp, and returns JSON.  
- Includes error handling for timeout, connection, and HTTP errors.  
- CORS is enabled for cross-origin requests.

---

## 🧩 Setup

### 1. Clone the repo
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```
### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Run the app locally
```bash
python app.py
```
