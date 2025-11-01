# 🎵 Synced Lyrics Backend API

> A premium FastAPI-powered backend service that delivers high-quality **time-synced (LRC)** and **plain-text lyrics** for your music app — built for speed, precision, and seamless Flutter integration.

![FastAPI](https://img.shields.io/badge/FastAPI-0.120.4-009688?logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![SyncedLyrics](https://img.shields.io/badge/Powered%20by-SyncedLyrics-orange)
![Render](https://img.shields.io/badge/Deploy%20to-Render-46E3B7?logo=render&logoColor=white)

---

## 🚀 Overview

The **Synced Lyrics Backend** is a modern, scalable, and minimal REST API built using **FastAPI**.  
It fetches **synchronized (LRC)** and **plain lyrics** from multiple sources, ensuring your app always delivers the best lyric experience — no matter the artist, track, or language.

Designed to power **music players, lyric visualizers, or karaoke-style apps**, this backend makes it effortless to integrate synced lyrics into your product.

---

## ✨ Features

✅ Fetches synced LRC lyrics with accurate timestamps  
✅ Automatically falls back to plain text when LRC isn’t available  
✅ Integrates seamlessly with **Flutter**, **React**, or **mobile music players**  
✅ Multi-source lyric fetching (Musixmatch, NetEase, Genius, etc.)  
✅ Optimized for speed using **FastAPI + Uvicorn**  
✅ Easy one-click deployment on **Render**  
✅ Detailed logging for API requests & responses  

---

## 🧱 Project Structure

```
app/
├── api/
│   └── routes_lyrics.py       # API endpoints
├── core/
│   └── logger.py              # Logging configuration
├── services/
│   └── lyrics_service.py      # Lyrics fetch logic
├── utils/
│   └── __init__.py
└── main.py                    # FastAPI app entry point
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/SanjuScript/lyric_backend.git
cd lyric_backend
```

### 2️⃣ Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Server Locally

Start the API server:

```bash
uvicorn app.main:app --reload
```

Now open your browser and navigate to:

```
http://127.0.0.1:8000
```

Check the interactive Swagger docs here:
```
http://127.0.0.1:8000/docs
```

---

## 🌐 Example API Request

### **Request**
```bash
GET /lyrics?query=Shape%20of%20You%20Ed%20Sheeran
```

### **Response**
```json
{
  "query": "Shape of You Ed Sheeran",
  "lyrics": "[00:12.45] The club isn't the best place to find a lover..."
}
```

> Returns synced lyrics (if available), else plain text.

---

## ☁️ Deploying to Render (Free Hosting)

You can deploy this API to [Render](https://render.com) easily.

### Steps:
1. Push your project to GitHub (already done ✅).  
2. Go to [Render → Web Services](https://render.com/).  
3. Click **“New Web Service”** and connect your GitHub repo.  
4. Use the following settings:
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn app.main:app --host 0.0.0.0 --port 10000`
   - **Region:** Closest to your users
5. Click **Deploy** 🚀

After deployment, you’ll get a public URL like:
```
https://lyric-backend.onrender.com
```

---

## 🧩 Flutter Integration Example

```dart
final String baseUrl = "https://lyric-backend.onrender.com";

Future<String?> fetchLyrics(String artist, String title) async {
  final query = Uri.encodeComponent("$title $artist");
  final url = Uri.parse("$baseUrl/lyrics?query=$query");

  final response = await http.get(url);

  if (response.statusCode == 200) {
    final data = jsonDecode(response.body);
    return data["lyrics"] as String?;
  } else {
    return null;
  }
}
```

---

## 🧠 Powered By

- ⚡ [FastAPI](https://fastapi.tiangolo.com/)
- 🎧 [SyncedLyrics](https://github.com/moehmeni/syncedlyrics)
- 🌍 [Render Cloud Hosting](https://render.com/)
- 🧩 [Uvicorn ASGI Server](https://www.uvicorn.org/)

---

## 🛠️ Requirements

- Python **3.10+**
- `uvicorn`, `fastapi`, and `syncedlyrics`
- Internet connection (for lyric providers)
- GitHub account (for deployment)

---

## 📦 Dependencies

All dependencies are managed in [`requirements.txt`](./requirements.txt):

```txt
fastapi==0.120.4
uvicorn==0.38.0
syncedlyrics==1.0.1
requests==2.32.5
beautifulsoup4==4.14.2
pydantic==2.12.3
python-dotenv==1.2.1
```
---

## 🧾 License

This project is licensed under the **MIT License** — you’re free to use, modify, and distribute it for both personal and commercial projects.

---

## 👨‍💻 Author

**Sanjay N P**  
📧 dev.sanju.codes@gmail.com  
🌐 [GitHub: SanjuScript](https://github.com/SanjuScript)

> “Built with ❤️ using FastAPI, SyncedLyrics, and a deep love for music.”

---

## 🧩 Optional — Render Deployment Config

If you want auto-deploys on push, create a `render.yaml` file in the root:

```yaml
services:
  - type: web
    name: synced-lyrics-api
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn app.main:app --host 0.0.0.0 --port 10000
    autoDeploy: true
```

---

⭐ **If you like this project, give it a star on GitHub to show your support!**
