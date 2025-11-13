#!/usr/bin/env python3
"""
Benchmark comparison: Obsidian REST API search vs ripgrep

Compares performance and results between:
1. Obsidian Local REST API simple_search
2. ripgrep (rg) direct filesystem search

Usage:
    python benchmark_search.py <search_term> [--slipbox-only]

Example:
    python benchmark_search.py "Campbell"
    python benchmark_search.py "Joseph Campbell" --slipbox-only
"""

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path

# Add parent directory to path to import obsidian_api
sys.path.insert(0, str(Path(__file__).parent / "scripts"))
from obsidian_api import get_api, ObsidianAPIError


def benchmark_api_search(query, vault_path=None, slipbox_only=False):
    """Benchmark Obsidian API search"""
    print(f"\n{'='*80}")
    print(f"OBSIDIAN API SEARCH")
    print(f"{'='*80}")

    start_time = time.time()

    try:
        api = get_api()
        results = api.simple_search(query, context_length=100)

        search_time = time.time() - start_time

        # Handle both list and dict responses
        if isinstance(results, list):
            matches = results
        elif isinstance(results, dict) and 'results' in results:
            matches = results['results']
        else:
            matches = []

        # Filter by slipbox if requested
        if slipbox_only:
            matches = [m for m in matches if m.get('filename', '').startswith('_Slipbox/')]

        # Extract just filenames
        filenames = [m.get('filename', '') for m in matches]

        print(f"✓ Search completed in {search_time:.4f} seconds")
        print(f"✓ Found {len(filenames)} files")
        print(f"\nFirst 10 results:")
        for i, filename in enumerate(filenames[:10], 1):
            print(f"  {i}. {filename}")

        if len(filenames) > 10:
            print(f"  ... and {len(filenames) - 10} more")

        return {
            'time': search_time,
            'count': len(filenames),
            'files': filenames,
            'method': 'API'
        }

    except ObsidianAPIError as e:
        print(f"✗ API Error: {e}")
        return None


def benchmark_ripgrep_search(query, vault_path, slipbox_only=False):
    """Benchmark ripgrep search"""
    print(f"\n{'='*80}")
    print(f"RIPGREP SEARCH")
    print(f"{'='*80}")

    # Determine search path
    if slipbox_only:
        search_path = os.path.join(vault_path, '_Slipbox')
    else:
        search_path = vault_path

    start_time = time.time()

    try:
        # Run ripgrep with:
        # -l: just list filenames
        # --type md: only search markdown files
        # -i: case insensitive
        result = subprocess.run(
            ['rg', '-l', '--type', 'md', '-i', query, search_path],
            capture_output=True,
            text=True,
            timeout=30
        )

        search_time = time.time() - start_time

        # Parse results
        if result.returncode == 0:
            filenames = [line.strip() for line in result.stdout.strip().split('\n') if line.strip()]
            # Convert absolute paths to relative paths
            filenames = [os.path.relpath(f, vault_path) for f in filenames]
        elif result.returncode == 1:
            # No matches found (this is normal, not an error)
            filenames = []
        else:
            print(f"✗ ripgrep error (exit code {result.returncode}): {result.stderr}")
            return None

        print(f"✓ Search completed in {search_time:.4f} seconds")
        print(f"✓ Found {len(filenames)} files")
        print(f"\nFirst 10 results:")
        for i, filename in enumerate(filenames[:10], 1):
            print(f"  {i}. {filename}")

        if len(filenames) > 10:
            print(f"  ... and {len(filenames) - 10} more")

        return {
            'time': search_time,
            'count': len(filenames),
            'files': filenames,
            'method': 'ripgrep'
        }

    except subprocess.TimeoutExpired:
        print(f"✗ ripgrep timed out after 30 seconds")
        return None
    except FileNotFoundError:
        print(f"✗ ripgrep not found. Please install ripgrep.")
        return None


