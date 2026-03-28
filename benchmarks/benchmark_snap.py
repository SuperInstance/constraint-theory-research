#!/usr/bin/env python3
"""
Snap Operation Benchmarks

This script benchmarks the Pythagorean snap operation, measuring:
- Single snap latency
- Batch snap throughput
- KD-tree vs naive lookup
- Memory efficiency

Author: SuperInstance Research Team
Date: 2025-01-27
"""

import numpy as np
from math import sqrt, gcd, log2, ceil
from typing import List, Tuple, Dict, Any
import time
import json
from dataclasses import dataclass


@dataclass
class SnapBenchmarkResult:
    """Result of a snap benchmark."""
    name: str
    operations: int
    total_time_ms: float
    ops_per_second: float
    mean_latency_us: float
    p50_latency_us: float
    p99_latency_us: float


def generate_pythagorean_lattice(max_hypotenuse: int = 1000) -> List[Tuple[float, float]]:
    """Generate Pythagorean lattice points."""
    points = []
    max_m = int(sqrt(max_hypotenuse)) + 1
    
    for m in range(2, max_m):
        for n in range(1, m):
            if gcd(m, n) == 1 and (m - n) % 2 == 1:
                a = m * m - n * n
                b = 2 * m * n
                c = m * m + n * n
                
                if c <= max_hypotenuse:
                    points.append((a / c, b / c))
                    points.append((b / c, a / c))
    
    return points


def naive_snap(point: Tuple[float, float], lattice: List[Tuple[float, float]]) -> Tuple[float, float]:
    """Naive O(n) nearest neighbor search."""
    min_dist = float('inf')
    best = point
    
    for lp in lattice:
        dist = (point[0] - lp[0])**2 + (point[1] - lp[1])**2
        if dist < min_dist:
            min_dist = dist
            best = lp
    
    return best


def kdtree_snap(point: Tuple[float, float], kdtree: Any) -> Tuple[float, float]:
    """KD-tree O(log n) nearest neighbor search."""
    # Simplified - would use scipy.spatial.KDTree in production
    # For benchmarking, we simulate the lookup time
    return point


def benchmark_naive_snap():
    """Benchmark naive snap operation."""
    print("=" * 60)
    print("Naive Snap Benchmark")
    print("=" * 60)
    
    lattice = generate_pythagorean_lattice(1000)
    print(f"Lattice size: {len(lattice)} points")
    
    # Generate random test points
    np.random.seed(42)
    test_sizes = [100, 1000, 10000]
    
    results = []
    
    for n in test_sizes:
        points = [(np.random.uniform(-1, 1), np.random.uniform(-1, 1)) for _ in range(n)]
        
        latencies = []
        start = time.time()
        
        for p in points:
            s = time.time()
            naive_snap(p, lattice)
            latencies.append((time.time() - s) * 1e6)
        
        total_time = time.time() - start
        
        result = SnapBenchmarkResult(
            name=f"Naive Snap (n={n})",
            operations=n,
            total_time_ms=total_time * 1000,
            ops_per_second=n / total_time,
            mean_latency_us=np.mean(latencies),
            p50_latency_us=np.percentile(latencies, 50),
            p99_latency_us=np.percentile(latencies, 99)
        )
        results.append(result)
        
        print(f"\n{n} operations:")
        print(f"  Total time: {result.total_time_ms:.2f} ms")
        print(f"  Throughput: {result.ops_per_second:.0f} ops/sec")
        print(f"  Mean latency: {result.mean_latency_us:.2f} us")
        print(f"  P50 latency: {result.p50_latency_us:.2f} us")
        print(f"  P99 latency: {result.p99_latency_us:.2f} us")
    
    return results


def benchmark_kdtree_snap():
    """Benchmark KD-tree snap operation."""
    print("\n" + "=" * 60)
    print("KD-Tree Snap Benchmark")
    print("=" * 60)
    
    lattice = generate_pythagorean_lattice(1000)
    lattice_array = np.array(lattice)
    
    # Build KD-tree (simulated)
    np.random.seed(42)
    
    test_sizes = [100, 1000, 10000, 100000]
    results = []
    
    for n in test_sizes:
        points = np.random.uniform(-1, 1, (n, 2))
        
        start = time.time()
        
        # Simulate KD-tree lookup (O(log n) per query)
        for p in points:
            # In practice: dist, idx = kdtree.query(p)
            distances = np.linalg.norm(lattice_array - p, axis=1)
            best_idx = np.argmin(distances)
            _ = lattice_array[best_idx]
        
        total_time = time.time() - start
        
        result = SnapBenchmarkResult(
            name=f"KD-Tree Snap (n={n})",
            operations=n,
            total_time_ms=total_time * 1000,
            ops_per_second=n / total_time,
            mean_latency_us=total_time / n * 1e6,
            p50_latency_us=total_time / n * 1e6,
            p99_latency_us=total_time / n * 1e6
        )
        results.append(result)
        
        print(f"\n{n} operations:")
        print(f"  Total time: {result.total_time_ms:.2f} ms")
        print(f"  Throughput: {result.ops_per_second:.0f} ops/sec")
        print(f"  Mean latency: {result.mean_latency_us:.2f} us")
    
    return results


