# **Fibonacci API Service**

## **Description**
This is a simple Flask-based REST API that calculates the nth Fibonacci number. The service accepts a GET request with a query parameter `n` (an integer) and returns the Fibonacci value for the given number.

## **Table of Contents**
- Prerequisites  
- Installation  
  - Method 1: Run Locally with Python  
  - Method 2: Run Locally with Docker  
- Endpoints  
- Error Handling  
- Production Considerations  
- Deployment  

---

## **Prerequisites**
Ensure the following tools are installed:
- Python 3.10+ → [Download Python](https://www.python.org/downloads/)
- Docker → [Install Docker](https://docs.docker.com/get-docker/)

---

## **Installation**

### **Method 1: Run Locally with Python**

**Step 1: Clone the Repository**
```bash
git clone https://github.com/Supraja-Reddy-2628/fibonacci-API.git
cd fibonacci-API
```

**Step 2: Set up a Virtual Environment**
```bash
python3 -m venv venv
```
Activate the virtual environment:  
- macOS/Linux: `source venv/bin/activate`  
- Windows: `venv\Scripts\activate`

**Step 3: Install Dependencies**
```bash
pip install -r requirements.txt
```

**Step 4: Run the Flask Application**
```bash
python app.py
```
The application will be available at: `http://127.0.0.1:80`

**Step 5: Test the API**
You can test the API with tools like curl or Postman:
```
GET http://127.0.0.1/fibonacci?n=10
```

---

### **Method 2: Run Locally with Docker**

**Step 1: Build the Docker Image**
```bash
docker build -t fibonacci-api .
```

**Step 2: Run the Docker Container**
```bash
docker run -p 80:80 fibonacci-api
```

The API will be available at `http://127.0.0.1:80`.

---

## **Endpoints**

### **Request**
```
GET /fibonacci?n=<number>
```

### **Successful Response (200 OK)**
```json
{
  "status": 200,
  "message": "Fibonacci successfully calculated",
  "number": 10,
  "fibonacci": 55
}
```

### **Error Responses**
- **400 Bad Request** (missing or invalid input):
```json
{
  "status": 400,
  "message": "Parameter \"number\" is required and must be an integer",
  "error": "Missing or invalid query parameter"
}
```
- **400 Bad Request** (negative number):
```json
{
  "status": 400,
  "message": "Invalid input: Fibonacci number cannot be computed for negative numbers",
  "error": "Fibonacci number cannot be computed for negative numbers."
}
```
- **500 Internal Server Error** (unexpected failure):
```json
{
  "status": 500,
  "message": "An unexpected error occurred",
  "error": "Error details"
}

**Continuous Integration/Continuous Deployment (CI/CD):**
We use GitHub Actions to automate the process of building the Docker image, pushing it to Azure Container Registry, and deploying it to Azure App Service.
See .github/workflows/deploy.yml for details.


## **Error Handling**
- **Invalid or Missing Query Parameter**: Returns 400 with a descriptive message.
- **Negative Input**: Returns 400 with an error indicating Fibonacci numbers cannot be negative.
- **Unhandled Exceptions**: Returns 500 with a general error message.


## **Production Considerations**
- **Containerization**: The application is containerized using Docker, enabling easy deployment across environments.
- **CI/CD**: Automate deployments using GitHub Actions, Azure Pipelines, or other CI/CD tools.

### **Scaling**
- Azure App Service supports automatic horizontal scaling.
- We can enable autoscaling through the Azure portal or CLI by configuring instance count rules based on CPU/memory/HTTP metrics.

### **Monitoring and Logging**
- Enable **Application Insights** in the Azure Portal to track metrics like request rates, response times, and exceptions.
- Configure **Diagnostic Settings** for access logs, error logs, and failed request tracing.
- Use **Azure Monitor** and **Log Analytics** to query logs and set alerts.

## **Deployment**

To deploy the app to Azure App Service using Docker:

```bash
az login
az acr login --name fibonacciregistry
docker tag fibonacci-api fibonacciregistry.azurecr.io/fibonacci-api
docker push fibonacciregistry.azurecr.io/fibonacci-api
az appservice plan create --name fibonacciAppPlan --resource-group fibonacciresource --is-linux --sku B1
az webapp create --resource-group fibonacciresource --plan fibonacciAppPlan --name fiboapp --deployment-container-image-name fibonacciregistry.azurecr.io/fibonacci-api
az webapp config container set --name fiboapp --resource-group fibonacciresource --docker-custom-image-name fibonacciregistry.azurecr.io/fibonacci-api --docker-registry-server-url https://fibonacciregistry.azurecr.io
```

**For official documentation on deploying Docker containers to Azure App Service:  **
**[Azure App Service Documentation](https://learn.microsoft.com/en-us/azure/app-service)**

