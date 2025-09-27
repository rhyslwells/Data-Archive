---
aliases: []
category: DEVOPS
date modified: 27-09-2025
tags:
- system
---
You can save that [[PowerShell]] command as a `.ps1` ([[ps1]]) script file and run it on Windows using PowerShell.
## Example
### Save as a PowerShell Script

1. Open a text editor (e.g., VS Code, Notepad++)
2. Paste the code below into a new file:
```powershell
$themes = "black", "white", "league", "beige", "sky", "night", "serif", "simple", "solarized", "blood", "moon"
foreach ($theme in $themes) {
  jupyter nbconvert presentation.ipynb --to slides --SlidesExporter.reveal_theme=$theme --output "presentation_$theme"
}
```
3. Save the file as:
```
convert-themes.ps1
```

## How to Run the Script

1. Open PowerShell
2. Navigate to the script’s directory:
```powershell
cd "C:\path\to\your\script"
```
3. Run the script:
```powershell
.\convert-themes.ps1
```