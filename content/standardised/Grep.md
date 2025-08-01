---
aliases: 
category: 
date modified: 27-07-2025
tags:
  - system
title:
---
In [[DE_Tools]] see:
https://github.com/rhyslwells/DE_Tools/blob/main/DE_Tools/Explorations/Other/Terminal/Grep

#### Example of what Grep can do 

 1. [[Search]] for a pattern in files

```bash
grep "error" logfile.txt
```

* Searches for the word `"error"` in `logfile.txt`.
* Useful for quickly checking logs or documents.

 2. Recursive search in directories

```bash
grep -r "TODO" ./src
```

* Recursively searches all files in the `./src` directory for `"TODO"`.
* Useful for finding code comments, notes, or markers across a codebase.

 3. Display line numbers of matches

```bash
grep -n "fail" test_results.txt
```

* Shows line numbers where `"fail"` appears.
* Helpful for [[debugging]] or jumping to the right place in a large file.

 4. Show only matching part of the line

```bash
grep -o "http[s]\?://[a-zA-Z0-9./?=_-]*" webpage.html
```

* `-o` prints *only* the matching substring (e.g., all URLs from HTML).
* Good for extracting emails, URLs, etc.

 5. Search multiple files and include filenames

```bash
grep "password" *.conf
```

* Searches all `.conf` files and prints matching lines with their filenames.
* Useful for auditing sensitive configurations.

#### Flags

Useful for finding where a function is used in a code base.

|Flag|Description|
|---|---|
|`-w`|Match whole words only (ignores substrings).|
|`-i`|Perform a case-insensitive match.|
|`-n`|Show line numbers of matching lines.|
|`-r`|Recursively search subdirectories.|
|`-l`|List only filenames that contain matches (no line content shown).|
|`-c`|Count matches per file, instead of showing them.|
|`-A N`|Show N lines after each match.|
|`-B N`|Show N lines before each match.|
|`-C N`|Show N lines before and after each match (context lines).|
|`-P`|Use Perl-compatible regular expressions (PCRE).|
|`-v`|Invert match: show lines that do not match the pattern.|
|`-o`|Print only the matching part of the line (not the entire line).|
|`--color`|Highlight matched strings with color (if supported by terminal).|
|`--include`|Include only files that match the given glob pattern (used with `-r`).|
|`--exclude`|Exclude files that match the given pattern from recursive searches.|





