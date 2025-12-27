import time
import subprocess

def main_loop():
    while True:
        print("[Operator] Task Loop gestartet...")
        result = subprocess.run("docker --version", shell=True, capture_output=True, text=True)
        print(result.stdout)
        time.sleep(30)

if __name__ == "__main__":
    main_loop()
