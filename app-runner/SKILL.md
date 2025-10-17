---
name: app-runner
description: Manages application lifecycle and health checks. Use when app isn't running but needs to be (testing, debugging, development). Stores project-specific startup config, handles multi-service apps, performs health checks. INVOKE when webapp-testing or other skills detect app is not accessible.
---

# Application Runner

Manages the lifecycle of web applications and services for development and testing. Handles service startup, health checks, and project-specific configuration.

## When to Use This Skill

**AUTOMATICALLY invoke when:**
- webapp-testing (or other skills) detects application is not accessible
- User asks to "start the app", "run the server", "start services"
- Tests fail with connection errors (connection refused, timeout, etc.)
- Health check fails when trying to access application endpoints

**DO NOT use when:**
- App is already running and accessible
- User just wants to know how to start the app (just read config)

## Core Responsibilities

1. **Application Lifecycle Management**
   - Start/stop web applications and services
   - Handle multi-service applications (frontend, backend, proxy, database, etc.)
   - Manage service dependencies and startup order

2. **Health Checks**
   - Verify services are accessible before testing
   - Wait for services to be ready
   - Detect when services are down

3. **Project Configuration**
   - Store startup commands in `.app-runner.yml`
   - Ask user once, remember for project
   - Handle project-specific requirements

## Configuration File Format

`.app-runner.yml` in project root:

```yaml
# Single service example
service:
  command: npm run dev
  health_check:
    url: http://localhost:5173
    timeout: 30

# Multi-service example
services:
  - name: nginx-proxy
    command: docker-compose up -d nginx
    health_check:
      url: http://localhost:3000
      timeout: 10

  - name: backend
    command: cd src && uvicorn app:app --port 8000
    health_check:
      url: http://localhost:8000/health
      timeout: 15

  - name: frontend
    command: cd web && npm run dev
    health_check:
      url: http://localhost:5173
      timeout: 30
    depends_on:
      - backend

# Main entry point for testing/accessing the application
entry_point: http://localhost:3000
```

## Helper Scripts

- `scripts/health_check.py` - Check if URL is accessible
- `scripts/manage_config.py` - Read/write `.app-runner.yml`
- `scripts/start_services.py` - Start services from config

## Usage Patterns

### Pattern 1: Check if App is Running

```python
import subprocess
import json

result = subprocess.run(
    ['python', '~/.claude/skills/app-runner/scripts/health_check.py',
     '--url', 'http://localhost:3000'],
    capture_output=True,
    text=True
)
info = json.loads(result.stdout)

if not info['accessible']:
    # App not running - invoke app-runner skill
    pass
```

### Pattern 2: Start Application

```python
# app-runner skill handles this
# 1. Check for .app-runner.yml
# 2. If not found, ask user how to start app
# 3. Save config
# 4. Start services
# 5. Wait for health checks
# 6. Return control to calling skill
```

## Integration with Other Skills

### webapp-testing Integration

```python
# In webapp-testing test script:
from pathlib import Path
import subprocess

# Check if app is accessible
health_check = subprocess.run(
    ['python', str(Path.home() / '.claude/skills/app-runner/scripts/health_check.py'),
     '--url', os.environ['TEST_BASE_URL']],
    capture_output=True,
    text=True
)

if health_check.returncode != 0:
    print(f"Application not accessible at {os.environ['TEST_BASE_URL']}")
    print("Please invoke app-runner skill to start the application.")
    sys.exit(1)

# Continue with testing...
```

## First-Run Experience

**When no config exists:**

1. Detect `.app-runner.yml` is missing
2. Ask user: "How do you start your application?"
3. User provides command(s)
4. Ask: "What URL should I check to verify it's running?"
5. Save to `.app-runner.yml`
6. Start services
7. Perform health checks
8. Ready for testing

**Subsequent runs:**

1. Read `.app-runner.yml`
2. Start services
3. Health checks
4. Ready

## Health Check Logic

Health checks verify a service is accessible:

```python
def health_check(url: str, timeout: int = 30) -> bool:
    """
    Check if a URL is accessible.

    Retries with exponential backoff up to timeout.
    Returns True if accessible, False otherwise.
    """
    import requests
    import time

    start = time.time()
    delay = 0.5

    while time.time() - start < timeout:
        try:
            response = requests.get(url, timeout=5)
            if response.status_code < 500:
                return True
        except requests.exceptions.RequestException:
            pass

        time.sleep(delay)
        delay = min(delay * 1.5, 5)  # Exponential backoff, max 5s

    return False
```

## Best Practices

1. **Keep config in project root** - `.app-runner.yml` should be project-specific
2. **Add to .gitignore if needed** - Config might contain local paths
3. **Use relative paths** - Makes config portable across machines
4. **Document requirements** - If app needs database, mention in config comments
5. **Health checks should be fast** - Use `/health` endpoints, not complex pages

## Example Configurations

### SvelteKit + Python Backend

```yaml
services:
  - name: backend
    command: cd src && uvicorn app:app --reload
    health_check:
      url: http://localhost:8000/health
      timeout: 15

  - name: frontend
    command: cd web && npm run dev
    health_check:
      url: http://localhost:5173
      timeout: 30
    depends_on:
      - backend

entry_point: http://localhost:5173
```

### Docker Compose

```yaml
service:
  command: docker-compose up -d
  health_check:
    url: http://localhost:3000
    timeout: 30
  shutdown_command: docker-compose down

entry_point: http://localhost:3000
```

### Nginx Proxy + Services

```yaml
services:
  - name: backend
    command: cd backend && python server.py
    health_check:
      url: http://localhost:8000
      timeout: 15

  - name: frontend
    command: cd frontend && npm run dev
    health_check:
      url: http://localhost:5173
      timeout: 30

  - name: nginx
    command: docker-compose up -d nginx
    health_check:
      url: http://localhost:3000
      timeout: 10
    depends_on:
      - backend
      - frontend

# Test through the nginx proxy
entry_point: http://localhost:3000
```
