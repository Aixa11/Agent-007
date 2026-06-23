param(
  [string]$Root = (Resolve-Path "$PSScriptRoot\..").Path
)

$ErrorActionPreference = "Stop"

$issues = New-Object System.Collections.Generic.List[string]

function Add-Issue([string]$Message) {
  $issues.Add($Message) | Out-Null
}

$requiredFiles = @(
  "AGENTS.md",
  "agent\rules.md",
  "blueprint\docs\architecture.md",
  "README.md",
  "README.en.md",
  "docs\vision.md",
  "docs\scope.md",
  "docs\roadmap.md"
)

foreach ($file in $requiredFiles) {
  $path = Join-Path $Root $file
  if (!(Test-Path $path)) {
    Add-Issue "Missing required file: $file"
  }
}

$requiredDirs = @(
  "agent",
  "agent\prompts",
  "agent\workflows",
  "blueprint",
  "blueprint\docs",
  "blueprint\modules",
  "blueprint\policies",
  "validation",
  "validation\schema",
  "examples",
  "examples\oil-pipeline",
  "tests"
)

foreach ($dir in $requiredDirs) {
  $path = Join-Path $Root $dir
  if (!(Test-Path $path)) {
    Add-Issue "Missing required directory: $dir"
  }
}

$requiredPromptFiles = @(
  "agent\prompts\analyze_infra.md",
  "agent\prompts\improve_incrementally.md",
  "agent\prompts\validate_changes.md",
  "agent\prompts\security_review.md",
  "agent\prompts\architecture_summary.md"
)

foreach ($file in $requiredPromptFiles) {
  $path = Join-Path $Root $file
  if (!(Test-Path $path)) {
    Add-Issue "Missing prompt file: $file"
  }
}

$requiredWorkflowFiles = @(
  "agent\workflows\analyze.md",
  "agent\workflows\propose.md",
  "agent\workflows\validate.md",
  "agent\workflows\publish.md"
)

foreach ($file in $requiredWorkflowFiles) {
  $path = Join-Path $Root $file
  if (!(Test-Path $path)) {
    Add-Issue "Missing workflow file: $file"
  }
}

$requiredModuleFiles = @(
  "blueprint\modules\README.md",
  "blueprint\modules\network\README.md",
  "blueprint\modules\security\README.md",
  "blueprint\modules\compute\README.md",
  "blueprint\modules\storage\README.md"
)

foreach ($file in $requiredModuleFiles) {
  $path = Join-Path $Root $file
  if (!(Test-Path $path)) {
    Add-Issue "Missing blueprint module file: $file"
  }
}

$requiredPolicyFiles = @(
  "blueprint\policies\iam-baseline.yaml",
  "blueprint\policies\logging-baseline.yaml",
  "blueprint\policies\encryption-baseline.yaml"
)

foreach ($file in $requiredPolicyFiles) {
  $path = Join-Path $Root $file
  if (!(Test-Path $path)) {
    Add-Issue "Missing policy file: $file"
  }
}

$schemaPath = Join-Path $Root "validation\schema\finding.schema.json"
if (!(Test-Path $schemaPath)) {
  Add-Issue "Missing schema file: validation/schema/finding.schema.json"
}

$examplePath = Join-Path $Root "examples\oil-pipeline\README.md"
if (!(Test-Path $examplePath)) {
  Add-Issue "Missing example file: examples/oil-pipeline/README.md"
}

$testsPath = Join-Path $Root "tests"
if (Test-Path $testsPath) {
  $testFiles = Get-ChildItem -Path $testsPath -File -ErrorAction SilentlyContinue
  if ($testFiles.Count -eq 0) {
    Add-Issue "The tests directory exists but does not contain any files."
  }
}

$agentsPath = Join-Path $Root "AGENTS.md"
if (Test-Path $agentsPath) {
  $content = Get-Content $agentsPath -Raw
  if ($content -notmatch "Commands") {
    Add-Issue "AGENTS.md should include a Commands section."
  }
  if ($content -notmatch "Boundaries") {
    Add-Issue "AGENTS.md should include a Boundaries section."
  }
}

$rulePath = Join-Path $Root "agent\rules.md"
if (Test-Path $rulePath) {
  $content = Get-Content $rulePath -Raw
  if ($content -notmatch "Incremental evolution") {
    Add-Issue "agent/rules.md should include incremental evolution guidance."
  }
  if ($content -notmatch "Data sovereignty") {
    Add-Issue "agent/rules.md should include data sovereignty guidance."
  }
}

if ($issues.Count -gt 0) {
  Write-Host "Validation failed:"
  $issues | ForEach-Object { Write-Host "- $_" }
  exit 1
}

Write-Host "Validation passed."
exit 0