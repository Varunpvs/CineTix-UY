# 🎬 CineTix - Simple Movie Ticket Booking platforms with polls

## 📌 Overview
The **CineTix** is a Django-based web application that allows users to vote for movies, book seats in theaters, and manage their bookings. The system dynamically generates seat layouts and enables users to select available seats interactively.

---
## 🚀 Features

✅ **User Authentication**: Secure login and registration for users.  
✅ **Movie Poll System**: Users vote on movies to decide if bookings should open.  
✅ **Dynamic Seat Selection**: Users can select seats interactively from a theater layout.  
✅ **Real-Time Booking Management**: Book, view, and cancel seat reservations.  
✅ **Admin Controls**: Admin can manage movies, theaters, screens, and bookings.  

---
## 🏗️ Tech Stack

- **Backend**: Django, Python
- **Frontend**: HTML, CSS, JavaScript (for dynamic seat selection)
- **Database**: SQLite (default) / PostgreSQL (recommended for production)
- **Authentication**: Django Auth
- **Deployment**: Docker, Gunicorn

---

---
## 🔧 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/movie-booking-system.git
cd movie-booking-system
```

### 2️⃣ Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create a Superuser (Admin)
```bash
python manage.py createsuperuser
```

### 6️⃣ Run the Server
```bash
python manage.py runserver
```

---
## 🎭 Usage

1️⃣ **Login/Register** on the platform.  
2️⃣ **Vote** for a movie in the poll section.  
3️⃣ If the poll is approved, **book seats** in an available theater.  
4️⃣ Select your **seats dynamically** and confirm booking.  
5️⃣ View or cancel your bookings from the dashboard.  

---
## 🎨 Dynamic Seat Selection UI
The seat selection uses **JavaScript & AJAX** to display real-time availability. Seats are **color-coded**:
- 🟢 **Available**
- 🔴 **Booked**
- 🔵 **Selected by the user**

Users can hover over seats, click to select, and finalize the booking.

---
## 🛠️ API Endpoints
| Method | Endpoint               | Description |
|--------|------------------------|-------------|
| GET    | `/movies/`             | List movies |
| GET    | `/polls/`              | View polls |
| POST   | `/polls/vote/`         | Vote for a movie |
| GET    | `/bookings/`           | View user bookings |
| POST   | `/bookings/book/`      | Book a seat |
| POST   | `/bookings/cancel/`    | Cancel a booking |

---
## 🖥️ Admin Panel
Access the Django admin panel:
```bash
http://127.0.0.1:8000/admin/
```
Use the **superuser** credentials created earlier to manage users, movies, polls, and bookings.

---
## 📜 License
This project is licensed under the **MIT License**.

