import os
from dotenv import load_dotenv

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

GITHUB_OWNER = os.getenv("GITHUB_OWNER")
GITHUB_REPO = os.getenv("GITHUB_REPO")

GITHUB_ISSUES_LIMIT = int(os.getenv("GITHUB_ISSUES_LIMIT", "100"))
CLAUDE_MODEL = os.getenv("CLAUDE_MODEL", "claude-opus-4-7")
CLAUDE_MAX_TOKENS = int(os.getenv("CLAUDE_MAX_TOKENS", "20000"))