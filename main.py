"""Write the funniest toaster error message to the output file."""

import os

LINE = "ERROR 04: BREAD STUCK. I HAVE EATEN IT. THERE WILL BE NO REFUND."
# Exactly 64 characters, no trailing newline: the file is the line itself.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
