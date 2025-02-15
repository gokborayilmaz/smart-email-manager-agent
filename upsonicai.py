import os
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv
from upsonic import Agent, Task, ObjectResponse

# Load environment variables
load_dotenv()

app = FastAPI(title="Smart Email Manager Agent")

# Initialize the AI agent
email_agent = Agent("Smart Email Manager", model="azure/gpt-4o", reflection=True)

# Define response formats
class EmailSummary(ObjectResponse):
    summary: str

class EmailTasks(ObjectResponse):
    tasks: list[str]

class EmailEvents(ObjectResponse):
    events: list[str]

class EmailReply(ObjectResponse):
    suggested_reply: str

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Smart Email Manager</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-gray-100 flex justify-center items-center h-screen">
        <div class="bg-white p-8 rounded-lg shadow-lg w-[40rem]">
            <h1 class="text-2xl font-bold text-center mb-4">📩 Smart Email Manager</h1>
            <textarea id="email_content" placeholder="Paste your email here..." class="w-full p-2 border rounded mb-4 h-32"></textarea>
            <button onclick="analyzeEmail()" class="bg-blue-500 text-white px-4 py-2 rounded w-full">Analyze Email</button>
            <div id="result" class="mt-4 text-sm text-gray-800 bg-gray-50 p-4 rounded overflow-y-auto h-64"></div>
        </div>
        <script>
            async function analyzeEmail() {
                const emailContent = document.getElementById("email_content").value;
                if (!emailContent) {
                    alert("Please enter an email content.");
                    return;
                }
                const response = await fetch(`/analyze_email?email=${encodeURIComponent(emailContent)}`);
                const data = await response.json();
                document.getElementById("result").innerText = JSON.stringify(data, null, 2);
            }
        </script>
    </body>
    </html>
    """

@app.get("/analyze_email")
async def analyze_email(email: str = Query(..., title="Email content")):
    """Analyzes an email and extracts useful information."""
    try:
        # Task 1: Generate summary
        summary_task = Task(
            f"Summarize the following email: {email}",
            response_format=EmailSummary
        )
        email_agent.do(summary_task)
        
        # Task 2: Extract tasks from the email
        tasks_task = Task(
            f"Identify any action items in the following email: {email}",
            response_format=EmailTasks
        )
        email_agent.do(tasks_task)
        
        # Task 3: Extract date/time events from the email
        events_task = Task(
            f"Extract any meetings, events, or deadlines from this email: {email}",
            response_format=EmailEvents
        )
        email_agent.do(events_task)
        
        # Task 4: Suggest a reply if needed
        reply_task = Task(
            f"If a response is needed, draft a professional reply for this email: {email}",
            response_format=EmailReply
        )
        email_agent.do(reply_task)
        
        return {
            "summary": summary_task.response.summary,
            "tasks": tasks_task.response.tasks,
            "events": events_task.response.events,
            "suggested_reply": reply_task.response.suggested_reply
        }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)