def compare_results(api_result, rg_result):
    """Compare and analyze results from both methods"""
    print(f"\n{'='*80}")
    print(f"COMPARISON")
    print(f"{'='*80}")

    if not api_result or not rg_result:
        print("⚠ Cannot compare - one or both searches failed")
        return

    # Performance comparison
    print(f"\n📊 Performance:")
    print(f"  API:      {api_result['time']:.4f}s")
    print(f"  ripgrep:  {rg_result['time']:.4f}s")

    speedup = api_result['time'] / rg_result['time']
    if speedup > 1:
        print(f"  → ripgrep is {speedup:.2f}x FASTER")
    else:
        print(f"  → API is {1/speedup:.2f}x FASTER")

    # Count comparison
    print(f"\n📈 Results count:")
    print(f"  API:      {api_result['count']} files")
    print(f"  ripgrep:  {rg_result['count']} files")

    # Set comparison
    api_files = set(api_result['files'])
    rg_files = set(rg_result['files'])

    common = api_files & rg_files
    api_only = api_files - rg_files
    rg_only = rg_files - api_files

    print(f"\n🔍 Result overlap:")
    print(f"  Common to both:  {len(common)} files")
    print(f"  API only:        {len(api_only)} files")
    print(f"  ripgrep only:    {len(rg_only)} files")

    if api_only:
        print(f"\n  Files found by API but not ripgrep:")
        for f in sorted(list(api_only)[:5]):
            print(f"    - {f}")
        if len(api_only) > 5:
            print(f"    ... and {len(api_only) - 5} more")

    if rg_only:
        print(f"\n  Files found by ripgrep but not API:")
        for f in sorted(list(rg_only)[:5]):
            print(f"    - {f}")
        if len(rg_only) > 5:
            print(f"    ... and {len(rg_only) - 5} more")

    # Overall assessment
    print(f"\n{'='*80}")
    print(f"RECOMMENDATION")
    print(f"{'='*80}")

    if len(common) == len(api_files) == len(rg_files):
        print("✓ Both methods found identical results")
        if speedup > 1.2:
            print(f"✓ ripgrep is significantly faster ({speedup:.2f}x)")
            print("→ RECOMMEND: Use ripgrep for content search")
        elif speedup < 0.8:
            print(f"✓ API is significantly faster ({1/speedup:.2f}x)")
            print("→ RECOMMEND: Use API for content search")
        else:
            print("→ Performance is similar - either method works")
    else:
        print("⚠ Results differ between methods")
        if len(rg_files) > len(api_files):
            print("→ ripgrep found more results")
        else:
            print("→ API found more results")
        print("→ Investigate differences to determine which is more accurate")


def get_vault_path():
    """Get vault path from obsidian.json"""
    obsidian_config = os.path.expanduser("~/Library/Application Support/obsidian/obsidian.json")

    if not os.path.exists(obsidian_config):
        print(f"✗ Cannot find Obsidian config at {obsidian_config}")
        return None

    try:
        with open(obsidian_config) as f:
            config = json.load(f)

        # Get first vault
        vaults = config.get('vaults', {})
        if not vaults:
            print("✗ No vaults found in Obsidian config")
            return None

        first_vault = next(iter(vaults.values()))
        vault_path = first_vault.get('path')

        if not vault_path or not os.path.exists(vault_path):
            print(f"✗ Vault path not found or doesn't exist: {vault_path}")
            return None

        return vault_path

    except Exception as e:
        print(f"✗ Error reading Obsidian config: {e}")
        return None


def main():
    parser = argparse.ArgumentParser(
        description='Benchmark Obsidian API search vs ripgrep',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument('query', help='Search term or phrase')
    parser.add_argument('--slipbox-only', action='store_true',
                       help='Search only in _Slipbox directory')
    parser.add_argument('--vault', help='Vault path (auto-detected if not specified)')

    args = parser.parse_args()

    # Get vault path
    vault_path = args.vault or get_vault_path()
    if not vault_path:
        sys.exit(1)

    print(f"Vault path: {vault_path}")
    print(f"Search query: '{args.query}'")
    if args.slipbox_only:
        print(f"Scope: _Slipbox directory only")
    else:
        print(f"Scope: Entire vault")

    # Run benchmarks
    api_result = benchmark_api_search(args.query, vault_path, args.slipbox_only)
    rg_result = benchmark_ripgrep_search(args.query, vault_path, args.slipbox_only)

    # Compare results
    compare_results(api_result, rg_result)


if __name__ == '__main__':
    main()
