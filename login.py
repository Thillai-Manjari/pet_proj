import uvicorn

n = eval(input("Enter 1 if you are a student \nEnter 2 if you are a teacher\n"))

if(n==1):
    if __name__ == "__main__":
        uvicorn.run("main2:app", host="127.0.0.1", port=8000, log_level="info")

else:
   if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")
