---
title: 
tags: 
aliases: 
category:
---
#### Files
DE_Tools\Explorations\Other\Terminal\Grep
#### Notes


|Flag|Description|
|---|---|
|`-w`|Match **whole words** only (ignores substrings).|
|`-i`|Perform a **case-insensitive** match.|
|`-n`|**Show line numbers** of matching lines.|
|`-r`|**Recursively search** subdirectories.|
|`-l`|**List only filenames** that contain matches (no line content shown).|
|`-c`|**Count matches** per file, instead of showing them.|
|`-A N`|Show **N lines after** each match.|
|`-B N`|Show **N lines before** each match.|
|`-C N`|Show **N lines before and after** each match (context lines).|
|`-P`|Use **Perl-compatible regular expressions (PCRE)**.|
|`-v`|**Invert match**: show lines that **do not** match the pattern.|
|`-o`|Print **only the matching part** of the line (not the entire line).|
|`--color`|Highlight matched strings with color (if supported by terminal).|
|`--include`|Include only files that match the given glob pattern (used with `-r`).|
|`--exclude`|Exclude files that match the given pattern from recursive searches.|

#### Images

![[grep.png]]



