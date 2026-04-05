---
tags:
category: DEVOPS
---
This guide covers managing R package dependencies in your project, similar to Python's `pip` + `venv`.

Currently:
- Use R studio or ipynb (easier)
## Key Concepts

### What is renv?

**`renv`** is [[R]]'s equivalent to Python's **venv + requirements.txt**. It's the recommended way to ensure consistent package versions across your project and team.

| Feature | Python | R |
|---------|--------|---|
| Environment isolation | `venv` | `renv/` folder |
| Dependency lock file | `requirements.txt` | `renv.lock` |
| Auto-activation | Manual (`source venv/bin/activate`) | Automatic (`.Rprofile`) |
| Freeze/snapshot | `pip freeze` | `renv::snapshot()` |
| Restore | `pip install -r requirements.txt` | `renv::restore()` |
| Share with team | Commit `requirements.txt` | Commit `renv.lock` |

**Key advantage:** `renv.lock` includes all transitive dependencies (packages your packages depend on) with exact versions. When you run `renv::restore()`, everyone gets the exact same package versions, eliminating "works on my machine" issues.
## Why Not Just Use .Rproj?

The `.Rproj` file only stores project settings (workspace behavior, encoding, tabs). It does **not** manage package dependencies. You need `renv` for that.

## Getting Started on Windows [[Command Prompt|CMD]]

### Step 1: First-Time Setup - Install renv

If you don't have `renv` installed yet:

```cmd
R
```

Then in the R console:

```r
install.packages("renv")
renv::init()
renv::snapshot()
q()
```

### Step 2: What Gets Created

Running `renv::init()` creates:
- **`.Rprofile`** — Activates renv automatically when you open the project
- **`renv.lock`** — Locks all package versions
- **`renv/`** — Folder storing your project's packages

### Step 3: Regular Workflow

**Install new packages:**
```r
install.packages("your_package")
library(your_package)
```

**Update the lock file (after installing packages):**
```r
renv::snapshot()
```

**When running scripts, packages load automatically:**
```cmd
Rscript your_script.R
```

**Restore packages (on new machine or after cloning):**
```r
renv::restore()
```

### Using Rscript Directly

If you prefer not to open an R console, use Rscript:

```cmd
Rscript -e "install.packages('renv')"
Rscript -e "renv::init()"
Rscript -e "renv::snapshot()"
```

## Git Workflow

1. **Commit `renv.lock`** to version control
2. **Never commit the `renv/` folder** (add to `.gitignore` if needed)
3. **When teammates pull:** They run `renv::restore()` to get the same packages

## Running Rscript in VS Code

VS Code will respect your renv setup automatically:
- When you run `Rscript your_script.R` from the terminal, it loads packages from `renv.lock`
- The `.Rprofile` activates renv for your project
- No special environment variables needed