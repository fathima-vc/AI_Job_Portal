# AI Job Portal 🚀

A web-based job portal developed using **Python and Django** that connects job seekers with recruiters. The platform allows users to explore job opportunities, apply for jobs, manage applications, and evaluate resumes.

## ✨ Key Features

### 👩‍💻 Job Seeker
- User registration and login
- Upload PDF resumes
- Extract text from uploaded resumes
- Resume evaluation using a free rule-based scoring system
- Identify technical and soft skills
- Get suggestions for improving resumes
- Browse and search job opportunities
- Apply for jobs with a cover letter
- Track application status

### 🏢 Recruiter
- Recruiter registration and login
- Dedicated recruiter dashboard
- Post new job opportunities
- Edit and delete job postings
- View applicants and cover letters
- Update application statuses

## 🛠️ Technologies Used

| Category | Technologies |
|---|---|
| Backend | Python, Django |
| Frontend | HTML, CSS, Bootstrap, JavaScript |
| Database | MySQL |
| PDF Processing | pypdf |
| Version Control | Git, GitHub |

## 📄 Resume Evaluation System

The project includes a free, rule-based resume evaluation system that:

- Extracts text from uploaded PDF resumes.
- Identifies technical and soft skills.
- Generates a resume score.
- Provides suggestions for improvement.
- Recommends relevant job roles based on detected skills.

**Note:** Resume evaluation uses locally implemented rules and does not require paid AI API access.

## 📸 Project Screenshots

### 🏠 Home Page

![Home Page](Screenshots/Screenshot%202026-11-22%20160709.png)

### 🏢 Recruiter Dashboard

![Recruiter Dashboard](Screenshots/Screenshot%202026-11-22%20160842.png)

### 📊 Resume Analysis

![Resume Analysis 1](Screenshots/Screenshot%202026-11-22%20160924.png)

![Resume Analysis 2](Screenshots/Screenshot%202026-11-22%20161002.png)

![Resume Analysis 3](Screenshots/Screenshot%202026-11-22%20161023.png)

![Resume Analysis 4](Screenshots/Screenshot%202026-11-22%20161146.png)

![Resume Analysis 5](Screenshots/Screenshot%202026-11-22%20161209.png)

![Resume Analysis 6](Screenshots/Screenshot%202026-11-22%20161223.png)

![Resume Analysis 7](Screenshots/Screenshot%202026-11-22%20161237.png)

## ⚙️ Installation and Setup

Follow these steps to run the project locally.

### 1. Clone the repository

```bash
git clone https://github.com/fathima-vc/AI_Job_Portal.git
```

### 2. Navigate to the project folder

```bash
cd AI_Job_Portal
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure environment variables

Create a `.env` file in the project root directory. Add your own Django secret key and MySQL database settings.

Do not upload your `.env` file or database credentials to GitHub.

### 7. Run database migrations

```bash
python manage.py migrate
```

### 8. Start the development server

```bash
python manage.py runserver
```

### 9. Open the application

Visit:

http://127.0.0.1:8000/

## 🎯 Project Objective

This project demonstrates practical skills in Python Full Stack Development, Django web development, database integration, authentication, PDF processing, and job application management.

## 👩‍💻 Author

**Fathima VC**

- GitHub Profile: [fathima-vc](https://github.com/fathima-vc)
- Project Repository: [AI Job Portal](https://github.com/fathima-vc/AI_Job_Portal)
