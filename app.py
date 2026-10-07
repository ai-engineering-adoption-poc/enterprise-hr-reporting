def workforce_summary():
    employees = [
        {"department": "Engineering", "count": 42},
        {"department": "Operations", "count": 18},
    ]
    return {"departments": employees, "source": "synthetic_demo_data"}

if __name__ == "__main__":
    print(workforce_summary())
