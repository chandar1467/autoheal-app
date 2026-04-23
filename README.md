# 🚀 Smart Auto-Healing Web Application

### Using Docker & Kubernetes

---

## 📌 Project Overview

This project demonstrates a **containerized web application** deployed using **Docker and Kubernetes** with an **auto-healing mechanism**.

The application is designed to automatically recover from failures using Kubernetes **liveness probes**, ensuring high availability and reliability.

---

## 🛠️ Technologies Used

* 🐳 Docker
* ☸️ Kubernetes (k3s)
* 🐍 Python (Flask)
* 🖥️ WSL (Ubuntu)

---

## ⚙️ Features

* Containerized web application
* Kubernetes Deployment & Service
* Auto-healing using liveness probes
* Crash simulation endpoint (`/crash`)
* Self-recovery without manual intervention

---

## 📂 Project Structure

```
autoheal-app/
│── app.py
│── Dockerfile
│── deployment.yaml
│── service.yaml
│── README.md
```

---

## 🚀 How to Run the Project

### 1️⃣ Start Docker

```bash
sudo service docker start
```

### 2️⃣ Set Kubernetes config

```bash
sudo chmod 644 /etc/rancher/k3s/k3s.yaml
export KUBECONFIG=/etc/rancher/k3s/k3s.yaml
```

### 3️⃣ Build Docker Image

```bash
docker build -t autoheal-app .
```

### 4️⃣ Import Image to Kubernetes

```bash
docker save autoheal-app -o autoheal.tar
sudo k3s ctr images import autoheal.tar
```

### 5️⃣ Deploy Application

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

### 6️⃣ Check Pods

```bash
kubectl get pods
```

---

## 🌐 Access the Application

Find your WSL IP:

```bash
ip addr show eth0
```

Open in browser:

```
http://<your-ip>:30007
```

---

## 💥 Test Auto-Healing

Open:

```
http://<your-ip>:30007/crash
```

Then monitor:

```bash
kubectl get pods -w
```

---

## 🔄 Auto-Healing Explanation

When the `/crash` endpoint is triggered:

1. Application crashes ❌
2. Kubernetes detects failure 🔍
3. Pod restarts automatically 🔁
4. Application becomes available again ✅

---

## 🎯 Output

* Web page displays:
  **"Auto-Healing App Running!"**

* Crash endpoint triggers recovery:

  * Pod restarts automatically
  * No manual intervention required

---

## 🧠 Learning Outcomes

* Understanding of containerization using Docker
* Deployment using Kubernetes
* Implementation of self-healing systems
* Basics of DevOps workflow

---

## 📌 Conclusion

This project successfully demonstrates how Kubernetes ensures **high availability** through **auto-healing mechanisms**, making applications more reliable in real-world environments.

---

## 👨‍💻 Author

**Chandar Gandrathi**
GitHub: https://github.com/chandar1467

---
