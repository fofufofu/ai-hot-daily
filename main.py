import requests
import json
from datetime import datetime
from collections import Counter

# Simple RSS feed fetcher (using GitHub trending as source)
GITHUB_TRENDING_URL = "https://github.com/trending?since=daily"


def fetch_trending_repos():
    # Mock: In real implementation, parse HTML or use API. Here we simulate.
    repos = ["AIHOT", "lint", "rune", "screenwriting-skills", "ai-engineering-interview-questions-company-wise"]
    return repos


def summarize_repos(repos):
    # Mock LLM call: Extract keywords and generate summary
    all_text = " ".join(repos).lower()
    keywords = [w for w in all_text.split() if len(w) > 4]
    common = Counter(keywords).most_common(5)
    date_str = datetime.now().strftime("%Y-%m-%d")
    summary_lines = [f"Daily AI Trend Report - {date_str}", "Top keywords: " + ", ".join([k for k, _ in common])]
    for repo in repos[:5]:
        summary_lines.append(f"- {repo}")
    return "\n".join(summary_lines)


def main():
    print("Fetching trending repos...")
    repos = fetch_trending_repos()
    print("Generating summary...")
    summary = summarize_repos(repos)
    print(summary)

if __name__ == "__main__":
    main()
