# Attribution Guide for Forked MIT-Licensed Projects

## Your Situation

Your project (aiphoria) is a fork/derivative of the original **aiphoria** project by the **European Forest Institute (EFI)**, which is licensed under the MIT license.

---

## ✅ The Correct Approach

### 1. **Keep the Original License**
Your current LICENSE file is correct - MIT with copyright to European Forest Institute. 

✅ **Current status**: Correct

```
MIT License

Copyright (c) 2024 European Forest Institute
```

### 2. **Add Author/Contributor Information**
Since MIT license allows modifications and redistribution, you should:

**Option A (RECOMMENDED)** - Update the LICENSE to include both:
```
MIT License

Copyright (c) 2024 European Forest Institute
Copyright (c) 2024 Arthur Jakobs

Permission is hereby granted, free of charge, to any person obtaining a copy...
```

**Option B** - Create CONTRIBUTORS.md or ACKNOWLEDGMENTS.md:
```markdown
# Contributors

## Original Authors
- European Forest Institute (EFI)
  - Cleo Orfanidou (cleo.orfanidou@efi.int)
  - Janne Järvikylä (janne.jarvikyla@efi.int)

## Fork Maintainer
- Arthur Jakobs (2024)
```

### 3. **Update Metadata Files**

#### **setup.py / pyproject.toml**
Your current setup is incomplete. Here's what you should do:

**For pyproject.toml** (preferred modern approach):
```toml
[project]
authors = [
    {name = "Arthur Jakobs", email = "arthur.jakobs@example.com"}
]

# Add this section:
contributors = [
    {name = "European Forest Institute", email = "cleo.orfanidou@efi.int"}
]
```

**For setup.py**:
```python
setup(
    author="Arthur Jakobs",
    maintainer="Arthur Jakobs",
    maintainer_email="arthur.jakobs@example.com",
    # Note: setuptools doesn't have contributors field, 
    # use description or CONTRIBUTORS.md instead
)
```

### 4. **README.md Update**
Add proper attribution section:

```markdown
## Attribution

This project is maintained by Arthur Jakobs as a fork of the original 
[aiphoria](https://github.com/EuropeanForestInstitute/aiphoria) project 
created by the European Forest Institute.

### Original Project
- **Original Authors**: European Forest Institute
  - Cleo Orfanidou
  - Janne Järvikylä
- **License**: MIT
- **Repository**: https://github.com/EuropeanForestInstitute/aiphoria

### Modifications
Enhancements and modifications made by Arthur Jakobs (2024).

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

The MIT License permits:
- ✅ Commercial use
- ✅ Modification
- ✅ Distribution
- ✅ Private use

With conditions:
- ⚠️ Must include license and copyright notice
- ⚠️ Must include a copy of this License
```

### 5. **Package Docstring Update**

In `aiphoria/__init__.py`:

```python
"""
Aiphoria - Advanced Industrial Process Flow Handling and ODYM-based 
Resource Information Assistant

A Python package for material flow analysis and dynamic stock modeling.

This project is a fork/derivative work of the original aiphoria project by 
the European Forest Institute, maintained by Arthur Jakobs.

Original Project:
    - Authors: European Forest Institute
    - License: MIT
    - Repository: https://github.com/EuropeanForestInstitute/aiphoria

Modifications and enhancements (2024) by Arthur Jakobs.
Licensed under MIT License.
"""
```

---

## Best Practices for MIT-Licensed Forks

### ✅ DO:
1. ✅ Keep the original LICENSE file
2. ✅ Add your name to LICENSE as contributor/modifier
3. ✅ Create CONTRIBUTORS.md or ACKNOWLEDGMENTS.md
4. ✅ Update README with attribution section
5. ✅ Link to original repository
6. ✅ Document what you've modified
7. ✅ Update pyproject.toml with contributor info
8. ✅ Include original authors' contact info if public

### ❌ DON'T:
1. ❌ Remove or modify the original LICENSE
2. ❌ Claim you're the original author
3. ❌ Remove attribution to European Forest Institute
4. ❌ Change the license type (unless you have permission)
5. ❌ Forget to mention it's a fork/derivative work
6. ❌ Hide the original repository

---

## MIT License - Quick Reference

The MIT License is **very permissive** - you can:
- ✅ Modify the code
- ✅ Distribute it
- ✅ Use it commercially
- ✅ Use it privately
- ✅ Sublicense it

**You just need to:**
- Include the original license
- Include copyright notice
- State changes made
- Include this license with any copy

---

## Recommended File Structure

```
aiphoria/
├── LICENSE .......................... [UPDATED] Add your copyright
├── README.md ........................ [UPDATED] Add attribution section
├── CONTRIBUTORS.md .................. [NEW] List all contributors
├── ACKNOWLEDGMENTS.md ............... [OPTIONAL] Extended credits
├── CHANGELOG.md ..................... [NEW] Document changes from original
├── pyproject.toml ................... [UPDATED] Add contributors field
├── setup.py ......................... [UPDATED] Add maintainer info
└── aiphoria/
    └── __init__.py .................. [UPDATED] Add docstring attribution
```

