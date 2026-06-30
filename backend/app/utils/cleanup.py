from pathlib import Path


def cleanup_logs():

    log_dir = Path("logs")

    if not log_dir.exists():
        return

    for file in log_dir.glob("*.log"):

        if file.stat().st_size > 50 * 1024 * 1024:
            file.unlink()