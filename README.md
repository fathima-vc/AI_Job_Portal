
## Project Screenshots

### Home Page
![Home Page](Screenshots/Screenshot%202026-11-22%20160709.png)

### Recruiter Dashboard
![Recruiter Dashboard](Screenshots/Screenshot%202026-11-22%20160842.png)

### Resume Analysis
![Resume Analysis](Screenshots/Screenshot%202026-11-22%20160924.png)

![Resume Analysis](Screenshots/Screenshot%202026-11-22%20161002.png)

![Resume Analysis](Screenshots/Screenshot%202026-11-22%20161023.png)

![Resume Analysis](Screenshots/Screenshot%202026-11-22%20161146.png)

![Resume Analysis](Screenshots/Screenshot%202026-11-22%20161209.png)

![Resume Analysis](Screenshots/Screenshot%202026-11-22%20161223.png)

![Resume Analysis](Screenshots/Screenshot%202026-11-22%20161237.png)

\# AI Job Portal



An online job portal built using Python and Django that connects job seekers with recruiters. The platform allows users to explore job opportunities, apply for jobs, manage applications, and evaluate resumes.



\## Features



\### Job Seeker

\- User registration and login

\- Upload PDF resumes

\- Extract text from uploaded resumes

\- Resume evaluation with a free rule-based scoring system

\- Identify technical skills and soft skills

\- Get suggestions for improving resumes

\- Browse and search job opportunities

\- Apply for jobs with a cover letter

\- Track application status



\### Recruiter

\- Recruiter registration and login

\- Recruiter dashboard

\- Post new job opportunities

\- Edit and delete posted jobs

\- View applicants

\- Update application status



\## Technologies Used



\- \*\*Backend:\*\* Python, Django

\- \*\*Frontend:\*\* HTML, CSS, Bootstrap, JavaScript

\- \*\*Database:\*\* MySQL

\- \*\*Resume Processing:\*\* PyPDF

\- \*\*Version Control:\*\* Git and GitHub



\## Resume Evaluation



The project includes a free, rule-based resume evaluation system. It checks resume content, identifies skills, provides a score, and suggests improvements. It does not require paid AI API access.



\## Project Setup



1\. Clone the repository:



&#x20;  ```bash

&#x20;  git clone https://github.com/fathima-vc/AI\_Job\_Portal.git

&#x20;  ```



2\. Navigate to the project folder:



&#x20;  ```bash

&#x20;  cd AI\_Job\_Portal

&#x20;  ```



3\. Create and activate a virtual environment:



&#x20;  ```bash

&#x20;  python -m venv venv

&#x20;  ```



&#x20;  Windows:



&#x20;  ```bash

&#x20;  venv\\Scripts\\activate

&#x20;  ```



4\. Install dependencies:



&#x20;  ```bash

&#x20;  pip install -r requirements.txt

&#x20;  ```



5\. Configure your environment variables in a `.env` file. Add your own Django secret key and MySQL database settings. Do not upload this file to GitHub.



6\. Run database migrations:



&#x20;  ```bash

&#x20;  python manage.py migrate

&#x20;  ```



7\. Start the development server:



&#x20;  ```bash

&#x20;  python manage.py runserver

&#x20;  ```



8\. Open `http://127.0.0.1:8000/` in your browser.



\## Author



\*\*Fathima VC\*\*



GitHub: \[fathima-vc](https://github.com/fathima-vc)

