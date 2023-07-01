from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3

app = Flask(__name__)
#koneksi
app.secret_key = 'bebasapasaja'
app.config['MYSQL_HOST'] ='localhost'
app.config['MYSQL_USER'] ='root'
app.config['MYSQL_PASSWORD'] =''
app.config['MYSQL_DB'] ='login'
mysql = MySQL(app)

#INDEX
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/informasi')
def informasi():
    return render_template('pengumuman.html')

@app.route('/contact')
def contact():
    return render_template('Pembuat.html')

#LOGIN
@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        # email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        session['user'] = username
        #cek data username
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM computer WHERE username=%s',(username, ))
        akun = cursor.fetchone()
        if akun is None:
            flash('Login Gagal, Cek Username Anda','danger')
        elif not check_password_hash(akun[4], password):
        #elif not akun[4] == password:
            flash('Login gagal, Cek Password Anda', 'danger')
        else:
            session['loggedin'] = True
            session['username'] = akun[3]
            session['level'] = akun[5]
            # return redirect(url_for('dashboard'))
            if session['level'] == 'Admin':
                return redirect(url_for('dashboard'))
            elif session['level'] == 'Dosen':
                return redirect(url_for('dashboard_dosen'))
            elif session['level'] == 'Mahasiswa':
                return redirect(url_for('dashboard_mahasiswa'))
            else:
                flash('Login gagal, Cek Username/Password Anda', 'danger')
    return render_template('login.html')

#DASHBOARD ADMIN
@app.route('/dashboard')
def dashboard():
    if 'loggedin' in session:
        cur = mysql.connection.cursor()
        cur.execute('SELECT count(*) FROM computer WHERE level="Dosen"')
        rv = cur.fetchone()
        cur.close()
        cur2 = mysql.connection.cursor()
        cur2.execute('SELECT count(*) FROM computer WHERE level="Mahasiswa"')
        rv2 = cur2.fetchone()
        cur2.close()
        cur3 = mysql.connection.cursor()
        cur3.execute('SELECT count(*) FROM matakuliah')
        rv3 = cur3.fetchone()
        cur3.close()
        values = [
            rv[0], rv2[0]]
        colors = [
            "#F7464A", "#46BFBD"]
        labels = [
            'Dosen', 'Mahasiswa']
        pie_labels = labels
        pie_values = values
        bar_labels=labels
        bar_values=values
        return render_template('admindahsboard3.html', dosen=rv,mhs=rv2, matkul=rv3, max=50, set=zip(values, labels, colors),labels=bar_labels, values=bar_values)
    flash('Harap Login dulu','danger')
    return redirect(url_for('login'))

#DASHBOARD DOSEN
@app.route('/dashboard-dosen')
def dashboard_dosen():
    if 'loggedin' in session:
        return render_template('dosendashboard.html')
    flash('Harap Login dulu','danger')
    return redirect(url_for('login'))