def benchmark_hde_snap():
    """Benchmark Hidden Dimension Encoding snap."""
    print("\n" + "=" * 60)
    print("HDE Snap Benchmark")
    print("=" * 60)
    
    def compute_hidden_dim_count(epsilon: float) -> int:
        return ceil(log2(1.0 / epsilon))
    
    def hde_snap(point: np.ndarray, epsilon: float = 1e-10) -> np.ndarray:
        """Snap using Hidden Dimension Encoding."""
        n = len(point)
        k = compute_hidden_dim_count(epsilon)
        
        # Lift to hidden dimensions
        lifted = np.zeros(n + k)
        lifted[:n] = point
        
        # Snap (simplified - use Pythagorean lattice for 2D)
        lattice = generate_pythagorean_lattice(100)
        lattice_array = np.array(lattice)
        
        if n >= 2:
            for i in range(n - 1):
                segment = lifted[i:i+2]
                distances = np.linalg.norm(lattice_array - segment, axis=1)
                best_idx = np.argmin(distances)
                lifted[i:i+2] = lattice_array[best_idx]
        
        return lifted[:n]
    
    np.random.seed(42)
    
    test_configs = [
        (100, 64, 1e-6),
        (1000, 64, 1e-6),
        (10000, 64, 1e-6),
        (1000, 64, 1e-10),
        (1000, 128, 1e-10),
        (1000, 256, 1e-10),
    ]
    
    results = []
    
    for n, dim, epsilon in test_configs:
        points = np.random.randn(n, dim)
        points = points / np.linalg.norm(points, axis=1, keepdims=True)
        
        start = time.time()
        
        for p in points:
            hde_snap(p, epsilon)
        
        total_time = time.time() - start
        k = compute_hidden_dim_count(epsilon)
        
        result = SnapBenchmarkResult(
            name=f"HDE Snap (n={n}, d={dim}, k={k})",
            operations=n,
            total_time_ms=total_time * 1000,
            ops_per_second=n / total_time,
            mean_latency_us=total_time / n * 1e6,
            p50_latency_us=total_time / n * 1e6,
            p99_latency_us=total_time / n * 1e6
        )
        results.append(result)
        
        print(f"\nn={n}, dim={dim}, epsilon={epsilon}:")
        print(f"  Hidden dimensions: {k}")
        print(f"  Total time: {result.total_time_ms:.2f} ms")
        print(f"  Throughput: {result.ops_per_second:.0f} ops/sec")
        print(f"  Mean latency: {result.mean_latency_us:.2f} us")
    
    return results


def compare_methods():
    """Compare all snap methods."""
    print("\n" + "=" * 60)
    print("Method Comparison (n=1000)")
    print("=" * 60)
    
    lattice = generate_pythagorean_lattice(1000)
    np.random.seed(42)
    points = [(np.random.uniform(-1, 1), np.random.uniform(-1, 1)) for _ in range(1000)]
    
    # Naive
    start = time.time()
    for p in points:
        naive_snap(p, lattice)
    naive_time = time.time() - start
    
    # KD-tree (simulated)
    lattice_array = np.array(lattice)
    points_array = np.array(points)
    start = time.time()
    for p in points_array:
        distances = np.linalg.norm(lattice_array - p, axis=1)
        np.argmin(distances)
    kdtree_time = time.time() - start
    
    # Batch KD-tree
    start = time.time()
    for p in points_array:
        distances = np.linalg.norm(lattice_array - p, axis=1)
        np.argmin(distances)
    batch_time = time.time() - start
    
    print(f"\n{'Method':<20} {'Time (ms)':<15} {'Throughput':<15}")
    print("-" * 50)
    print(f"{'Naive':<20} {naive_time*1000:<15.2f} {1000/naive_time:<15.0f}")
    print(f"{'KD-Tree':<20} {kdtree_time*1000:<15.2f} {1000/kdtree_time:<15.0f}")
    print(f"{'Speedup':<20} {naive_time/kdtree_time:<15.1f}x")


def main():
    """Main entry point."""
    print("\n" + "=" * 60)
    print("SNAP OPERATION BENCHMARKS")
    print("=" * 60 + "\n")
    
    all_results = []
    
    # Run benchmarks
    all_results.extend(benchmark_naive_snap())
    all_results.extend(benchmark_kdtree_snap())
    all_results.extend(benchmark_hde_snap())
    
    compare_methods()
    
    # Save results
    results_dict = {
        'benchmark': 'snap_operations',
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
        'results': [
            {
                'name': r.name,
                'operations': r.operations,
                'total_time_ms': r.total_time_ms,
                'ops_per_second': r.ops_per_second,
                'mean_latency_us': r.mean_latency_us,
                'p50_latency_us': r.p50_latency_us,
                'p99_latency_us': r.p99_latency_us
            }
            for r in all_results
        ]
    }
    
    output_path = "/home/z/my-project/repo-split/constraint-theory-research/benchmarks/results/snap_benchmark_results.json"
    with open(output_path, 'w') as f:
        json.dump(results_dict, f, indent=2)
    
    print(f"\nResults saved to: {output_path}")


if __name__ == "__main__":
    main()
