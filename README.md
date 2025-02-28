# Synthetic Employee Leave Dataset Generator

## Overview
This project generates a synthetic dataset for employee leave approvals using AI/ML models and Faker-based randomization. Synthetic data is useful for testing, training machine learning models, and ensuring privacy when working with sensitive employee data. The dataset includes key details such as employee information, leave type, approval status, and performance metrics. It is containerized with **Docker** to ensure ease of use and scalability.

## Features
- Generates **5,000 to 10,000** synthetic employee leave records
- Uses **Faker** to generate realistic employee details
- Supports **GPT-4 API integration** (optional) for enhanced data realism by generating structured leave requests
- Saves dataset **incrementally to CSV** to prevent data loss
- **Dockerized** for easy deployment and script execution
- Allows running **multiple Python scripts** inside a single container

## Prerequisites
Ensure you have the following installed:
- **Python 3.11**
- **pip** (Python package manager)
- **Docker** (for containerized execution)

## Installation
### 1. Clone the Repository
```sh
git clone https://github.com/Deepanshu-Sehgal/Leave-Approval-Project.git
cd synthetic-leave-dataset
```

### 2. Install Dependencies
```sh
pip install -r requirements.txt
```

### 3. Set Up Environment Variables
Create a **.env** file and add your OpenAI API key (if using GPT-4 for data generation):
```sh
echo "OPENAI_API_KEY=your_api_key_here" > .env
```

## Running the Dataset Generator
Run the script locally:
```sh
python generate_dataset.py
```

## Docker Setup
### 1. Build the Docker Image
```sh
docker build -t synthetic-leave-dataset .
```

### 2. Run the Container (Idle Mode)
```sh
docker run -d --name leave-dataset synthetic-leave-dataset
```
This keeps the container running so that scripts can be executed as needed.

### 3. Run a Specific Python Script Inside the Container
```sh
docker exec -it leave-dataset python generate_dataset.py
```

### 4. Stop and Remove the Container
```sh
docker stop leave-dataset && docker rm leave-dataset
```

## Accessing Generated Data
By default, the generated dataset is saved as **synthetic_employee_leave_data.csv** inside the `/app` directory of the container. This location can be customized by modifying the script parameters. To copy the file to your local machine, use:
```sh
docker cp leave-dataset:/app/synthetic_employee_leave_data.csv .
```

## Running with Volume Mounting (Persistent Data)
To ensure the generated CSV file is directly accessible on your host machine:
```sh
docker run -d --name leave-dataset -v $(pwd)/data:/app/data synthetic-leave-dataset
```
This saves all CSV files inside the `./data` folder on your local machine.

## Future Enhancements
- Implement AI/ML-based leave approval predictions (Planned feature)
- Add a REST API for requesting synthetic datasets
- Integrate database storage options (MySQL, PostgreSQL, MongoDB)

## License
This project is licensed under the **MIT License**. For more details, refer to [MIT License](https://opensource.org/licenses/MIT).

