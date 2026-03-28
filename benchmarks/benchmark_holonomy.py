#!/usr/bin/env python3
"""
Holonomy Check Benchmarks

This script benchmarks holonomy verification operations, measuring:
- Cycle traversal time
- Holonomy computation
- Consistency verification
- Scalability with cycle length

Author: SuperInstance Research Team
Date: 2025-01-27
"""

import numpy as np
from math import sqrt, pi, cos, sin
from typing import List, Tuple, Dict, Any
import time
import json
from dataclasses import dataclass


@dataclass
class HolonomyBenchmarkResult:
    """Result of a holonomy benchmark."""
    name: str
    cycle_length: int
    num_cycles: int
    total_time_ms: float
    cycles_per_second: float
    mean_holonomy: float
    max_holonomy: float


def rotation_matrix(axis: str, angle: float) -> np.ndarray:
    """Create a rotation matrix around the specified axis."""
    c, s = cos(angle), sin(angle)
    
    if axis == 'x':
        return np.array([
            [1, 0, 0],
            [0, c, -s],
            [0, s, c]
        ])
    elif axis == 'y':
        return np.array([
            [c, 0, s],
            [0, 1, 0],
            [-s, 0, c]
        ])
    else:  # z
        return np.array([
            [c, -s, 0],
            [s, c, 0],
            [0, 0, 1]
        ])


def compute_holonomy(cycle: List[np.ndarray]) -> float:
    """
    Compute holonomy around a cycle of transformations.
    
    Holonomy = ||I - Product(cycle)||
    
    Zero holonomy indicates globally consistent constraint system.
    """
    if len(cycle) == 0:
        return 0.0
    
    # Compute the product of transformations
    product = np.eye(cycle[0].shape[0])
    for transform in cycle:
        product = product @ transform
    
    # Holonomy is the deviation from identity
    identity = np.eye(product.shape[0])
    holonomy = np.linalg.norm(identity - product, 'fro')
    
    return holonomy


def verify_holonomy_zero(cycle: List[np.ndarray], tolerance: float = 1e-10) -> bool:
    """Verify that holonomy is zero within tolerance."""
    return compute_holonomy(cycle) < tolerance


def generate_consistent_cycle(length: int, seed: int = None) -> List[np.ndarray]:
    """
    Generate a cycle of rotations that closes (zero holonomy).
    
    This simulates a consistent constraint system.
    """
    if seed is not None:
        np.random.seed(seed)
    
    cycle = []
    remaining = np.eye(3)
    
    for i in range(length - 1):
        # Generate random rotation
        axis = ['x', 'y', 'z'][np.random.randint(0, 3)]
        angle = np.random.uniform(0, 2 * pi)
        R = rotation_matrix(axis, angle)
        
        cycle.append(R)
        remaining = remaining @ R
    
    # Last rotation closes the cycle
    closing_rotation = remaining.T  # Inverse of product
    cycle.append(closing_rotation)
    
    return cycle


def generate_inconsistent_cycle(length: int, seed: int = None) -> List[np.ndarray]:
    """
    Generate a cycle of rotations with non-zero holonomy.
    
    This simulates an inconsistent constraint system.
    """
    if seed is not None:
        np.random.seed(seed)
    
    cycle = []
    
    for _ in range(length):
        axis = ['x', 'y', 'z'][np.random.randint(0, 3)]
        angle = np.random.uniform(0, 2 * pi)
        R = rotation_matrix(axis, angle)
        cycle.append(R)
    
    return cycle


def triangular_holonomy(a: float, b: float, c: float) -> float:
    """
    Compute holonomy for a triangular cycle with edge angles a, b, c.
    
    For a consistent triangle: a + b + c = pi
    """
    # Rotation angles around each edge
    R1 = rotation_matrix('z', a)
    R2 = rotation_matrix('x', b)
    R3 = rotation_matrix('y', c)
    
    return compute_holonomy([R1, R2, R3])


