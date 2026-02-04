from flask import Flask, redirect, url_for
import threading
import time

app = Flask(__name__)

sayac = 0
LOCK = threading.Lock()

@app.route("/")
def index():
    return f"""
    <h1>Sayac: {sayac}</h1>

    <form action="/arttir" method="post">
        <button style="font-size:20px;">+1</button>
    </form>

    <p>Bot her 500 ms'de bir otomatik arttırır 🤖</p>
    """

@app.route("/arttir", methods=["POST"])
def arttir():
    global sayac
    with LOCK:
        sayac += 1
    return redirect(url_for("index"))

def bot():
    global sayac
    while True:
        time.sleep(0.5)  # 500 ms
        with LOCK:
            sayac += 1
        print("Bot tıkladı:", sayac)

# Botu arka planda başlat
threading.Thread(target=bot, daemon=True).start()

# Replit için gerekli ayar
app.run(host="0.0.0.0", port=8080)