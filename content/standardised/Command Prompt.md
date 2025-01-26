---
tags:
  - software
aliases:
  - cmd
category:
---
Command Prompt (cmd) is a command-line interpreter on Windows systems that allows users to execute commands to perform various basic tasks. Below are some common tasks that can be performed in cmd, along with examples:

Related to:
- [[Bash]]

## 1. Navigating the File System

- **Changing Directories:**
  ```cmd
  cd C:\path\to\directory
  ```
  Changes the current directory to `C:\path\to\directory`.

- **Listing Files and Directories:**
  ```cmd
  dir
  ```
  Lists the files and directories in the current directory.

## 2. Managing Files and Directories

- **Creating a Directory:**
  ```cmd
  mkdir newfolder
  ```
  Creates a new directory named `newfolder`.

- **Deleting a Directory:**
  ```cmd
  rmdir /s /q newfolder
  ```
  Deletes the directory `newfolder` and its contents. The `/s` flag removes all directories and files in the specified directory, and the `/q` flag runs the command quietly without asking for confirmation.

- **Copying Files:**
  ```cmd
  copy C:\source\file.txt D:\destination\
  ```
  Copies `file.txt` from the `C:\source` directory to the `D:\destination` directory.

- **Renaming Files:**
  ```cmd
  ren oldfile.txt newfile.txt
  ```
  Renames `oldfile.txt` to `newfile.txt`.

- **Deleting Files:**
  ```cmd
  del file.txt
  ```
  Deletes `file.txt`.

## 3. Viewing and Managing System Information

- **Viewing IP Configuration:**
  ```cmd
  ipconfig
  ```
  Displays the current network configuration.

- **Viewing System Information:**
  ```cmd
  systeminfo
  ```
  Provides detailed system information including OS version, hardware details, and network configurations.

## 4. Managing Processes

- **Viewing Running Processes:**
  ```cmd
  tasklist
  ```
  Lists all currently running processes.

- **Killing a Process:**
  ```cmd
  taskkill /F /PID 1234
  ```
  Terminates the process with the Process ID (PID) `1234`. The `/F` flag forces the process to terminate.

## 5. Networking Commands

- **Pinging a Server:**
  ```cmd
  ping www.example.com
  ```
  Sends ICMP Echo Request packets to the specified host and displays the response.

- **Tracing Route to a Server:**
  ```cmd
  tracert www.example.com
  ```
  Traces the route packets take to the specified host.

## 6. Batch File Scripting

- **Creating and Running a Simple Batch File:**
  - Create a file named `example.bat` with the following content:
    ```cmd
    @echo off
    echo Hello, World!
    pause
    ```
  - Run the batch file:
    ```cmd
    example.bat
    ```
  This batch file prints "Hello, World!" to the console and waits for the user to press a key before closing.

## 7. Environment Variables

- **Viewing Environment Variables:**
  ```cmd
  set
  ```
  Displays all current environment variables and their values.

- **Setting an Environment Variable:**
  ```cmd
  set MYVAR=Hello
  ```
  Sets an environment variable `MYVAR` with the value `Hello`.

## 8. Disk Operations

- **Checking Disk Usage:**
  ```cmd
  chkdsk C:
  ```
  Checks the file system and file system metadata of the C: drive for logical and physical errors.

- **Formatting a Disk:**
  ```cmd
  format D: /FS:NTFS
  ```
  Formats the D: drive with the NTFS file system.

## 9. Echoing Messages

- **Displaying a Message:**
  ```cmd
  echo Hello, World!
  ```
  Prints `Hello, World!` to the console.

## 10. Redirecting Output

- **Redirecting Command Output to a File:**
  ```cmd
  dir > output.txt
  ```
  Redirects the output of the `dir` command to `output.txt`.

These examples illustrate some of the basic functionalities of Command Prompt. While cmd is less powerful compared to [[PowerShell]], it remains useful for simple file system navigation, file management, and running legacy scripts.