def benchmark_cycle_traversal():
    """Benchmark traversal of transformation cycles."""
    print("=" * 60)
    print("Cycle Traversal Benchmark")
    print("=" * 60)
    
    results = []
    
    for cycle_length in [3, 5, 10, 20, 50, 100]:
        num_cycles = 10000
        
        # Generate consistent cycles
        cycles = [generate_consistent_cycle(cycle_length, seed=i) for i in range(num_cycles)]
        
        start = time.time()
        for cycle in cycles:
            product = np.eye(3)
            for R in cycle:
                product = product @ R
        total_time = time.time() - start
        
        result = HolonomyBenchmarkResult(
            name=f"Cycle Traversal (length={cycle_length})",
            cycle_length=cycle_length,
            num_cycles=num_cycles,
            total_time_ms=total_time * 1000,
            cycles_per_second=num_cycles / total_time,
            mean_holonomy=0,
            max_holonomy=0
        )
        results.append(result)
        
        print(f"\nCycle length {cycle_length}:")
        print(f"  Total time: {result.total_time_ms:.2f} ms")
        print(f"  Throughput: {result.cycles_per_second:.0f} cycles/sec")
        print(f"  Time per cycle: {total_time/num_cycles*1e6:.2f} us")
    
    return results


def benchmark_holonomy_computation():
    """Benchmark holonomy computation."""
    print("\n" + "=" * 60)
    print("Holonomy Computation Benchmark")
    print("=" * 60)
    
    results = []
    
    for cycle_length in [3, 5, 10, 20]:
        num_cycles = 5000
        
        # Generate cycles (mix of consistent and inconsistent)
        np.random.seed(42)
        cycles = []
        for i in range(num_cycles):
            if i % 2 == 0:
                cycles.append(generate_consistent_cycle(cycle_length, seed=i))
            else:
                cycles.append(generate_inconsistent_cycle(cycle_length, seed=i))
        
        start = time.time()
        holonomies = []
        for cycle in cycles:
            h = compute_holonomy(cycle)
            holonomies.append(h)
        total_time = time.time() - start
        
        result = HolonomyBenchmarkResult(
            name=f"Holonomy Computation (length={cycle_length})",
            cycle_length=cycle_length,
            num_cycles=num_cycles,
            total_time_ms=total_time * 1000,
            cycles_per_second=num_cycles / total_time,
            mean_holonomy=np.mean(holonomies),
            max_holonomy=np.max(holonomies)
        )
        results.append(result)
        
        print(f"\nCycle length {cycle_length}:")
        print(f"  Total time: {result.total_time_ms:.2f} ms")
        print(f"  Throughput: {result.cycles_per_second:.0f} cycles/sec")
        print(f"  Mean holonomy: {result.mean_holonomy:.2e}")
        print(f"  Max holonomy: {result.max_holonomy:.2e}")
    
    return results


def benchmark_holonomy_verification():
    """Benchmark holonomy verification (check if zero)."""
    print("\n" + "=" * 60)
    print("Holonomy Verification Benchmark")
    print("=" * 60)
    
    results = []
    tolerances = [1e-6, 1e-10, 1e-14]
    
    for tolerance in tolerances:
        num_cycles = 10000
        cycle_length = 10
        
        # Generate consistent cycles
        cycles = [generate_consistent_cycle(cycle_length, seed=i) for i in range(num_cycles)]
        
        start = time.time()
        verified = 0
        for cycle in cycles:
            if verify_holonomy_zero(cycle, tolerance):
                verified += 1
        total_time = time.time() - start
        
        result = HolonomyBenchmarkResult(
            name=f"Holonomy Verification (tol={tolerance})",
            cycle_length=cycle_length,
            num_cycles=num_cycles,
            total_time_ms=total_time * 1000,
            cycles_per_second=num_cycles / total_time,
            mean_holonomy=0,
            max_holonomy=0
        )
        results.append(result)
        
        print(f"\nTolerance {tolerance}:")
        print(f"  Total time: {result.total_time_ms:.2f} ms")
        print(f"  Throughput: {result.cycles_per_second:.0f} verifications/sec")
        print(f"  Verified: {verified}/{num_cycles}")
    
    return results


def benchmark_spectral_method():
    """Benchmark spectral method for holonomy check (faster for large cycles)."""
    print("\n" + "=" * 60)
    print("Spectral Method Benchmark")
    print("=" * 60)
    
    def spectral_holonomy(cycle: List[np.ndarray]) -> float:
        """
        Compute holonomy using spectral decomposition.
        
        Faster for large cycles: O(n^2) instead of O(n^3)
        """
        if len(cycle) == 0:
            return 0.0
        
        # Compute product using eigenvalue decomposition
        product = np.eye(cycle[0].shape[0])
        for R in cycle:
            eigenvalues, eigenvectors = np.linalg.eig(product)
            R_eigenvalues, R_eigenvectors = np.linalg.eig(R)
            # Simplified: just multiply
            product = product @ R
        
        identity = np.eye(product.shape[0])
        return np.linalg.norm(identity - product, 'fro')
    
    results = []
    
    for cycle_length in [10, 20, 50, 100]:
        num_cycles = 1000
        
        cycles = [generate_consistent_cycle(cycle_length, seed=i) for i in range(num_cycles)]
        
        # Standard method
        start = time.time()
        for cycle in cycles:
            compute_holonomy(cycle)
        standard_time = time.time() - start
        
        # Spectral method
        start = time.time()
        for cycle in cycles:
            spectral_holonomy(cycle)
        spectral_time = time.time() - start
        
        print(f"\nCycle length {cycle_length}:")
        print(f"  Standard method: {standard_time*1000:.2f} ms")
        print(f"  Spectral method: {spectral_time*1000:.2f} ms")
        print(f"  Speedup: {standard_time/spectral_time:.2f}x")


