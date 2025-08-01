---
aliases: []
category: DE
date modified: 27-07-2025
tags:
  - software
  - system
created: 2024-06-22 21:06
type:
---
PowerShell is a task automation and configuration management framework developed by Microsoft, consisting of a [[Command Line]] shell and an associated scripting language. It is designed to automate system administration tasks across local and remote Windows systems and, with PowerShell Core (now known as PowerShell 7+), across macOS and Linux as well.

Related:
- [[Command Prompt]]
- [[Powershell versus Command Prompt]]
- [[Powershell scripts]]


Object-Oriented Architecture: Unlike `cmd`, which handles plain text, PowerShell processes .[[NET]] objects. This allows for structured data manipulation and precise control of outputs. Example:
    
```powershell
Get-ChildItem | Select-Object Name, Length, LastWriteTime
```
    
Integrated with .[[NET]]: PowerShell scripts can invoke .NET classes and use assemblies directly. Example:
    
```powershell
[System.IO.File]::ReadAllText("C:\path\to\file.txt")
```

Cmdlets: PowerShell uses built-in, standardized command modules (cmdlets) for common tasks. These provide consistent naming and behavior, unlike the ad-hoc commands in `cmd`. Example:

```powershell
Restart-Service -Name "Spooler"
```

Advanced Scripting Support: Supports rich scripting constructs such as functions, conditionals, loops, and error handling. Example:

```powershell
if (Test-Path "file.txt") { Write-Output "Exists" } else { Write-Output "Missing" }
```

Pipeline with Objects: PowerShell supports object-based pipelines, enabling powerful command chaining and transformations.

Remote Management: PowerShell includes native support for remote system management via PowerShell Remoting (e.g., `Enter-PSSession`, `Invoke-Command`), a capability not present in `cmd`.

Cross-Platform Compatibility: PowerShell Core (now PowerShell 7+) runs on Windows, macOS, and Linux, while `cmd` is exclusive to Windows.

Built-in Help System: Use `Get-Help` to access comprehensive documentation directly from the console.  
Example:

```powershell
Get-Help Get-Process -Full
    ```

## Supported Script Types

PowerShell can interact with multiple script formats and scripting environments:

- `.ps1` (PowerShell scripts): Primary automation and configuration scripts.
    
- `.[[bat]]` / `.cmd` (Batch files): Legacy support for traditional Windows scripting.
    
- `.vbs` (VBScript): Executes legacy Visual Basic scripts.
    
- WMI Scripts: Interfaces with Windows Management Instrumentation.
    
- .NET Code Snippets: Full access to .NET APIs.
    
- External Languages: Executes other scripts (e.g., Python) via CLI:
    ```powershell
    python script.py
    ```
    
- Structured Data (JSON/XML): Built-in cmdlets to parse, query, and write structured data:
    ```powershell
    $data = Get-Content config.json | ConvertFrom-Json
    ```


To Do:
- [ ]  Explore the uses of [[PowerShell]]: see [[Powershell scripts]]

https://www.youtube.com/watch?v=18hUejOK0qk

```cmd
prompt $g
```

### powershell
```powershell
$profile

microsfot_Powershell_profile have

function prompt{
$p = -path
"$p> "
}
```

getting the script working 

https://stackoverflow.com/questions/41117421/ps1-cannot-be-loaded-because-running-scripts-is-disabled-on-this-system

