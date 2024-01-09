from pathlib import Path
import subprocess
import time


ROOT = Path(__file__).parent


if __name__ == '__main__':
    prev_files = None

    while True:
        files = {
            path: path.stat().st_mtime
            for path in ROOT.rglob("*.py")
        }
            
        if prev_files != files:
            print("Modified...")

            try:
                start = time.time()
                subprocess.check_call(["python", str(ROOT / "main.py")], cwd=ROOT)
                end = time.time()
                print(f"    Done [{end-start:.02f}sec]")


            except subprocess.CalledProcessError:
                print("    Failed !!")

            prev_files = files
            
        time.sleep(0.5)