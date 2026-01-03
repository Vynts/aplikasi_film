import os
from flask import Flask, request, redirect, render_template, url_for, session
import mysql.connector
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash, generate_password_hash

HOST = "localhost"
USER = "root"
PASS = ""
DB = "python_film"

def connect():
    return mysql.connector.connect(
        host = HOST,
        user = USER,
        password = PASS,
        database = DB,
    )


filepath_images = '/home/erza/belajar_python/app_film/static/images'
filepath_videos = '/home/erza/belajar_python/app_film/static/videos'

app = Flask(__name__)
app.secret_key = "yasukasukasaya"
app.config['UPLOAD_IMAGES'] = filepath_images
app.config['UPLOAD_VIDEOS'] = filepath_videos

@app.context_processor
def inject_genres():
    conn = connect()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM genre")
    genre = cursor.fetchall()

    cursor.close()
    conn.close()
    return dict(genre=genre)

@app.route("/")
def beranda():
    conn = connect()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM film ORDER BY idfilm DESC LIMIT 6")
    data = cursor.fetchall()

    cursor.execute("SELECT * FROM film ORDER BY total_penonton DESC LIMIT 8")
    populer = cursor.fetchall()

    cursor.close()
    conn.close()
    return render_template("film/beranda.html", data=data, populer=populer)

@app.route("/movies")
def movies():
    conn = connect()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM film ORDER BY idfilm DESC")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("film/movie.html", data=data)

@app.route("/detail/<int:id>", methods=["GET","POST"])
def detail(id):
    if request.method == "POST":
        nama = request.form["nama"]
        komentar = request.form["komentar"]

        conn = connect()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO komentar (idfilm, nama, komentar) VALUES (%s, %s, %s)", (id, nama, komentar))
        conn.commit()

        conn.close()
        cursor.close()
 
    conn = connect()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("UPDATE film SET total_penonton= total_penonton + 1 WHERE idfilm=%s", (id,))
    conn.commit()

    cursor.execute("SELECT a.*,c.idfilm FROM komentar a JOIN film c ON c.idfilm=a.idfilm WHERE c.idfilm=%s", (id,))
    komentar = cursor.fetchall()

    cursor.execute("SELECT a.*, b.tipegenre FROM film a JOIN genre b ON a.idgenre=b.idgenre WHERE idfilm=%s", (id,))
    data = cursor.fetchone()

    cursor.execute("SELECT * FROM film WHERE idgenre=%s", (data['idgenre'],))
    film = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("film/detail.html", data=data, film=film, komentar=komentar)

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        user = request.form["user"]
        password = request.form["password"]

        conn = connect()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM user WHERE username=%s", (user,))
        users = cursor.fetchone()

        if users and check_password_hash(users['password'], password):
            session['logged_in'] = True
            session['iduser'] = users['iduser']
            session['username'] = users['username']
            session['role'] = users['role']
            return redirect(url_for("dashboard"))
        
    return render_template("film/login.html")

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        user = request.form['user']
        username = request.form['username']
        password = request.form['password']

        password_hashed = generate_password_hash(password)

        if user:
            conn = connect()
            cursor = conn.cursor()

            cursor.execute("INSERT INTO user (user, username, password) VALUES (%s, %s, %s)", (user, username, password_hashed))
            conn.commit()

            cursor.close()
            conn.close()
            return redirect(url_for('login'))

    return render_template("film/register.html")

@app.route("/logout")
def logout():
    session.clear()

    return redirect(url_for("login"))

@app.route("/dashboard")
def dashboard():
    role = session.get('role')

    if not session.get('logged_in') or role != "admin":
        return redirect(url_for('login'))
    
    elif role == "user" :
        return redirect(url_for('beranda'))

    return render_template("template/dashboard.html")

@app.route("/genres/<nama>")
def genres(nama):

    conn = connect()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM genre WHERE cur=%s", (nama,))
    judul = cursor.fetchone()

    cursor.execute("SELECT a.*,b.* FROM film a JOIN genre b ON a.idgenre=b.idgenre WHERE b.tipegenre=%s", (nama,))
    data = cursor.fetchall()

    conn.close()
    cursor.close()
    
    return render_template("film/genres.html", judul=judul, data=data)

