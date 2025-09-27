---
aliases:
- cmd
category: DE
date modified: 27-09-2025
tags:
- system
---
Command Prompt (cmd) is a text-based command-line interpreter for Windows. Although more limited than [[PowerShell]]—which supports object-oriented scripting—`cmd` remains useful for legacy compatibility, simple file and process operations, and lightweight scripting.

Related to: [[Bash]], [[PowerShell]], [[bat]]

Summary Characteristics
* Text-Based Interface: Commands operate on plain text, without the object-passing capabilities of PowerShell.
* Limited Built-in Commands: Focused on core utilities like file handling, process control, and system inspection.
* Direct Execution: Commands are interpreted and executed line-by-line, without support for pipelines.

Navigating the File System
* Change Directory:
  ```cmd
  cd C:\path\to\directory
  ```
* List Directory Contents:
  ```cmd
  dir
  ```
* List in Bare Format:
  ```cmd
  dir /b
  ```

Managing Files and Directories
* Create a Directory:
  ```cmd
  mkdir newfolder
  ```
* Delete a Directory (with contents):
  ```cmd
  rmdir /s /q newfolder
  ```
* Copy a File:
  ```cmd
  copy C:\source\file.txt D:\destination\
  ```
* Rename a File:
  ```cmd
  ren oldfile.txt newfile.txt
  ```
* Delete a File:
  ```cmd
  del file.txt
  ```

Viewing System and Network Information
* Network Configuration:
  ```cmd
  ipconfig
  ```
* Detailed System Info:
  ```cmd
  systeminfo
  ```

Managing Processes
* List Running Processes:
  ```cmd
  tasklist
  ```
* Kill a Process by PID:
  ```cmd
  taskkill /F /PID 1234
  ```


Scripting with Batch Files
* Simple `.bat` Script Example:
  `example.bat`
  ```cmd
  @echo off
  echo Hello, World!
  pause
  ```
* Run the Script:
  ```cmd
  example.bat
  ```

Environment Variables
* View All Variables:
  ```cmd
  set
  ```
* Set a Variable:
  ```cmd
  set MYVAR=Hello
  ```

Redirecting Output
* Send Command Output to File:

  ```cmd
  dir > output.txt
  ```

Viewing Command History
* Current Session Only:

  ```cmd
  doskey /history
  ```