#DASHBOARD MAHASISWA
@app.route('/dashboard-mahasiswa')
def dashboard_mahasiswa():
    if 'loggedin' in session:
        data = session.get('user')
        cur = mysql.connection.cursor()
        cur.execute('SELECT nama FROM computer WHERE username=%s',(data,))
        rv = cur.fetchone()
        session['mhs'] = rv[0]
        cur.close()
        cur2 = mysql.connection.cursor()
        cur2.execute('SELECT count(*) FROM penilaian WHERE mahasiswa=%s AND hasil="A"',(rv[0],))
        rv2 = cur2.fetchone()
        cur2.close()
        cur3 = mysql.connection.cursor()
        cur3.execute('SELECT count(*) FROM penilaian WHERE mahasiswa=%s AND hasil="A-"',(rv[0],))
        rv3 = cur3.fetchone()
        cur3.close()
        cur4 = mysql.connection.cursor()
        cur4.execute('SELECT count(*) FROM penilaian WHERE mahasiswa=%s AND hasil="AB"',(rv[0],))
        rv4 = cur4.fetchone()
        cur4.close()
        cur5 = mysql.connection.cursor()
        cur5.execute('SELECT count(*) FROM penilaian WHERE mahasiswa=%s AND hasil="B+"',(rv[0],))
        rv5 = cur5.fetchone()
        cur5.close()
        cur6 = mysql.connection.cursor()
        cur6.execute('SELECT count(*) FROM penilaian WHERE mahasiswa=%s AND hasil="B"',(rv[0],))
        rv6 = cur6.fetchone()
        cur6.close()
        cur7 = mysql.connection.cursor()
        cur7.execute('SELECT count(*) FROM penilaian WHERE mahasiswa=%s AND hasil="B-"',(rv[0],))
        rv7 = cur7.fetchone()
        cur7.close()
        cur8 = mysql.connection.cursor()
        cur8.execute('SELECT count(*) FROM penilaian WHERE mahasiswa=%s AND hasil="BC"',(rv[0],))
        rv8 = cur8.fetchone()
        cur8.close()
        cur9 = mysql.connection.cursor()
        cur9.execute('SELECT count(*) FROM penilaian WHERE mahasiswa=%s AND hasil="C+"',(rv[0],))
        rv9 = cur9.fetchone()
        cur9.close()
        cur10 = mysql.connection.cursor()
        cur10.execute('SELECT count(*) FROM penilaian WHERE mahasiswa=%s AND hasil="C"',(rv[0],))
        rv10 = cur10.fetchone()
        cur10.close()
        cur11 = mysql.connection.cursor()
        cur11.execute('SELECT count(*) FROM penilaian WHERE mahasiswa=%s AND hasil="D"',(rv[0],))
        rv11 = cur11.fetchone()
        cur11.close()
        cur12 = mysql.connection.cursor()
        cur12.execute('SELECT count(*) FROM penilaian WHERE mahasiswa=%s AND hasil="E"',(rv[0],))
        rv12 = cur12.fetchone()
        cur12.close()
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM note")
        note = cursor.fetchall()
        cursor.close()
        values = [
            rv2[0], rv3[0], rv4[0], rv5[0],rv6[0], rv7[0],rv8[0], rv9[0],rv10[0], rv11[0], rv12[0]]
        colors = [
                "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA"]
        labels = [
            'A', 'A-', 'AB', 'B+', 'B', 'B-', 'BC', 'C+', 'C','D','E']
        return render_template('mahasiswadashboard.html', nama=rv, max=50, set=zip(values, labels, colors), note=note)
    flash('Harap Login dulu','danger')
    return redirect(url_for('login'))

#PROFILE ADMIN
@app.route('/profile', methods=('GET', 'POST'))
def profile_admin():
    data = session.get('user')
    cur = mysql.connection.cursor()
    cur.execute('SELECT nama, npm, username, level FROM computer WHERE username=%s',(data,))
    rv = cur.fetchone()
    cur.close()
    return render_template('adminpro.html', data=rv)

#PROFILE DOSEN
@app.route('/profile-dosen', methods=('GET', 'POST'))
def profile_dosen():
    data = session.get('user')
    cur = mysql.connection.cursor()
    cur.execute('SELECT nama, npm, username, level FROM computer WHERE username=%s',(data,))
    rv = cur.fetchone()
    cur.close()
    return render_template('dosenprofile.html', data=rv)

#PROFILE MAHASISWA
@app.route('/profile-mahasiswa', methods=('GET', 'POST'))
def profile_mahasiswa():
    data = session.get('user')
    cur = mysql.connection.cursor()
    cur.execute('SELECT nama, npm, username, level FROM computer WHERE username=%s',(data,))
    rv = cur.fetchone()
    cur.close()
    return render_template('mhsprofile.html', data=rv)

#REGISTRASI DOSEN
@app.route('/dosen', methods=('GET', 'POST'))
def dosen():
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, nama, NPM, username FROM computer WHERE level = 'Dosen'")
    rv = cur.fetchall()
    cur.close()
    return render_template('admindos.html', computers=rv)

@app.route('/registrasi', methods=('GET', 'POST'))
def registrasi():
    if request.method == 'POST':
        nama = request.form['nama']
        npm = request.form['npm']
        username = request.form['username']
        password = request.form['password']
        level = request.form['level']
        # password = request.form['password'].encode('utf-8')
        #cek username atau email
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM computer WHERE username=%s ',(username, ))
        akun = cursor.fetchone()
        if akun is None:
            cursor.execute('INSERT INTO computer VALUES (%s, %s, %s, %s, %s)', (nama, npm, username,  generate_password_hash(password), level))
            mysql.connection.commit()
            flash('Registrasi Berhasil','success')
        else :
            flash('Username atau email sudah ada','danger')
    return render_template('registrasi2.html')

