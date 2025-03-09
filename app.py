from flask import Flask, render_template, request, send_file
import os
import yt_dlp

download_folder = "downloads"
os.makedirs(download_folder, exist_ok=True)  # Ensure folder exists

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form.get('url')
    if not url:
        return "Error: No URL provided", 400
    
    try:
        ydl_opts = {
            'format': 'mp4',
            'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s')
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
        return send_file(filename, as_attachment=True)
    except Exception as e:
        return f"Error: {e}", 500

if __name__ == "__main__":
    app.run(debug=True)
