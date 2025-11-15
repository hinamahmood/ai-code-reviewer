import git
import tempfile
from app.ai_client import ask_ai

def analyze_repository(url: str):
    temp_dir = tempfile.mkdtemp()
    git.Repo.clone_from(url, temp_dir)

    result = ask_ai(f"Analyze this repository: {url}")
    return {"repo": url, "analysis": result}
