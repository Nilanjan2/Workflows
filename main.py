from datetime import datetime
now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

with open("last_run.txt", "w") as f:
    f.write(f"Last run: {now}\n")

print(f"Updated last_run.txt with: {now}")
