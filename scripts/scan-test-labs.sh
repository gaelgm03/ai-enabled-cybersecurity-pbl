#!/bin/bash
#
# Scan the SQLi-Labs test directory for security vulnerabilities.
#
# Usage:
#   ./scan-test-labs.sh [OPTIONS]
#
# Options:
#   --no-llm    Disable LLM-based remediation (uses templates instead, faster)
#   --quiet     Suppress progress output
#
# Examples:
#   ./scan-test-labs.sh              # Full scan with LLM
#   ./scan-test-labs.sh --no-llm     # Quick scan without LLM
#

set -e

# Get project paths
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
SRC_DIR="$PROJECT_ROOT/src"
TARGET_PATH="$PROJECT_ROOT/test"
OUTPUT_DIR="$PROJECT_ROOT/reports/test-sqli-labs"

# Verify paths exist
if [ ! -d "$TARGET_PATH" ]; then
    echo "Error: Target path not found: $TARGET_PATH" >&2
    exit 1
fi

if [ ! -d "$SRC_DIR" ]; then
    echo "Error: Source directory not found: $SRC_DIR" >&2
    exit 1
fi

# Print info
echo "Starting security scan of test directory..."
echo "Target: $TARGET_PATH"
echo "Output: $OUTPUT_DIR"
echo ""

# Run the pipeline from src directory
cd "$SRC_DIR"
python -m pipeline.main "$TARGET_PATH" --output-dir "$OUTPUT_DIR" "$@"
EXIT_CODE=$?

if [ $EXIT_CODE -eq 0 ]; then
    echo ""
    echo "Scan completed successfully!"
    echo "Reports available at:"
    echo "  - $OUTPUT_DIR/findings.json"
    echo "  - $OUTPUT_DIR/report.md"
fi

exit $EXIT_CODE
