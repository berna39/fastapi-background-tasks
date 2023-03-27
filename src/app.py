from fastapi import FastAPI, BackgroundTasks
from services.mailing import do_send_mail

app = FastAPI()

@app.get("/")
async def root():
    return { "message": "Hello from the other side" }

@app.get("/send-mail")
async def send_mail():
    do_send_mail("destination@domain.com", "A random subject", "hello from the other side")

    return { "message": "The mail has been sent" }

@app.get("/send-bg-mail")
async def send_mail(backgroundTasks: BackgroundTasks):
    backgroundTasks.add_task(do_send_mail, "destination@domain.com", "A random subject", "hello from the other side")

    return { "message": "The mail has been sent" }