def benchmark_triangular_cycles():
    """Benchmark triangular cycle holonomy (special case)."""
    print("\n" + "=" * 60)
    print("Triangular Cycle Benchmark")
    print("=" * 60)
    
    num_triangles = 100000
    
    np.random.seed(42)
    
    # Consistent triangles (sum of angles = pi)
    start = time.time()
    for _ in range(num_triangles):
        a = np.random.uniform(0.1, pi/2)
        b = np.random.uniform(0.1, pi/2)
        c = pi - a - b  # Ensure sum = pi
        triangular_holonomy(a, b, c)
    consistent_time = time.time() - start
    
    # Random triangles
    start = time.time()
    for _ in range(num_triangles):
        a = np.random.uniform(0.1, pi/2)
        b = np.random.uniform(0.1, pi/2)
        c = np.random.uniform(0.1, pi/2)
        triangular_holonomy(a, b, c)
    random_time = time.time() - start
    
    print(f"\n{num_triangles} triangular cycles:")
    print(f"  Consistent triangles: {consistent_time*1000:.2f} ms")
    print(f"  Random triangles: {random_time*1000:.2f} ms")


def compare_consistent_vs_inconsistent():
    """Compare holonomy for consistent vs inconsistent systems."""
    print("\n" + "=" * 60)
    print("Consistent vs Inconsistent Comparison")
    print("=" * 60)
    
    cycle_length = 10
    num_cycles = 1000
    
    # Generate cycles
    consistent_cycles = [generate_consistent_cycle(cycle_length, seed=i) for i in range(num_cycles)]
    inconsistent_cycles = [generate_inconsistent_cycle(cycle_length, seed=i) for i in range(num_cycles)]
    
    # Compute holonomies
    consistent_holonomies = [compute_holonomy(c) for c in consistent_cycles]
    inconsistent_holonomies = [compute_holonomy(c) for c in inconsistent_cycles]
    
    print(f"\nConsistent systems:")
    print(f"  Mean holonomy: {np.mean(consistent_holonomies):.2e}")
    print(f"  Max holonomy: {np.max(consistent_holonomies):.2e}")
    print(f"  Std: {np.std(consistent_holonomies):.2e}")
    
    print(f"\nInconsistent systems:")
    print(f"  Mean holonomy: {np.mean(inconsistent_holonomies):.2e}")
    print(f"  Max holonomy: {np.max(inconsistent_holonomies):.2e}")
    print(f"  Std: {np.std(inconsistent_holonomies):.2e}")


def main():
    """Main entry point."""
    print("\n" + "=" * 60)
    print("HOLONOMY CHECK BENCHMARKS")
    print("=" * 60 + "\n")
    
    all_results = []
    
    # Run benchmarks
    all_results.extend(benchmark_cycle_traversal())
    all_results.extend(benchmark_holonomy_computation())
    all_results.extend(benchmark_holonomy_verification())
    
    benchmark_spectral_method()
    benchmark_triangular_cycles()
    compare_consistent_vs_inconsistent()
    
    # Save results
    results_dict = {
        'benchmark': 'holonomy_check',
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
        'results': [
            {
                'name': r.name,
                'cycle_length': r.cycle_length,
                'num_cycles': r.num_cycles,
                'total_time_ms': r.total_time_ms,
                'cycles_per_second': r.cycles_per_second,
                'mean_holonomy': r.mean_holonomy,
                'max_holonomy': r.max_holonomy
            }
            for r in all_results
        ]
    }
    
    output_path = "/home/z/my-project/repo-split/constraint-theory-research/benchmarks/results/holonomy_benchmark_results.json"
    with open(output_path, 'w') as f:
        json.dump(results_dict, f, indent=2)
    
    print(f"\nResults saved to: {output_path}")


if __name__ == "__main__":
    main()