#REGISTRASI MAHASISWA
@app.route('/mahasiswa', methods=('GET', 'POST'))
def mahasiswa():
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, nama, NPM, username FROM computer WHERE level = 'Mahasiswa'")
    rv = cur.fetchall()
    cur.close()
    return render_template('adminmah.html', computers=rv)

#REGISTRASI MAHASISWA
@app.route('/dosen-mahasiswa', methods=('GET', 'POST'))
def mahasiswa_dosen():
    cur = mysql.connection.cursor()
    cur.execute("SELECT nama, NPM, username FROM computer WHERE level = 'Mahasiswa'")
    rv = cur.fetchall()
    cur.close()
    return render_template('dosenmhs.html', computers=rv)

#MATA KULIAH ADMIN
@app.route('/matakuliah', methods=('GET', 'POST'))
def matakuliah():
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, nama_matkul,sks,dosen FROM matakuliah")
    rv = cur.fetchall()
    cur.close()
    return render_template('matkul.html', matkul=rv)

#MATA KULIAH DOSEN
@app.route('/matakuliah-dosen', methods=('GET', 'POST'))
def matakuliah_dosen():
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, nama_matkul, sks, dosen FROM matakuliah")
    rv = cur.fetchall()
    cur.close()
    return render_template('dosenmatkul.html', matkul=rv)

#MATA KULIAH MHS
@app.route('/matakuliah-mahasiswa', methods=('GET', 'POST'))
def matakuliah_mahasiswa():
    cur = mysql.connection.cursor()
    cur.execute("SELECT nama_matkul, sks, dosen FROM matakuliah")
    rv = cur.fetchall()
    cur.close()
    return render_template('matakuliahmhs.html', matkul=rv)

#NILAI ADMIN
@app.route('/nilai', methods=('GET', 'POST'))
def nilai():
    cur = mysql.connection.cursor()
    cur.execute("SELECT nama FROM computer WHERE level='Mahasiswa'")
    rv = cur.fetchall()
    cur.close()
    cur2 = mysql.connection.cursor()
    cur2.execute("SELECT nama_matkul FROM matakuliah")
    rv2 = cur2.fetchall()
    cur2.close()
    cur3 = mysql.connection.cursor()
    cur3.execute("SELECT * FROM penilaian")
    rv3 = cur3.fetchall()
    cur3.close()
    if request.method == 'POST':
        mahasiswa = request.form['mahasiswa']
        matkul = request.form['matkul']
        presensi = request.form['presensi']
        uts = request.form['uts']
        uas = request.form['uas']
        tugasbesar = request.form['tugasbesar']
        tugaskecil = request.form['tugaskecil']
        bobot = float((10/100*presensi)+(20/100*uts)+(20/100*uas)(30/100*tugasbesar)(20/100*tugaskecil))

        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO computer VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', (mahasiswa, matkul, presensi, uts, uas, tugasbesar, tugaskecil, bobot))
        mysql.connection.commit()
    return render_template('adminnilai.html', mhs=rv, matkul=rv2, nilai=rv3)

#NILAI DOSEN
@app.route('/nilai-dosen', methods=('GET', 'POST'))
def nilai_dosen():
    cur = mysql.connection.cursor()
    cur.execute("SELECT nama FROM computer WHERE level='Mahasiswa'")
    rv = cur.fetchall()
    cur.close()
    cur2 = mysql.connection.cursor()
    cur2.execute("SELECT nama_matkul FROM matakuliah")
    rv2 = cur2.fetchall()
    cur2.close()
    cur3 = mysql.connection.cursor()
    cur3.execute("SELECT * FROM penilaian")
    rv3 = cur3.fetchall()
    cur3.close()
    if request.method == 'POST':
        mahasiswa = request.form['mahasiswa']
        matkul = request.form['matkul']
        presensi = request.form['presensi']
        uts = request.form['uts']
        uas = request.form['uas']
        tugasbesar = request.form['tugasbesar']
        tugaskecil = request.form['tugaskecil']
        bobot = float((10/100*presensi)+(20/100*uts)+(20/100*uas)(30/100*tugasbesar)(20/100*tugaskecil))

        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO computer VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', (mahasiswa, matkul, presensi, uts, uas, tugasbesar, tugaskecil, bobot))
        mysql.connection.commit()
    return render_template('dosennilai.html',mhs=rv, matkul=rv2, nilai=rv3)

