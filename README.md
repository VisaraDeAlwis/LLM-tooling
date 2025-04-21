## 🌍 City Companion – Weather & Fuel Station Finder 🔧

A lightweight LLM tool integration that provides real-time **weather updates** and **fuel station details** based on a city name. This is part of an experimental project to enhance LLM capabilities with external tools (APIs).

---

### 🚀 Features
- 🌤️ Get **current temperature and weather conditions** for any city
- ⛽ Find **fuel stations near a selected city**, with:
  - Station name
  - Address
  - Google rating
- 🌐 Powered by:
  - **OpenWeather API** (for weather)
  - **Google Maps Platform APIs** (Geocoding + Places API)
- 🧠 Built for **LLM tooling and RAG applications**

---

### 📦 Folder Structure
```
.
├── main.py                  # Entry point script
├── temperature.py           # Weather fetch logic
├── location.py              # Fuel station logic (geocoding + nearby search)
├── .env                     # API keys stored securely here
└── README.md
```

---

### 🔧 Setup & Run

#### 1. 🔐 Get Your API Keys:
- **OpenWeatherMap API** → [openweathermap.org](https://openweathermap.org/)
- **Google Maps API** → [console.cloud.google.com](https://console.cloud.google.com/)

#### 2. 📄 Create `.env` File:
```env
API_KEY_TEMP=your_openweather_api_key
API_KEY_LOCATION=your_google_maps_api_key
```

#### 3. ▶️ Run the Script:
```bash
python main.py
```

---

### 📦 Dependencies
Install required packages using:

```bash
pip install requests python-dotenv
```

---

### 🧠 LLM Use Case
This project is designed to be integrated with an LLM-based assistant that:
- Receives a user prompt like:  
  _"How’s the weather in Colombo and are there fuel stations nearby?"_
- Dynamically triggers this tool to return accurate and formatted data
- Combines data with LLM outputs in a conversational way

---

### 📜 License
MIT License

---

### ✨ Author
Crafted with ⚙️ by Visara De Alwis – aspiring AI/ML engineer & LLM tool builder  
🔗 www.linkedin.com/in/visara-de-alwis 

