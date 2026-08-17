#!/usr/bin/env python3

import argparse
import gzip
import shutil
import subprocess
from pathlib import Path

parser = argparse.ArgumentParser(
    description="Download files from a tab-separated list of URLs and output prefixes."
)
parser.add_argument(
    "input_file",
    help="Tab-separated file containing: URL<TAB>output_prefix"
)

args = parser.parse_args()

with open(args.input_file) as f:
    for line in f:
        line = line.strip()

        # Skip blank lines and comments
        if not line or line.startswith("#"):
            continue

        try:
            url, prefix = line.split("\t")
        except ValueError:
            print(f"Skipping invalid line:\n{line}")
            continue

        filename = Path(url).name
        suffixes = "".join(Path(filename).suffixes)

        outfile = prefix + suffixes

        print(f"\nDownloading {outfile}")
        subprocess.run(
            ["wget", "-c", "-O", outfile, url],
            check=True
        )

        # Uncompress .gz files (except .tar.gz)
        if outfile.endswith(".gz") and not outfile.endswith(".tar.gz"):
            extracted = outfile[:-3]
            print(f"Extracting {extracted}")

            with gzip.open(outfile, "rb") as fin, open(extracted, "wb") as fout:
                shutil.copyfileobj(fin, fout)

            Path(outfile).unlink()

print("\nAll downloads completed.")
