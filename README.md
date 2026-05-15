# Fake Store API Data Pipeline

โปรเจกต์นี้เป็นการสร้างระบบ ETL (Extract, Transform, Load) Pipeline สำหรับดึงข้อมูลสินค้าออนไลน์จาก REST API โดยใช้ Apache Airflow ในการควบคุม workflow ผ่าน DAG และใช้ PostgreSQL สำหรับจัดเก็บข้อมูล

ระบบถูกออกแบบให้อยู่ใน Docker Environment เพื่อให้สามารถติดตั้งและใช้งานได้ง่าย

---

# จุดประสงค์ของโปรเจกต์

โปรเจกต์นี้ถูกพัฒนาขึ้นเพื่อศึกษาแนวคิดของ Data Engineering และ Data Pipeline โดยมีการทำงานแบบอัตโนมัติ ตั้งแต่การดึงข้อมูล การแปลงข้อมูล และโหลดข้อมูลเข้าสู่ฐานข้อมูล

---

# Architecture ของระบบ

```text
Fake Store API
        ↓
Apache Airflow DAG
        ↓
Raw JSON Storage
        ↓
Data Transformation (Pandas)
        ↓
PostgreSQL Database
```

---

# อธิบายการทำงานของระบบ

## 1. Extract Process

ระบบจะดึงข้อมูลสินค้าจาก Fake Store API ผ่าน REST API

ข้อมูลที่ดึงได้ เช่น:
- ชื่อสินค้า
- ราคา
- หมวดหมู่สินค้า
- คะแนน Rating

ตัวอย่าง API:

https://fakestoreapi.com/products

ข้อมูลที่ได้จะถูกจัดเก็บเป็นไฟล์ JSON ในโฟลเดอร์:

```text
raw_data/
```

---

## 2. Transform Process

หลังจากได้ข้อมูลดิบ ระบบจะใช้ Pandas ในการแปลงข้อมูลให้อยู่ในรูปแบบที่เหมาะสมสำหรับการวิเคราะห์

สิ่งที่ทำในขั้นตอนนี้:
- เลือกเฉพาะ columns ที่จำเป็น
- แปลง nested JSON
- จัดรูปแบบข้อมูล
- ลบข้อมูลที่เป็น null

ข้อมูลที่ถูกแปลงแล้วจะถูกบันทึกเป็นไฟล์ CSV ในโฟลเดอร์:

```text
transformed/
```

---

## 3. Load Process

ระบบจะโหลดข้อมูลที่ผ่านการ transform แล้วเข้าสู่ PostgreSQL Database

ตารางที่ใช้:

```text
products
```

โดยข้อมูลจะถูก insert ผ่าน SQLAlchemy

---

# การใช้ Apache Airflow

โปรเจกต์นี้ใช้ Apache Airflow สำหรับควบคุมลำดับการทำงานของ ETL Pipeline ผ่าน DAG (Directed Acyclic Graph)

DAG Workflow:

```text
extract_products
        ↓
transform_products
        ↓
load_products
```

รายละเอียดแต่ละ Task:
- extract_products → ดึงข้อมูลจาก API
- transform_products → แปลงและ clean data
- load_products → โหลดข้อมูลเข้าสู่ PostgreSQL

---

# เทคโนโลยีที่ใช้

| Technology | Description |
|---|---|
| Python | ใช้พัฒนา ETL Scripts |
| Apache Airflow | ใช้ orchestrate workflow |
| Docker | ใช้ containerize ระบบ |
| Docker Compose | ใช้จัดการหลาย containers |
| PostgreSQL | ใช้จัดเก็บข้อมูล |
| Pandas | ใช้ transform data |
| SQLAlchemy | ใช้เชื่อมต่อ database |

---

# โครงสร้างโปรเจกต์

```text
fake_store_pipeline/
│
├── dags/
│   └── ecommerce_pipeline_dag.py
│
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── raw_data/
├── transformed/
│
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .gitignore
```

---

# วิธีการใช้งาน

## 1. Start Docker Containers

รันคำสั่ง:

```bash
docker compose up -d
```

---

## 2. เปิด Airflow UI

เข้าใช้งานผ่าน browser:

```text
http://localhost:8080
```

---

## 3. Login Airflow

Username:

```text
airflow
```

Password:

```text
airflow
```

---

## 4. เปิดใช้งาน DAG

DAG Name:

```text
ecommerce_pipeline
```

จากนั้นกด:
- Turn ON DAG
- Trigger DAG

---

# PostgreSQL Connection

| Field | Value |
|---|---|
| Host | localhost |
| Port | 5432 |
| Username | airflow |
| Password | airflow |
| Database | ecommerce_db |

---

# ตัวอย่าง SQL Query

## ดูข้อมูลทั้งหมด

```sql
SELECT * FROM products;
```

---

## ดูสินค้าราคาแพงที่สุด

```sql
SELECT title, price
FROM products
ORDER BY price DESC
LIMIT 5;
```

---

## ดูสินค้าที่ rating สูงที่สุด

```sql
SELECT title, rating
FROM products
ORDER BY rating DESC
LIMIT 5;
```

---

# จุดเด่นของโปรเจกต์

- มี ETL Pipeline แบบอัตโนมัติ
- ใช้ Apache Airflow DAG จริง
- ใช้ REST API จริง
- ใช้ Docker Environment
- มีการจัดเก็บ Raw Data
- มี Data Transformation
- ใช้ PostgreSQL Database

---

# สรุป

โปรเจกต์นี้เป็นตัวอย่างของ Data Pipeline สำหรับงานด้าน Data Engineering โดยใช้ Apache Airflow ควบคุม ETL Workflow ตั้งแต่การดึงข้อมูลจาก API การจัดเก็บข้อมูลดิบ การแปลงข้อมูล และโหลดเข้าสู่ฐานข้อมูล PostgreSQL ภายใน Docker Environment แบบอัตโนมัติ

---
