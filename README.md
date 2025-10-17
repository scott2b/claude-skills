# Claude Code Skills

Custom skills for [Claude Code](https://claude.ai/code) that work together to provide seamless web application testing and development.

## Installation

### Prerequisites

- [Claude Code](https://docs.claude.com/en/docs/claude-code) installed and running
- Python 3.10+
- [Playwright](https://playwright.dev/python/docs/intro) for browser automation: `pip install playwright && playwright install`
- (Optional) `requests` library for health checks: `pip install requests`
- (Optional) PyYAML for config management: `pip install pyyaml`

### Option 1: Install All Skills (Recommended)

Clone this repository directly into your `~/.claude/skills` directory:

```bash
# If ~/.claude/skills doesn't exist yet
git clone https://github.com/scott2b/claude-skills.git ~/.claude/skills

# If ~/.claude/skills already exists
cd ~/.claude/skills
git init
git remote add origin https://github.com/scott2b/claude-skills.git
git fetch
git checkout -t origin/main
```

This will make all skills available to Claude Code automatically.

### Option 2: Install Individual Skills

If you only want specific skills, copy them into `~/.claude/skills/`:

```bash
# Create skills directory if it doesn't exist
mkdir -p ~/.claude/skills

# Clone the repo temporarily
git clone https://github.com/scott2b/claude-skills.git /tmp/claude-skills

# Copy individual skills (with their dependencies)
cp -r /tmp/claude-skills/webapp-testing ~/.claude/skills/
cp -r /tmp/claude-skills/env-manager ~/.claude/skills/
cp -r /tmp/claude-skills/app-runner ~/.claude/skills/

# Clean up
rm -rf /tmp/claude-skills
```

**Note**: If you install `webapp-testing`, you should also install its dependencies (`env-manager` and `app-runner`) for full functionality.

### Verify Installation

Claude Code will automatically detect skills in `~/.claude/skills/`. To verify:

```bash
ls ~/.claude/skills/
# Should show: webapp-testing  env-manager  app-runner  README.md
```

Next time you use Claude Code, these skills will be available.

## Skills Overview

### webapp-testing
**Purpose**: Playwright-based browser automation for testing web applications

**Key Features**:
- Login helper with role-based authentication (user/admin)
- Auth state caching for faster subsequent tests
- Screenshot capture and DOM inspection
- CSRF token handling

**Dependencies**:
- `env-manager` - for checking/loading environment variables
- `app-runner` - for ensuring application is running and accessible

**Scripts**:
- `scripts/login_helper.py` - Handles authentication with role support

**When Invoked**: User asks to test web pages, verify functionality, or automate browser interactions

---

### env-manager
**Purpose**: Intelligent environment variable management

**Key Features**:
- Detects missing environment variables
- Finds .env files in project directory
- Analyzes file format (shell/simple/fish)
- Provides shell-specific load commands (bash, zsh, fish)
- Uses REAL environment variables (no fake python-dotenv approach)

**Dependencies**: None (standalone)

**Scripts**:
- `scripts/check_env.py` - Check if required variables are set
- `scripts/detect_env_files.py` - Find and analyze .env files

**When Invoked**: Automatically when environment variables are missing or tasks require configuration (testing, API calls, deployment)

---

### app-runner
**Purpose**: Application lifecycle management and health checks

**Key Features**:
- Interactive first-time setup (asks user how to start app)
- Project-specific configuration via `.app-runner.yml`
- Multi-service application support
- Health check with exponential backoff
- Startup command storage and reuse

**Dependencies**: None (standalone)

**Scripts**:
- `scripts/health_check.py` - Verify URL accessibility
- `scripts/manage_config.py` - Read/write `.app-runner.yml` config

**When Invoked**: Automatically when application is not accessible but needs to be (for testing, debugging, development)

---

## Dependency Graph

```
webapp-testing
├── env-manager    (checks environment variables)
└── app-runner     (ensures app is running)
```

## Typical Workflow

1. User: "Test the login page"
2. Claude invokes `webapp-testing` skill
3. `webapp-testing` checks environment via `env-manager`
   - If missing variables: env-manager finds .env files and suggests load commands
4. `webapp-testing` checks if app is accessible via `app-runner`
   - If not running: app-runner asks how to start it (first time) or uses saved config
   - Waits for health check to pass
5. `webapp-testing` executes Playwright test script
   - Uses login_helper.py if authentication needed
   - Takes screenshots, inspects DOM, performs actions
   - Opens screenshots in system viewer (Preview on macOS)

## Design Principles

- **Separation of Concerns**: Each skill has a single, well-defined responsibility
- **Real Environment**: Skills use actual shell environment variables, not fake python-dotenv
- **Project-Specific Config**: Settings stored in project directory (`.app-runner.yml`, `.env.test`)
- **Interactive First-Time Setup**: Ask user once, save configuration, reuse automatically
- **Framework Agnostic**: No hardcoded assumptions about ports, frameworks, or setup
- **Black Box Scripts**: Helper scripts are invoked directly without reading source code
