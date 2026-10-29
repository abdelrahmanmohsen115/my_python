from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import csv

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/register")
async def register(
    full_name: str = Form(...),
    phone: int = Form(...),
    email: str = Form(...),
    password: int = Form(...),
    city: str = Form(...)
):
    headers = ["Name", "Phone", "Email", "Password", "City"]
    user_data = [full_name, phone, email, password, city]

  
    with open("users.csv", mode="a", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)

        if file.tell() == 0:
            writer.writerow(headers)

        writer.writerow(user_data)

    print("The data has been successfully saved to the users.csv file!")
 
    return FileResponse("done.html")
    #python -m uvicorn ahmad:app --reloadده الامر اللي قي (run)
    #python -m uvicorn forget:app --reload