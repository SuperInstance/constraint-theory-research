#!/usr/bin/env python3
"""
Run All Benchmarks

This script runs all benchmark suites and aggregates results.

Author: SuperInstance Research Team
Date: 2025-01-27
"""

import subprocess
import sys
import json
import time
from pathlib import Path


def run_benchmark(script_name: str) -> dict:
    """Run a benchmark script and return results."""
    print(f"\n{'='*60}")
    print(f"Running {script_name}...")
    print('='*60)
    
    result = subprocess.run(
        [sys.executable, script_name],
        capture_output=True,
        text=True
    )
    
    print(result.stdout)
    
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return {'success': False, 'error': result.stderr}
    
    return {'success': True}


def main():
    """Run all benchmarks."""
    print("\n" + "="*60)
    print("CONSTRAINT THEORY BENCHMARK SUITE")
    print("="*60 + "\n")
    
    benchmark_dir = Path(__file__).parent
    results_dir = benchmark_dir / "results"
    results_dir.mkdir(exist_ok=True)
    
    benchmarks = [
        "benchmark_snap.py",
        "benchmark_quantize.py",
        "benchmark_holonomy.py"
    ]
    
    start_time = time.time()
    results = {}
    
    for benchmark in benchmarks:
        script_path = benchmark_dir / benchmark
        if script_path.exists():
            results[benchmark] = run_benchmark(str(script_path))
        else:
            print(f"Warning: {benchmark} not found")
            results[benchmark] = {'success': False, 'error': 'File not found'}
    
    total_time = time.time() - start_time
    
    # Summary
    print("\n" + "="*60)
    print("BENCHMARK SUMMARY")
    print("="*60)
    
    for name, result in results.items():
        status = "PASS" if result.get('success', False) else "FAIL"
        print(f"  [{status}] {name}")
    
    print(f"\nTotal time: {total_time:.2f} seconds")
    
    # Save summary
    summary = {
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
        'total_time_seconds': total_time,
        'results': results
    }
    
    summary_path = results_dir / "benchmark_summary.json"
    with open(summary_path, 'w') as f:
        json.dump(summary, f, indent=2)
    
    print(f"\nSummary saved to: {summary_path}")


if __name__ == "__main__":
    main()
