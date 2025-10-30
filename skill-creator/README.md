# Skill Creator

A meta-skill that guides the creation of effective Claude Code skills.

Originally copied from https://github.com/anthropics/skills/tree/main/skill-creator


## Overview

The skill-creator provides comprehensive guidance for creating, editing, and packaging skills that extend Claude's capabilities. It includes best practices for skill design, progressive disclosure principles, and tooling for initialization, validation, and packaging.


## What's Included

### SKILL.md
Core instructions for the skill creation process, covering:
- Understanding skills and their anatomy
- 6-step skill creation workflow
- Best practices for writing skills (imperative form, date handling, progressive disclosure)
- Guidelines for bundled resources (scripts, references, assets)

### Scripts

- **`init_skill.py`** - Initialize a new skill with proper directory structure and template files
- **`package_skill.py`** - Validate and package skills into distributable zip files
- **`quick_validate.py`** - Validate skill structure and metadata

### LICENSE.txt

License information for the skill-creator skill.


## Usage

This skill is automatically invoked when users want to create or update a skill. To manually invoke:

```
Use the skill-creator skill to help me build a new skill for [purpose]
```


## Changelog

### 2025-10-30 - Date Handling Best Practice

**Added**: Best practices guidance for handling dates and timestamps in skills

**Context**: Claude does not have a built-in real-time clock tool and may hallucinate or guess dates incorrectly. This was identified as a recurring issue in narrative skills that timestamp their outputs.

**Changes**:
- Added new "Best Practices" section to Step 4 (Edit the Skill)
- Documented that skills requiring current date should:
  - In Claude Code: Explicitly instruct to use `date +%Y-%m-%d` command
  - In Claude Desktop/Web: Instruct to ask user or use system date if available
  - Never rely on Claude to provide dates from memory or inference
- Added example instruction format
- Included alongside existing best practices for progressive disclosure and clear tool usage

**Impact**: Future skills created with skill-creator will include proper date handling instructions, preventing date hallucination errors.

**Related**: This change was applied retroactively to the narrative-maps skill (2025-10-30).

---

## Version History

- **2025-10-30**: Initial README and changelog created; date handling best practice added
