# **Flask Blog**

A simple blog application built with Flask and MongoDB, allowing users to create, view, and manage blog posts.

---

## **Features**

- View a list of all blog posts.
- Create new blog posts using a simple form.
- View detailed content of individual blog posts.
- Integrated with MongoDB for seamless data storage.

---

## **Technologies Used**

- **Backend**: Flask, Flask-PyMongo
- **Database**: MongoDB
- **Frontend**: HTML, CSS
- **Language**: Python

---

## **Getting Started**

### **Prerequisites**

1. Python (version 3.7+ recommended)
2. MongoDB installed and running locally
3. pip (Python package installer)

---

### **Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/havish7728/Flask-Blog.git
   cd Flask-Blog
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - **Windows**:
     ```bash
     .\venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Ensure MongoDB is running on your local machine.

---

### **Running the Application**

1. Start the Flask development server:
   ```bash
   python app.py
   ```

2. Open your web browser and visit:
   ```plaintext
   http://127.0.0.1:5000/
   ```

---

## **Project Structure**

```plaintext
Flask-Blog/
│
├── app.py                 # Main application file
├── requirements.txt       # Project dependencies
├── venv/                  # Virtual environment
├── templates/             # HTML templates
│   ├── index.html         # Home page (list of blog posts)
│   ├── post.html          # View a single blog post
│   └── new_post.html      # Create a new blog post
├── static/                # Static files (CSS, images, etc.)
│   └── style.css          # Custom styles
└── README.md              # Project documentation
```

---

## **Usage**

- **Homepage**: Lists all blog posts.
- **Create New Post**: Navigate to `/new` to add a new blog post.
- **View Post**: Click on any blog title to view its details.


## **Contributing**

Contributions are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.
