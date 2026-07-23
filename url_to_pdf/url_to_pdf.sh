#!/usr/bin/env bash

set -euo pipefail

# Check dependency
if ! command -v wkhtmltopdf >/dev/null 2>&1; then
    echo "Error: wkhtmltopdf is not installed."
    echo "Install it with: sudo apt install wkhtmltopdf"
    exit 1
fi

# Prompt for URL
read -rp "Enter the URL: " url

# Basic validation
if [[ -z "$url" ]]; then
    echo "Error: URL cannot be empty."
    exit 1
fi

if [[ ! "$url" =~ ^https?:// ]]; then
    echo "Error: URL must start with http:// or https://"
    exit 1
fi

# Prompt for output filename
read -rp "Enter output PDF name (leave blank for auto): " output_file

# Auto-generate filename if blank
if [[ -z "${output_file}" ]]; then
    domain=$(echo "$url" | awk -F/ '{print $3}' | sed 's/[^a-zA-Z0-9._-]/_/g')
    timestamp=$(date +"%Y%m%d_%H%M%S")
    output_file="${domain}_${timestamp}.pdf"
fi

# Make sure it ends in .pdf
if [[ "$output_file" != *.pdf ]]; then
    output_file="${output_file}.pdf"
fi

echo "Converting page to PDF..."
wkhtmltopdf "$url" "$output_file"

echo "Done. Saved as: $output_file"
