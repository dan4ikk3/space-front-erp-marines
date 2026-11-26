#!/usr/bin/env python3
import subprocess
import sys

REPO = "https://github.com/RMC-14/RMC-14.git"
SHA_FILE = "Tools/upstream-rmc14.sha"
SKIP = [
    "RobustToolbox", "RSI.NET", ".gitmodules", ".github", ".vscode", "Modifications",
    "README.md", "PATCHES.md", "ИЗМЕНЕНИЯ.md", "LICENSE-SPACE-FRONT.txt",
]


def git(*args, check=True):
    return subprocess.run(["git", *args], check=check, capture_output=True, text=True)


def main():
    base = open(SHA_FILE).read().strip()
    git("remote", "remove", "rmc", check=False)
    git("remote", "add", "rmc", REPO)
    print("Загружаю RMC-14 master...")
    git("fetch", "--no-tags", "--filter=blob:none", "rmc", "master")
    new = git("rev-parse", "rmc/master").stdout.strip()
    if new == base:
        print("Новых изменений нет")
        return 0
    branch = f"upstream-rmc14-{new[:10]}"
    git("checkout", "-b", branch)
    diff = git("diff", "--binary", base, new, "--", ".", *[f":!{p}" for p in SKIP]).stdout
    with open("upstream.patch", "w", encoding="utf-8", newline="\n") as f:
        f.write(diff)
    result = git("apply", "--3way", "--whitespace=nowarn", "upstream.patch", check=False)
    print(result.stderr)
    with open(SHA_FILE, "w") as f:
        f.write(new + "\n")
    print(f"Ветка {branch}. База теперь {new[:10]}.")
    if result.returncode != 0:
        print("Есть конфликты: найди маркеры <<<<<<< и поправь вручную, затем git add -A && git commit")
    else:
        print("Конфликтов нет: проверь git status и сделай коммит")
    return 0


sys.exit(main())
