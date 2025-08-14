from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3, os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "supersecretkey"
UPLOAD_FOLDER = "static/uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def init_db():
    conn = sqlite3.connect('clients.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT, address TEXT, email TEXT, phone TEXT,
        date TEXT, service TEXT, problem TEXT,
        net_amount REAL, amount_paid REAL, amount_to_be_paid REAL,
        image TEXT, invoice TEXT
    )''')
    conn.commit()
    conn.close()

init_db()

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        if username == "admin" and password == "admin":
            return redirect(url_for('dashboard'))
        if username == "0" and password == "0":
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid credentials")
    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/add_client", methods=["GET", "POST"])
def add_client():
    if request.method == "POST":
        try:
            data = request.form

            # Handle file uploads
            image_file = request.files.get('image')
            invoice_file = request.files.get('invoice')

            if not image_file or not invoice_file:
                flash("Please upload both image and invoice files.")
                return redirect(url_for('add_client'))

            image_filename = secure_filename(image_file.filename)
            invoice_filename = secure_filename(invoice_file.filename)

            # Ensure uploads folder exists
            os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

            # Save files
            image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], image_filename))
            invoice_file.save(os.path.join(app.config['UPLOAD_FOLDER'], invoice_filename))

            # Insert into database
            conn = sqlite3.connect('clients.db')
            c = conn.cursor()
            c.execute('''INSERT INTO clients
                (name,address,email,phone,date,service,problem,net_amount,amount_paid,amount_to_be_paid,image,invoice)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?)''', (
                data['name'], data['address'], data['email'], data['phone'], data['date'],
                data['service'], data['problem'], data['net_amount'], data['amount_paid'] ,
                data['amount_to_be_paid'], image_filename, invoice_filename
            ))
            conn.commit()
            conn.close()

            flash("Client added successfully!")
            return redirect(url_for('manage_clients'))

        except Exception as e:
            flash(f"Error adding client: {str(e)}")
            return redirect(url_for('add_client'))

    return render_template("add_client.html")


@app.route("/manage_clients")
def manage_clients():
    search = request.args.get('search')
    conn = sqlite3.connect('clients.db')
    c = conn.cursor()
    if search:
        c.execute("SELECT * FROM clients WHERE name LIKE ?", ('%'+search+'%',))
    else:
        c.execute("SELECT * FROM clients")
    clients = c.fetchall()
    conn.close()
    return render_template("manage_clients.html", clients=clients)

@app.route("/edit_client/<int:id>", methods=["GET", "POST"])
def edit_client(id):
    conn = sqlite3.connect('clients.db')
    c = conn.cursor()

    if request.method == "POST":
        try:
            data = request.form
            # Get uploaded files (optional)
            image_file = request.files.get('image')
            invoice_file = request.files.get('invoice')

            # Fetch current filenames
            c.execute("SELECT image, invoice FROM clients WHERE id=?", (id,))
            current_files = c.fetchone()
            current_image, current_invoice = current_files

            # If new files are uploaded, replace them; otherwise keep old
            if image_file and image_file.filename:
                image_filename = secure_filename(image_file.filename)
                image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], image_filename))
            else:
                image_filename = current_image

            if invoice_file and invoice_file.filename:
                invoice_filename = secure_filename(invoice_file.filename)
                invoice_file.save(os.path.join(app.config['UPLOAD_FOLDER'], invoice_filename))
            else:
                invoice_filename = current_invoice

            # Update database
            c.execute('''UPDATE clients SET
                name=?, address=?, email=?, phone=?, date=?, service=?, problem=?,
                net_amount=?, amount_paid=?, amount_to_be_paid=?, image=?, invoice=?
                WHERE id=?''', (
                data['name'], data['address'], data['email'], data['phone'], data['date'],
                data['service'], data['problem'], data['net_amount'], data['amount_paid'],
                data['amount_to_be_paid'], image_filename, invoice_filename, id
            ))
            conn.commit()
            flash("Client updated successfully!")
        except Exception as e:
            flash(f"Error updating client: {str(e)}")
        finally:
            conn.close()

        return redirect(url_for('manage_clients'))

    else:
        # GET request: fetch client details
        c.execute("SELECT * FROM clients WHERE id=?", (id,))
        client = c.fetchone()
        conn.close()
        return render_template("edit_client.html", client=client)


@app.route("/delete_client/<int:id>")
def delete_client(id):
    conn = sqlite3.connect('clients.db')
    c = conn.cursor()
    c.execute("DELETE FROM clients WHERE id=?", (id,))
    conn.commit()
    conn.close()
    flash("Client deleted successfully!")
    return redirect(url_for('manage_clients'))

if __name__ == "__main__":
    app.run(debug=True)
