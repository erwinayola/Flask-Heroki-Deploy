from flask import Flask, jsonify, request, render_template
import random

app = Flask(__name__)

# Pesan-pesan default Puja Kerang Ajaib
default_messages = [
    "Makan patty itu spongebob",
    "Berdansalah, Patrick",
    "Ayo ke rumah Sandy",
    "Jangan lupa beli Krabby Patty",
    "Squidward, kapan kau senang?",
    "Plankton selalu mencuri resep rahasia Krabby Patty",
    "Gary, jangan lupa makan malam",
    "Mr. Krabs suka uang",
    "Spongebob adalah karyawan terbaik di Krusty Krab",
    "Bikini Bottom adalah tempat yang menyenangkan"
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nama_post = request.form.get('nama')
        if nama_post:
            welcome_message = f"Selamat datang, {nama_post}, anda berhasil masuk ke Puja Kerang Ajaib"
            random_message = f"{nama_post}, {random.choice(default_messages)}"
            return render_template('kerangajaib.html', welcome_message=welcome_message, random_message=random_message)

    return render_template('kerangajaib.html', welcome_message=None, random_message=None)

if __name__ == '__main__':
    app.run(debug=True)