@app.route("/genre/<path:action>", methods=["GET","POST"])
def genre(action) :
    if not session["loggedin"] == True and not session["admin"] == True:
        return redirect(url_for("login"))
    
    # menampilkan data
    if action == "tampil":
        conn = connect()
        conn = connect()
        cursor = conn.cursor(dictionary=True)

        page = request.args.get('page', 1, type=int)
        per_page = 5

        offset = (page - 1 ) * per_page
        
        cursor.execute("SELECT COUNT(*) AS total FROM genre")
        total_data = cursor.fetchone()['total']

        total_page = (total_data + per_page - 1) // per_page

        search = request.args.get('search')
        search_pattern = f"%{search}%"

        cursor.execute("SELECT * FROM genre LIMIT %s OFFSET %s", (per_page, offset))
        data = cursor.fetchall()

        if search:
            cursor.execute("SELECT * FROM genre WHERE tipegenre LIKE %s", (search_pattern,))
            data = cursor.fetchall()

        conn.close()
        cursor.close()

        return render_template("admin/data_genre.html", data=data, page=page, total_page=total_page,  per_page=per_page)
    if action == "tambah":
        if request.method == "POST":
            genre = request.form["genre"]
            cur = genre.lower()

            conn = connect()
            cursor = conn.cursor()

            cursor.execute("INSERT INTO genre (tipegenre, cur) VALUES (%s, %s)", (genre, cur))
            conn.commit()

            conn.close()
            cursor.close()

            return redirect(url_for("genre", action="tampil"))
    if action == "edit":
        conn = connect()
        cursor = conn.cursor(dictionary=True)

        id = request.args.get("id")

        if request.method == "POST":
            genre = request.form["genre"]
            cur = genre.lower()

            if id:
                cursor.execute("UPDATE genre SET tipegenre=%s, cur=%s WHERE idgenre=%s", (genre, cur, id))
                conn.commit()

        cursor.execute("SELECT * FROM genre WHERE idgenre=%s", (id,))
        data = cursor.fetchone()

        conn.close()
        cursor.close()

        return render_template("admin/edit_genre.html", data=data)

    if action == "hapus": 
        id = request.args.get('id')
        conn = connect()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM film WHERE idgenre=%s", (id,))
        cursor.execute("DELETE FROM genre WHERE idgenre=%s", (id,))
        conn.commit()

        conn.close()
        cursor.close()

        return redirect(url_for("genre", action="tampil"))
    
