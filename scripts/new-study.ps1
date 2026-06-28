<#
.SYNOPSIS
  Mount a new study project from the datavidence template in one command.

.DESCRIPTION
  Wraps the full bootstrap so each new study is a single invocation:
    1. copier copy (non-interactive, with your answers)
    2. git init -b main + first commit
    3. (optional) make setup to restore the analysis environment

  Written for Windows PowerShell 5.1 (no '&&'); also runs on PowerShell 7+.

.PARAMETER Name
  Human-readable project name (required). Example: "RIE Mortality Cohort".

.PARAMETER Dest
  Destination folder for the new project (required). Created if missing.

.PARAMETER Stack
  Analysis stack: r | python | none. Default: r.

.PARAMETER Knowledge
  Knowledge retrieval coupling: none | hybrid | graph. Default: none.

.PARAMETER TemplateSource
  Copier template source. Default: the published GitHub template.
  Use a local path (e.g. "C:\workspace\datavidence-template-project") to test
  unreleased template changes.

.PARAMETER Setup
  If supplied, also runs 'make setup' in the new project (needs make + the stack toolchain).

.EXAMPLE
  .\scripts\new-study.ps1 -Name "RIE Mortality Cohort" -Dest "C:\workspace\rie-mortality"

.EXAMPLE
  .\scripts\new-study.ps1 -Name "Quick Test" -Dest "C:\tmp\qt" -Stack python -TemplateSource "C:\workspace\datavidence-template-project"
#>
[CmdletBinding()]
param(
  [Parameter(Mandatory = $true)] [string] $Name,
  [Parameter(Mandatory = $true)] [string] $Dest,
  [ValidateSet('r', 'python', 'none')] [string] $Stack = 'r',
  [ValidateSet('none', 'hybrid', 'graph')] [string] $Knowledge = 'none',
  [string] $TemplateSource = 'gh:psotob91/datavidence-template-project',
  [switch] $Setup
)

$ErrorActionPreference = 'Stop'

function Require-Cmd($cmd, $hint) {
  if (-not (Get-Command $cmd -ErrorAction SilentlyContinue)) {
    throw "'$cmd' not found on PATH. $hint"
  }
}

Require-Cmd copier "Install with: pipx install copier  (or: uv tool install copier)"
Require-Cmd git    "Install Git for Windows: https://git-scm.com/download/win"

Write-Host "==> Generating '$Name' ($Stack stack, knowledge=$Knowledge) into $Dest" -ForegroundColor Cyan
# --vcs-ref=HEAD: render the committed tip, NOT the latest git tag. Copier defaults
# to the newest tag; this factory ships from `main` without per-change release tags,
# so the default would render a stale snapshot (e.g. the old v0.1.0). HEAD renders
# the current template for both the gh: source and a local path.
copier copy --defaults --vcs-ref=HEAD `
  --data project_name="$Name" `
  --data analysis_stack=$Stack `
  --data knowledge_retrieval=$Knowledge `
  $TemplateSource $Dest
if ($LASTEXITCODE -ne 0) { throw "copier copy failed (exit $LASTEXITCODE)." }

Write-Host "==> git init + first commit" -ForegroundColor Cyan
Push-Location $Dest
try {
  git init -b main | Out-Null
  git add -A
  git commit -m "chore: init '$Name' from datavidence template" | Out-Null

  if ($Setup) {
    Require-Cmd make "Install make, or run 'make setup' later by hand."
    Write-Host "==> make setup" -ForegroundColor Cyan
    make setup
  }
}
finally {
  Pop-Location
}

Write-Host ""
Write-Host "Done. Follow the setup card (it has the exact order, DO/DON'T):" -ForegroundColor Green
Write-Host "  $Dest\docs\SETUP.md"
Write-Host ""
Write-Host "Quick version:" -ForegroundColor Green
Write-Host "  cd `"$Dest`"; claude        # Claude Code auto-loads CLAUDE.md. Do NOT run /init."
if (-not $Setup) { Write-Host "  make setup                 # restore the analysis environment" }
Write-Host "  # Cowork? In Code run /psotobverse-utils:sync-cowork, then paste .claude/COWORK_INSTRUCTIONS.md into Cowork."
