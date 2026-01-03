<#
.SYNOPSIS
    Scan the SQLi-Labs test directory for security vulnerabilities.

.DESCRIPTION
    Runs the security scanning pipeline against the test/sqli-labs directory
    and generates reports in reports/test-sqli-labs/.

.PARAMETER NoLLM
    Disable LLM-based remediation (uses templates instead, faster).

.PARAMETER Quiet
    Suppress progress output.

.EXAMPLE
    .\scan-test-labs.ps1
    Runs the full scan with LLM remediation.

.EXAMPLE
    .\scan-test-labs.ps1 -NoLLM
    Runs a quick scan without LLM (uses template-based remediation).
#>

param(
    [switch]$NoLLM,
    [switch]$Quiet
)

$ErrorActionPreference = "Stop"

# Get project paths
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$ProjectRoot = Split-Path -Parent $ScriptDir
$SrcDir = Join-Path $ProjectRoot "src"
$TargetPath = Join-Path $ProjectRoot "test"
$OutputDir = Join-Path $ProjectRoot "reports" "test-sqli-labs"

# Verify paths exist
if (-not (Test-Path $TargetPath)) {
    Write-Error "Target path not found: $TargetPath"
    exit 1
}

if (-not (Test-Path $SrcDir)) {
    Write-Error "Source directory not found: $SrcDir"
    exit 1
}

# Build Python command arguments
$PythonArgs = @(
    "-m", "pipeline.main",
    $TargetPath,
    "--output-dir", $OutputDir
)

if ($NoLLM) {
    $PythonArgs += "--no-llm"
}

if ($Quiet) {
    $PythonArgs += "--quiet"
}

# Run the pipeline from src directory
Write-Host "Starting security scan of test directory..."
Write-Host "Target: $TargetPath"
Write-Host "Output: $OutputDir"
Write-Host ""

Push-Location $SrcDir
try {
    python @PythonArgs
    $exitCode = $LASTEXITCODE
} finally {
    Pop-Location
}

if ($exitCode -eq 0) {
    Write-Host ""
    Write-Host "Scan completed successfully!"
    Write-Host "Reports available at:"
    Write-Host "  - $OutputDir\findings.json"
    Write-Host "  - $OutputDir\report.md"
} else {
    Write-Error "Scan failed with exit code: $exitCode"
}

exit $exitCode