---

## Implementation Steps

### Step 1: Update LICENSE File
```
MIT License

Copyright (c) 2024 European Forest Institute
Copyright (c) 2024 Arthur Jakobs

Permission is hereby granted...
```

### Step 2: Create CONTRIBUTORS.md
```markdown
# Contributors and Attribution

## Original Project
- **European Forest Institute (EFI)**
  - Cleo Orfanidou (cleo.orfanidou@efi.int)
  - Janne Järvikylä (janne.jarvikyla@efi.int)
  - [Original Repository](https://github.com/EuropeanForestInstitute/aiphoria)

## Fork Maintained By
- **Arthur Jakobs** (2024)
  - Refactored to proper Python package structure
  - Enhanced documentation
  - [This Repository](https://github.com/jakobsarthur/aiphoria)

## License
MIT License - See [LICENSE](LICENSE) file for details
```

### Step 3: Update README.md
Add this section:
```markdown
## Attribution & Licensing

**This project is a fork of the original aiphoria project created by the 
European Forest Institute.**

### Original Project
The original [aiphoria](https://github.com/EuropeanForestInstitute/aiphoria) 
was developed by:
- **Cleo Orfanidou** (cleo.orfanidou@efi.int)
- **Janne Järvikylä** (janne.jarvikyla@efi.int)

### Current Fork
Maintained and enhanced by Arthur Jakobs as of 2024.

### License
This project is licensed under the **MIT License** - permissive open-source 
license. See [LICENSE](LICENSE) file for full details.

Both the original and this fork are licensed under MIT, which allows:
- Commercial use
- Modification and distribution
- Private use
- Sublicensing

**Conditions:**
- Must include the original license text
- Must include copyright notice
- See LICENSE file for full terms
```

### Step 4: Update pyproject.toml
```toml
[project]
authors = [
    {name = "Arthur Jakobs", email = "arthur.jakobs@example.com"}
]

# Note: PEP 621 doesn't have standard contributors field yet,
# use in description or separate CONTRIBUTORS.md file
```

### Step 5: Update aiphoria/__init__.py
```python
"""
Aiphoria - Advanced Industrial Process Flow Handling and ODYM-based 
Resource Information Assistant

A Python package for material flow analysis and dynamic stock modeling.

**Fork Information:**
This project is a fork of the original aiphoria project created by the 
European Forest Institute.

Original Project:
    - Authors: European Forest Institute
    - Contact: cleo.orfanidou@efi.int, janne.jarvikyla@efi.int
    - License: MIT
    - Repository: https://github.com/EuropeanForestInstitute/aiphoria

Current Fork (2024):
    - Maintained by: Arthur Jakobs
    - License: MIT (same as original)
    - Repository: https://github.com/jakobsarthur/aiphoria

Licensed under the MIT License.
"""
```

---

## Summary: What to Do Right Now

### Priority 1 (Must Do)
1. ✅ LICENSE - Add your copyright line
2. ✅ README.md - Add attribution section
3. ✅ Create CONTRIBUTORS.md file

### Priority 2 (Should Do)
1. Update aiphoria/__init__.py docstring
2. Update pyproject.toml with maintainer info
3. Create CHANGELOG.md documenting changes

### Priority 3 (Nice to Have)
1. Create ACKNOWLEDGMENTS.md for extended credits
2. Add original repo link to documentation
3. Document which parts were modified

---

## Example: Complete Attribution Section

**README.md**:
```markdown
## Attribution and License

**This is a fork of the original aiphoria project.**

### Original Project Credits
- **European Forest Institute (EFI)**
- **Authors**: Cleo Orfanidou, Janne Järvikylä
- **License**: MIT License
- **Original Repository**: [EFI/aiphoria](https://github.com/EuropeanForestInstitute/aiphoria)
- **Contact**: cleo.orfanidou@efi.int

### Fork Modifications
This fork has been maintained and enhanced by Arthur Jakobs since 2024.
Key enhancements include package structure improvements and enhanced 
documentation.

### License
This project maintains the same MIT License as the original. See 
[LICENSE](LICENSE) file for complete license text.

### How to Cite
If you use this project, please cite:
1. The original aiphoria project (European Forest Institute)
2. This fork (Arthur Jakobs, 2024) - if using specific enhancements
```

---

## Questions? Key Points to Remember

1. **MIT is permissive** - You can modify and redistribute with few restrictions
2. **You must include the license** - Always include the original LICENSE file
3. **Add your contribution** - Make it clear what you've done
4. **Credit the original** - Always mention the original authors/organization
5. **Be transparent** - Users should know it's a fork

This approach balances:
- ✅ Proper credit to the European Forest Institute
- ✅ Recognition of your improvements
- ✅ Clear communication to users
- ✅ Compliance with MIT license terms

---

**Recommended**: Implement Priority 1 items first, then Priority 2 at your convenience.
