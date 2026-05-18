from django.shortcuts import render
import datetime

def home(request):
    count = request.session.get("visit_count", 0) + 1
    request.session["visit_count"] = count
    context = {
        # TODO: Add "page_title", "heading", and "server_time" keys
        # server_time should be datetime.datetime.now()
        "page_title" : "Cool Home Page",
        "heading" : f"Welcome to my site! This session visit count: {count} !",
        "server_time" : datetime.datetime.now()
    }
    return render(request, "pages/home.html", context)

def about(request):
    skills = ["Python", "HTTP", "HTML", "CSS"]
    return render(request, "pages/about.html", {"skills": skills})

def greet(request, name):
    message = ""
    if request.method == "POST":
        note = request.POST.get("note")
        message = f'Thanks, {name}! Your note: "{note}"'
    return render(request, "pages/greet.html", {"name": name, "message": message})
    
ALL_PROJECTS = [
    {"name": "Socket Server",    "lang": "Python",     "year": 2025, "done": True},
    {"name": "HTML Profile",     "lang": "HTML",       "year": 2025, "done": True},
    {"name": "CSS Layout",       "lang": "CSS",        "year": 2025, "done": True},
    {"name": "Django App",       "lang": "Python",     "year": 2025, "done": False},
    {"name": "REST API",         "lang": "Python",     "year": 2024, "done": True},
    {"name": "React Dashboard",  "lang": "JavaScript", "year": 2024, "done": True},
    {"name": "SQL Queries Lab",  "lang": "SQL",        "year": 2024, "done": True},
    {"name": "CLI Tool",         "lang": "Python",     "year": 2023, "done": True},
]

def projects(request):
    q = request.GET.get("q", "").strip()
    # TODO: if q is non-empty, filter ALL_PROJECTS so only entries whose name
    #       or lang contains q (case-insensitive) are kept; otherwise show all
    if q:
        project_list = [
            p for p in ALL_PROJECTS
            if q.lower() in p["name"].lower()
            or q.lower() in p["lang"].lower()
        ]
    else:
        project_list = ALL_PROJECTS 
        
    done_count = sum(1 for p in ALL_PROJECTS if p["done"] is True)
    context = {
        # TODO: pass project_list, done_count, and q
        "project_list": project_list,
        "done_count": done_count,
        "q": q
    }
    return render(request, "pages/projects.html", context)

def api_demo(request):
    return render(request, "pages/api_demo.html")
