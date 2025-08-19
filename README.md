

<img width="3780" height="1890" alt="Purple and White Futuristic Artificial Intelligence Technology Banner (1)" src="https://github.com/user-attachments/assets/900d9e6d-7e4a-4d83-ae48-a94614c6a7d6" />


# Satra- A Clients Management Webapp

A Full-stack webapp designed to simplify and streamline client management for businesses. It offers a secure login system, an intuitive dashboard, and comprehensive features to manage client information efficiently. Users can add new clients with details such as name, contact information, services provided, payment status, and upload related documents like invoices or images. The Manage Clients section allows searching, editing, and deleting client records with ease, giving businesses full control over their client database. With a modern, user-friendly interface and organized workflow, this app helps companies save time, stay organized, and maintain professional relationships effectively

✅ Prerequisites

- Python installed (version 3.7+ recommended)
- Flask and pandas installed
  - If not installed, use:  
    ```bash
    pip install flask pandas
    ```


📁 File/Folder Layout:
----------------------------------------------------
clients_management_webapp/
│
├── static/
|   ├── style.css       
│   └── uploads/
│
├── templates/
│   ├── login.html
|   ├── dashboard.html
|   ├── add_client.html
|   ├── edit_client.html
│   └── manage_clients.html
│
├── clients.db
|
|
├── README.md
|
└── app.py
    


🛠️ Step-by-Step Setup

### 🔹 Step 1: Download

1. Download the code/Folder clients_management_webapp  

2. Follow the step 2

### 🔹 Step 2: Run the Server

1. Go to the folder:

   - Using command line:
     ```bash
     cd path_to/clients_management_webapp/
     ```

   - Or right-click the 'clients_management_webapp' and choose **"Open in Terminal"** or **"Open PowerShell window here"**.

2. Run the Flask server:

   ```bash
   python app.py

3. You will see output like:
Running on http://127.0.0.1:5000/

### 🔹 Step 3: Open the application 

1. Open your web browser.

2. Go to:
http://127.0.0.1:5000

3. The Portal appears.
4. Enter the user name and password (username- admin, password- admin).
5. Click Login it will redirect to dashboard page.
6. Open add clients fill the details and save it, you can now able to edit/delete it in manage clients section.