#LAPORAN NILAI MAHASISWA
@app.route('/laporan-hasilstudi', methods=('GET', 'POST'))
def laporanhasilstudi():
    mahasiswa = session.get('mhs')
    cur = mysql.connection.cursor()
    cur.execute("SELECT matkul, bobot, hasil FROM penilaian WHERE mahasiswa=%s",(mahasiswa,))
    rv = cur.fetchall()
    cur.close()
    return render_template('nilaimhs.html', nilai=rv)

@app.route('/simpan-nilai-admin', methods=["POST"])
def simpan_nilai_admin():
    mahasiswa = request.form['mahasiswa']
    matkul = request.form['matkul']
    presensi = request.form['presensi']
    uts = request.form['uts']
    uas = request.form['uas']
    tugasbesar = request.form['tugasbesar']
    tugaskecil = request.form['tugaskecil']

    bobot = float((10/100*float(presensi))+(20/100*float(uts))+(20/100*float(uas))+(30/100*float(tugasbesar))+(20/100*float(tugaskecil)))
    hasil = None
    if bobot >= float(85) and bobot <=float(100):
        hasil = 'A'
    elif bobot >= float(80) and bobot <float(85):
        hasil = 'A-'
    elif bobot >= float(76) and bobot <float(80):
        hasil = 'AB'
    elif bobot >= float(72) and bobot <float(76):
        hasil = 'B+'
    elif bobot >= float(68) and bobot <float(72):
        hasil = 'B'
    elif bobot >= float(65) and bobot <float(68):
        hasil = 'B-'
    elif bobot >= float(62) and bobot <float(65):
        hasil = 'BC'
    elif bobot >= float(59) and bobot <float(62):
        hasil = 'C+'
    elif bobot >= float(56) and bobot <float(69):
        hasil = 'C'
    elif bobot >= float(45) and bobot <float(56):
        hasil = 'D'
    elif bobot <float(45):
        hasil = 'E'
    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO penilaian VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)', (mahasiswa, matkul, presensi, uts, uas, tugasbesar, tugaskecil, bobot, hasil,))
    mysql.connection.commit()
    return redirect(url_for('nilai'))

@app.route('/simpan-nilai', methods=["POST"])
def simpan_nilai():
    mahasiswa = request.form['mahasiswa']
    matkul = request.form['matkul']
    presensi = request.form['presensi']
    uts = request.form['uts']
    uas = request.form['uas']
    tugasbesar = request.form['tugasbesar']
    tugaskecil = request.form['tugaskecil']

    bobot = float((10/100*float(presensi))+(20/100*float(uts))+(20/100*float(uas))+(30/100*float(tugasbesar))+(20/100*float(tugaskecil)))
    hasil = None
    if bobot >= float(85) and bobot <=float(100):
        hasil = 'A'
    elif bobot >= float(80) and bobot <float(85):
        hasil = 'A-'
    elif bobot >= float(76) and bobot <float(80):
        hasil = 'AB'
    elif bobot >= float(72) and bobot <float(76):
        hasil = 'B+'
    elif bobot >= float(68) and bobot <float(72):
        hasil = 'B'
    elif bobot >= float(65) and bobot <float(68):
        hasil = 'B-'
    elif bobot >= float(62) and bobot <float(65):
        hasil = 'BC'
    elif bobot >= float(59) and bobot <float(62):
        hasil = 'C+'
    elif bobot >= float(56) and bobot <float(69):
        hasil = 'C'
    elif bobot >= float(45) and bobot <float(56):
        hasil = 'D'
    elif bobot <float(45):
        hasil = 'E'
    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO penilaian VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)', (mahasiswa, matkul, presensi, uts, uas, tugasbesar, tugaskecil, bobot, hasil,))
    mysql.connection.commit()
    return redirect(url_for('nilai_dosen'))

#CRUD REGISTRASI
@app.route('/simpan', methods=["POST"])
def simpan():
    nama = request.form['nama']
    npm = request.form['npm']
    username = request.form['username']
    password = request.form['password']
    level = request.form['level']
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO computer VALUES (NULL ,%s, %s, %s, %s, %s)', (nama, npm, username, generate_password_hash(password),level,))
    mysql.connection.commit()
    return redirect(url_for('registrasi'))

