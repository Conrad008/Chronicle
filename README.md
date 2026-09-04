# Chronicle | Photo Gallery

A responsive Django photo gallery web application designed to showcase artworks, portraits, and photography. Built with Django 3.x, PostgreSQL, and styled using Tailwind CSS with a custom warm earth-tone palette.


##  Features

* **User Authentication & Profiles:** Custom registration, secure login/logout, and user profile pages displaying liked photos.
* **Photo Gallery Display:** Dynamic photo grid layout featuring titles, tags, and detail view pages.
* **Tag Filtering:** Filter photo collections by tags to easily locate specific categories.
* **User Interactions:** Interactive like and dislike system for authenticated users.
* **Photo Uploads:** Front-end image publishing form with tag assignments and metadata handling.
* **Responsive Design:** Mobile-first layout styled using Tailwind CSS with a custom **Warm & Natural** palette (`#FDFBF7`, `#2C2A29`, `#A35C3E`, `#4A6B5B`).

---

##  Tech Stack

* **Backend:** Python 3.x, Django 3.x
* **Database:** PostgreSQL (Production), SQLite (Local Development)
* **Frontend:** HTML5, CSS3, Tailwind CSS (via CDN)
* **Production Tools:** Gunicorn, WhiteNoise, `dj-database-url`, Pillow
* **Version Control & Hosting:** Git, GitHub, Render

---

##  Project Structure

```text
chronicle/
├── manage.py
├── build.sh
├── Procfile
├── requirements.txt
├── .gitignore
├── README.md
├── chronicle/                  # Main Project Settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── photo_gallery/              # App Logic
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── templates/                  # Flat Templates Directory
│   ├── base.html
│   ├── photo_list.html
│   ├── photo_detail.html
│   ├── profile.html
│   ├── upload_photo.html
│   ├── login.html
│   └── register.html
└── media/                      # Uploaded Media Files (Local)
    └── photos/

```

## How to Contribute

1. **Fork the Repository:** Create your own copy of the project to work on.
2. **Create a Feature Branch:**

```bash
git checkout -b feature/AmazingFeature

```
3. **Commit Your Changes:**

```bash
    git commit -m 'Add some AmazingFeature'
```

4.  **Push to the Branch:**
```bash
    git push origin feature/AmazingFeature
```

5.  **Open a Pull Request:** Describe your changes and submit for review.

**Coding Standards**
*   Ensure all HTML is semantic and well-commented.
*   Maintain the **Warm natural** color palette for all UI additions.
*   Test responsiveness across multiple screen sizes before submitting.


## Getting Started

**Prerequisites**
Any modern web browser (Chrome, Firefox, Safari, or Edge).

Installation
1. **Clone the repository:**
   
```bash
   git clone https://github.com/Conrad008/Chronicle.git
   cd Chronicle
```

2. **Open the project:**
Simply open the index.html file in your preferred browser to view the current build.

## License

This project is licensed under the MIT License.

## author
**conrad kipngeno**