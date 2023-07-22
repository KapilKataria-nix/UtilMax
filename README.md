# UtilMax

## CPU and Memory Utilization Monitor

This is a simple Flask web application that monitors CPU and memory utilization of the system using the `psutil` library. If the CPU or memory utilization exceeds 80%, the application will display a warning message suggesting to scale up the resources.

## Prerequisites

Before running the application, make sure you have the following installed:

- Python (version 3.6 or higher)
- Flask
- psutil

You can install Flask and psutil using pip:

```bash
pip install flask psutil
```

## How to Run

1. Clone this repository to your local machine or download the ZIP file and extract it.

2. Navigate to the project directory in your terminal or command prompt.

3. Run the Flask application by executing the following command:

```bash
python your_file_name.py
```

Replace `your_file_name.py` with the name of the Python file containing the code (e.g., `app.py`).

4. Once the application is running, open your web browser and visit `http://127.0.0.1:5000/`.

## How it Works

1. The application uses the Flask framework to create a simple web server.

2. When you visit the homepage (`/`), the server will call the `index` function.

3. Inside the `index` function, the `psutil` library is used to get the CPU and memory utilization.

4. If the CPU utilization or memory utilization is above 80%, a warning message will be displayed suggesting to scale up.

5. The `index.html` file, located in the `templates` directory, will be rendered with the CPU and memory utilization metrics and the warning message (if applicable).

## Customization

You can customize the behavior of the application by modifying the `if` condition in the `index` function in `your_file_name.py`. For example, you can change the threshold value from 80 to any other percentage as per your requirements.

## Notes

- This application is intended for demonstration purposes and may not be suitable for production environments without further security and performance optimizations.

- The web server is set to run on all available network interfaces (`0.0.0.0`) and in debug mode (`debug=True`) for development purposes. In production, you should configure it differently.

- For a more robust solution, consider deploying the application using a production-ready web server like Nginx or Gunicorn.