@app.route('/update', methods=["POST"])
def update():
    id_data = request.form['id']
    nama = request.form['nama']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE computer SET data=%s WHERE id=%s", (nama, id_data,))
    mysql.connection.commit()
    return redirect(url_for('registrasi'))

@app.route('/update-dsn', methods=["POST"])
def update_dsn():
    id_data = request.form['id']
    nama = request.form['nama']
    npm = request.form['npm']
    username = request.form['username']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE computer SET nama=%s, npm=%s, username=%s WHERE id=%s", (nama, npm,username,id_data))
    mysql.connection.commit()
    return redirect(url_for('dosen'))

@app.route('/update-mhs', methods=["POST"])
def update_mhs():
    id_data = request.form['id']
    nama = request.form['nama']
    npm = request.form['npm']
    username = request.form['username']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE computer SET nama=%s, npm=%s, username=%s WHERE id=%s", (nama, npm,username,id_data))
    mysql.connection.commit()
    return redirect(url_for('mahasiswa'))

@app.route('/update-mtklh', methods=["POST"])
def update_mtklh():
    id_data = request.form['id']
    nama = request.form['nama']
    sks = request.form['sks']
    dosen = request.form['dosen']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE matakuliah SET nama_matkul=%s, sks=%s, dosen=%s WHERE id=%s", (nama, sks,dosen,id_data))
    mysql.connection.commit()
    return redirect(url_for('matakuliah'))

@app.route('/update-mtklh-dsn', methods=["POST"])
def update_mtklh_dsn():
    id_data = request.form['id']
    nama = request.form['nama']
    sks = request.form['sks']
    dosen = request.form['dosen']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE matakuliah SET nama_matkul=%s, sks=%s, dosen=%s WHERE id=%s", (nama, sks,dosen,id_data))
    mysql.connection.commit()
    return redirect(url_for('matakuliah_dosen'))

@app.route('/hapus/<string:id_data>', methods=["GET"])
def hapus(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM computer WHERE nama=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('mahasiswa'))

@app.route('/hapus-matakuliah/<string:id_data>', methods=["GET"])
def hapus_matkul(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM matakuliah WHERE nama_matkul=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('matakuliah'))

@app.route('/hapus-nilai/<string:id_data>', methods=["GET"])
def hapus_nilai(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM penilaian WHERE mahasiswa=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('nilai'))

@app.route('/hapus-nilai-dosen/<string:id_data>', methods=["GET"])
def hapus_nilai_dosen(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM penilaian WHERE mahasiswa=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('nilai_dosen'))

@app.route('/hapus-note/<string:id_data>', methods=["GET"])
def hapus_note(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM note WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('dashboard_mahasiswa'))

@app.route('/simpan-matkul', methods=["POST"])
def simpan_matkul():
    matkul = request.form['matkul']
    sks = request.form['sks']
    dosen = request.form['dosen']
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO matakuliah VALUES (NULL ,%s, %s, %s)', (matkul,sks,dosen,))
    mysql.connection.commit()
    return redirect(url_for('matakuliah'))
    
@app.route('/simpan-note', methods=["POST"])
def simpan_note():
    note = request.form['note']
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO note VALUES (NULL ,%s)', (note,))
    mysql.connection.commit()
    return redirect(url_for('dashboard_mahasiswa'))

@app.route('/search', methods=('GET', 'POST'))
def search():
    keyword = request.form.get('keyword')
    print(keyword)
    cur = mysql.connection.cursor()
    cur.execute("SELECT nama, npm, username from computer WHERE level='Dosen' AND nama LIKE %s", ('%'+keyword+'%',))
    rv = cur.fetchall()
    cur.close()
    return render_template('search-admin-dsn.html', results=rv)

@app.route('/search-mhs', methods=('GET', 'POST'))
def search_mhs():
    keyword = request.form.get('keyword')
    print(keyword)
    cur = mysql.connection.cursor()
    cur.execute("SELECT nama, npm, username from computer WHERE level='Mahasiswa' AND nama LIKE %s", ('%'+keyword+'%',))
    rv = cur.fetchall()
    cur.close()
    return render_template('search-admin-mahasiswa.html', results=rv)

#logout
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('username', None)
    #session.pop('level', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)


