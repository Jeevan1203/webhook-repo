# 📊 GitHub Events Dashboard

A real-time dashboard that captures and displays GitHub repository events (Push, Pull Request, Merge) using webhooks, Flask, MongoDB, and a clean modern UI.

> ✅ Submitted for TechStaX Developer Assessment

---

## 🚀 Features

- 🔗 GitHub Webhook integration
- 🧠 Captures Push, Pull Request, and Merge events
- 💾 MongoDB Atlas for event storage
- 🌗 Persistent Dark/Light theme toggle
- 🎛️ Event type filters (Push, PR, Merge)
- 📊 Summary stats with live count
- 📥 Download events as `.json`
- 📱 Responsive design
- 📣 Toast notifications for new events
- ⚠️ Custom 404 error handling

---

## 🖼️ Preview


[image](https://github.com/user-attachments/assets/c21f0f45-b3c7-48af-8ccb-2dd67f9dab41)


---

## 🛠️ Tech Stack

| Layer     | Tools Used                         |
|-----------|------------------------------------|
| Backend   | Python, Flask, Flask-CORS          |
| Database  | MongoDB Atlas (`pymongo`)          |
| Frontend  | HTML, CSS, JavaScript              |
| UI Icons  | Font Awesome                       |
| Dev Tools | GitHub Webhooks, ngrok             |

---

## 📂 Project Structure

```bash
webhook-repo/
├── assignement/
│   ├── app.py           # Flask app entry point
│   ├── routes.py        # Webhook + events API
│   ├── models.py        # MongoDB connection
│   ├── utils.py         # GitHub event parsing logic
│   └── frontend/
│       └── index.html   # Dashboard UI
├── requirements.txt     # Python dependencies
└── README.md            # You're here ✅
