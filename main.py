import os

TEXT = """Someone carries you up the stairs the way they always have.
Your cheek finds the shoulder that knows your weight.
Below, the house settles. The kettle ticks itself cool.
Above the roof, the stars hold their slow, old watch,
and the arms around you do not let go."""

def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
