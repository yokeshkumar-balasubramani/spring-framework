# CVE-2024-38820 Patch Integration

This project provides an automated patching mechanism for addressing 

**CVE-2024-38820** in the Spring Framework. It includes a Python script that scans and modifies Java source files to apply safe code transformations and enforces locale-safe operations.

---

## 📁 Directory Structure

buildSrc/ 
    └── src/ 
        └── main/ 
            └── python/ 
                ├── runPatch/ 
                    │ └── main.py # Main runner script that loads all patches 
                └── patches/ 
                └── CVE-2024-38820.py # Patch logic specific to CVE-2024-38820

---

## 🛠️ What the Patch Does

The script targets Java source files under `src/main/java/` and applies the following changes:

1. **Locale Safety:**
    - Replaces `Locale.ENGLISH` with `Locale.ROOT`.
    - Replaces calls to `toLowerCase()` with `toLowerCase(Locale.ROOT)` to ensure locale-safe operations.

2. **Import Management:**
    - Adds `import java.util.Locale;` if `Locale.ROOT` is used and the import is missing.
    - Ensures correct import order according to Java conventions (e.g., `java.util.List` before `java.util.Locale`).

3. **Copyright**
    - Updates any `* Copyright 2002-XXXX` to `* Copyright 2002-2024`.

4. **Scope Restriction:**
    - Only applies to files inside `src/main/java/`.
    - Test files or other directories are excluded from modifications.

---

## ⚙️ Gradle Integration

To ensure patches are applied automatically before compilation, the Python patch script is integrated with the Gradle build process.
