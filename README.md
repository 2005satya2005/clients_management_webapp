# Intern Portal

Client Management Portal is a web-app that Manages Clients. .

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