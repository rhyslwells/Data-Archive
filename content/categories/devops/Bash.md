---
aliases:
  - 
category: DEVOPS
date modified: 27-09-2025
tags:
  - system
  - programming
---
#### Automation Scripts

In [[ML_Tools]], see: [[Bash_folder]]
#### **Basic Commands**

1. **Show Current Directory**: 
   ```bash
   pwd
   ```
2. **Display Contents of a Text File**: 
   ```bash
   cat filename.txt
   ```
3. **Search for a Word in a File**: 
   ```bash
   [[grep]] "word" filename.txt
   ```
4. **Replace Text in a File (Output Only)**: 
   ```bash
   sed 's/old/new/g' filename.txt
   ```

### Writing and Running a Bash Script

1. **Create a Script**: 
   ```bash
   nano hello.sh
   ```
   Add:
   ```bash
   #!/bin/bash
   echo "Hello, $(whoami)! Welcome to Bash scripting!"
   ```
   Save and exit: **Ctrl + O**, **Enter**, **Ctrl + X**.

2. **Make the Script Executable**: 
   ```bash
   chmod +x hello.sh
   ```

3. **Run the Script**: 
   ```bash
   ./hello.sh
   ```

### Useful Bash Automation Tips

- **Clear Screen**: 
   ```bash
   clear
   ```
- **Keyboard Shortcut**: **Ctrl + L**.
- **Clear Screen and Command History**: 
   ```bash
   clear && history -c
   ```
- **Reset Terminal**: 
   ```bash
   reset
   ```

### Managing Command History

1. **Clear Current Session’s History**: 
   ```bash
   history -c
   ```
2. **Save History to a Custom File**: 
   ```bash
   history > my_session_history.txt
   ```
3. **Clear and Remove Saved History**: 
   ```bash
   history -c
   > ~/.bash_history
   ```
4. **Start a Fresh Bash Session**: 
   ```bash
   exec bash
   ```

#### **Example: Conditional Execution**
```bash
if [ -f filename.txt ]; then
  echo "File exists."
else
  echo "File does not exist."
fi
```
### If you want to learn more bash, explore:

See these concepts:
   - Shebang: `#!/bin/bash`
   - Variables: `$PI_IP`, `${variable}`
   - Conditionals: `if [ condition ]; then`
   - Loops: `for`, `while`
   - Functions: `function_name() {}`
   - Command substitution: `$(command)`
   - Redirects: `>`, `>>`, `2>&1`

See these concepts:
   - Function definitions and exports
   - Color codes (ANSI escape sequences)
   - Command piping: `|`
   - SSH with command execution
   - Error checking: `$?`
   - Configuration files
   - Heredocs: `<< 'EOF'`