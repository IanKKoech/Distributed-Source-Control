import os
import shutil
import json
import hashlib
import datetime

REPO_DIR = ".myrepo"

class DistributedSourceControl:
    @staticmethod
    def init():
        """Initialize a repository in the current directory."""
        if os.path.exists(REPO_DIR):
            return "Repository already initialized."
        
        os.makedirs(f"{REPO_DIR}/commits", exist_ok=True)
        os.makedirs(f"{REPO_DIR}/staged", exist_ok=True)
        os.makedirs(f"{REPO_DIR}/branches", exist_ok=True)

        with open(f"{REPO_DIR}/log.txt", "w") as log_file:
            log_file.write("")
        with open(f"{REPO_DIR}/config.json", "w") as config_file:
            json.dump({"current_branch": "main"}, config_file)

        return "Initialized empty repository."

    @staticmethod
    def add(file_path):
        """Stage a file for commit."""
        if not os.path.exists(REPO_DIR):
            return "Repository not initialized."
        
        if not os.path.exists(file_path):
            return f"File '{file_path}' does not exist."

        staged_path = os.path.join(REPO_DIR, "staged", os.path.basename(file_path))
        shutil.copyfile(file_path, staged_path)
        return f"Staged file: {file_path}"

    @staticmethod
    def commit(message):
        """Commit the staged changes."""
        if not os.path.exists(REPO_DIR):
            return "Repository not initialized."
        
        staged_dir = os.path.join(REPO_DIR, "staged")
        if not os.listdir(staged_dir):
            return "No changes to commit."

        commit_id = hashlib.sha1(
            str(datetime.datetime.now()).encode()
        ).hexdigest()[:7]
        commit_dir = os.path.join(REPO_DIR, "commits", commit_id)
        os.makedirs(commit_dir, exist_ok=True)

        for file_name in os.listdir(staged_dir):
            shutil.move(os.path.join(staged_dir, file_name), os.path.join(commit_dir, file_name))

        with open(f"{REPO_DIR}/log.txt", "a") as log_file:
            log_file.write(f"{commit_id} {message}\n")

        return f"Committed changes: {commit_id} - {message}"

    @staticmethod
    def log():
        """View commit history."""
        if not os.path.exists(REPO_DIR):
            return "Repository not initialized."
        
        with open(f"{REPO_DIR}/log.txt", "r") as log_file:
            content = log_file.read().strip()
            return content if content else "No commits yet."