@app.route("/film/<path:action>", methods=["GET", "POST"])
def film(action):
    if not session["loggedin"] == True and not session["admin"] == True:
        return redirect(url_for("login"))
    
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    if action == "tampil":

        page = request.args.get('page', 1, type=int)
        per_page = 3

        offset = (page - 1) * per_page

        cursor.execute("SELECT COUNT(*) as total FROM film ")
        total_data = cursor.fetchone()['total']

        total_page = (per_page + total_data - 1) // per_page

        search = request.args.get('search')
        search_pattern = f"%{search}%"

        cursor.execute("SELECT * FROM film ORDER BY idfilm DESC LIMIT %s OFFSET %s", (per_page, offset))
        data = cursor.fetchall()

        if search:
            cursor.execute("SELECT * FROM film WHERE namafilm LIKE %s", (search_pattern,))
            data = cursor.fetchall()

        conn.close()
        cursor.close()

        return render_template("admin/data_film.html", data=data, total_page=total_page, page=page, per_page=per_page)
    if action == "tambah":
        if request.method == "POST":
            idgenre = request.form["idgenre"]
            namafilm = request.form["namafilm"]
            deskirpsi = request.form["deskripsi"]
            tahunrilis = request.form["tahunrilis"]
            poster = request.files["poster"]
            videofilm = request.files["videofilm"]
            filmtype = request.form["filmtype"]
            sutradara = request.form["sutradara"]
            artis = request.form["artis"]

            filename_videos = None
            filename_images = None

            if poster:
                filename_images = secure_filename(poster.filename)
                file_save_path = os.path.join(app.config['UPLOAD_IMAGES'], filename_images)
                poster.save(file_save_path)

            if videofilm:
                filename_videos = secure_filename(videofilm.filename)
                file_save_path = os.path.join(app.config['UPLOAD_VIDEOS'], filename_videos)
                videofilm.save(file_save_path)

        cursor.execute("INSERT INTO film (idgenre, namafilm, deskripsi, tahunrilis, posterfilm, videofilm, filmtype, sutradara, artis) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (idgenre, namafilm, deskirpsi, tahunrilis, filename_images, filename_videos, filmtype, sutradara, artis))
        conn.commit()

        cursor.close()
        conn.close()

        return redirect(url_for("film", action="tampil"))
    if action == "edit":
        conn = connect()
        cursor = conn.cursor(dictionary=True)
        id = request.args.get('id')

        if request.method == "POST":
            idgenre = request.form["idgenre"]
            namafilm = request.form["namafilm"]
            deskirpsi = request.form["deskripsi"]
            tahunrilis = request.form["tahunrilis"]
            poster = request.files["poster"]
            videofilm = request.files["videofilm"]
            filmtype = request.form["filmtype"]
            sutradara = request.form["sutradara"]
            artis = request.form["artis"]
            filename_images = None
            filename_videos = None

            if poster:
                filename_images = secure_filename(poster.filename)
                file_save_path = os.path.join(app.config['UPLOAD_IMAGES'], filename_images)
                poster.save(file_save_path)

            if videofilm:
                filename_videos = secure_filename(videofilm.filename)
                file_save_path = os.path.join(app.config['UPLOAD_VIDEOS'], filename_videos)
                videofilm.save(file_save_path)

            if id:
                cursor.execute("UPDATE film SET idgenre=%s, namafilm=%s, deskripsi=%s, tahunrilis=%s, posterfilm=%s, videofilm=%s, filmtype=%s, sutradara=%s, artis=%s WHERE idfilm=%s", (idgenre, namafilm, deskirpsi, tahunrilis, filename_images, filename_videos, filmtype, sutradara, artis, id))
                conn.commit()

                conn.close()
                cursor.close()

                return redirect(url_for("film", action="tampil"))

        cursor.execute("SELECT * FROM film WHERE idfilm=%s", (id,))
        data = cursor.fetchone()

        conn.close()
        cursor.close()
        return render_template("admin/edit_film.html", data=data)
    if action == "hapus":
        id = request.args.get('id')

        conn = connect()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("DELETE FROM komentar WHERE idfilm=%s", (id,))
        cursor.execute("DELETE FROM film WHERE idfilm=%s", (id,))
        conn.commit()

        cursor.close()
        conn.close()

        return redirect(url_for("film", action="tampil"))

@app.route("/komentar/<path:action>", methods=["POST","GET"])
def komentar(action):
    if not session["loggedin"] and not session["role"] == "admin":
        return redirect(url_for("login"))
    
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    if action == "tampil":
        page = request.args.get('page', 1, type=int)
        per_page = 5

        offset = (page - 1) * per_page

        cursor.execute("SELECT COUNT(*) AS total FROM komentar")
        total_data = cursor.fetchone()['total']

        total_page = (total_data + per_page - 1) // per_page 

        search = request.args.get('search')
        search_pattern = f"%{search}%"

        cursor.execute("SELECT a.*, b.namafilm, b.posterfilm FROM komentar a JOIN film b ON a.idfilm=b.idfilm LIMIT %s OFFSET %s", (per_page, offset))
        data = cursor.fetchall() 

        if search:
            cursor.execute("SELECT a.*, b.namafilm, b.posterfilm FROM komentar a JOIN film b ON a.idfilm=b.idfilm WHERE komentar LIKE %s", (search_pattern,))
            data = cursor.fetchall()
        
        cursor.close()
        conn.close()

        return render_template("admin/data_komentar.html", data=data, per_page=per_page, page=page, total_page=total_page)
    if action == "edit":
        id = request.args.get('id')

        if request.method == "POST":
            nama = request.form["nama"]
            komentar = request.form["komentar"]

            if id:
                cursor.execute("UPDATE komentar SET nama=%s, komentar=%s WHERE idkomentar=%s", (nama, komentar, id))
                conn.commit()

                return redirect(url_for("komentar", action="tampil"))

        cursor.execute("SELECT a.*, b.namafilm FROM komentar a JOIN film b ON a.idfilm=b.idfilm WHERE idkomentar=%s", (id,))
        data = cursor.fetchone()

        cursor.close()
        conn.close()

        return render_template("admin/edit_komentar.html", data=data)
    if action == "hapus":
        id = request.args.get('id')

        cursor.execute("DELETE FROM komentar WHERE idkomentar=%s", (id,))
        conn.commit()

        return redirect(url_for("komentar", action="tampil"))

if __name__ == "__main__":
    app.run(debug=True)
