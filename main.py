import os

ENTRY = "Sorry I'm late - I spent the deadline window retraining myself on punctuality, and the model converged on a bold new insight: the deadline was technically still in the future until it wasn't."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
