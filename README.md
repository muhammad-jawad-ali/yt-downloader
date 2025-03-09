# 🎥 YouTube Video Downloader

A simple YouTube video downloader built with `yt-dlp` and Flask. This tool allows users to download YouTube videos in MP4 format easily.

## 🚀 Features
- Download YouTube videos in MP4 format
- Simple web interface for non-technical users
- Lightweight and easy to deploy
- Free and open-source

## 📦 Requirements
Ensure you have the following installed:
- Python 3.8+
- `pip` (Python package manager)

## 🔧 Installation & Setup
1. **Clone the repository**
   ```sh
   git clone https://github.com/yourusername/yt-downloader.git
   cd yt-downloader
   ```

2. **Create a virtual environment** (Recommended)
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

## 🚀 Running the Application
```sh
python app.py
```
The server will start, and you can access it in your browser at:
```
http://127.0.0.1:5000
```

## 🌍 Deploying Online (For Free)
You can deploy your application using:
- **Render** (Free hosting for Flask apps)
- **Railway** (Free tier for Python apps)
- **Replit** (Run Python apps online)
- **GitHub Pages + Flask API with Backend**

## 🛠 Troubleshooting
- If `yt-dlp` fails to download videos, update it:
  ```sh
  yt-dlp -U
  ```
- If port `5000` is busy, use another port:
  ```sh
  python app.py --port 8080
  ```

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).

## 💡 Contributing
Pull requests are welcome! If you want to improve this project, follow these steps:
1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Make your changes and commit (`git commit -m "Your message"`)
4. Push to your branch (`git push origin feature-name`)
5. Open a Pull Request

## 🤝 Credits
Developed by [Muhammad Jawad Ali](https://github.com/muhammad-jawad-ali)
