# Bulk File Downloader & Decompressor

A lightweight Python command-line utility for **batch downloading files from URLs** using a tab-separated input file. It automatically preserves file extensions and decompresses `.gz` files after download.

## Features

* 📥 Batch download multiple files using `wget`
* 📋 Simple `URL<TAB>output_prefix` input format
* ⏭️ Skips blank lines, comments, and malformed entries
* 🔄 Supports resumable downloads with `wget -c`
* 📦 Automatically decompresses `.gz` files
* 🚫 Keeps `.tar.gz` archives compressed
* 🧹 Removes the original `.gz` file after successful extraction

## Usage

```bash
python3 download_files.py input.txt
```

### Input format

```text
https://example.com/genome.fasta.gz    sample_genome
https://example.com/annotation.gff.gz  sample_annotation
```

## Output:

```text
sample_genome.fasta
sample_annotation.gff
```

For `.tar.gz` files, the archive remains unchanged.

## Requirements

* Python 3
* `wget`

### Python modules

Uses only Python standard-library modules:

`argparse` · `gzip` · `shutil` · `subprocess` · `pathlib`

## Workflow

**Read URLs → Download → Preserve extensions → Decompress `.gz` → Clean up**

A simple utility for automating repetitive **bioinformatics data-download workflows**.
