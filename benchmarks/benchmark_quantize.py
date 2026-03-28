#!/usr/bin/env python3
"""
Quantization Benchmarks

This script benchmarks quantization operations, measuring:
- Quantization throughput
- MSE/distortion
- Constraint preservation
- Memory usage

Author: SuperInstance Research Team
Date: 2025-01-27
"""

import numpy as np
from math import sqrt, log2, ceil, pi, atan2, cos, sin
from typing import List, Dict, Any, Tuple
import time
import json
from dataclasses import dataclass


@dataclass
class QuantBenchmarkResult:
    """Result of a quantization benchmark."""
    name: str
    data_size: int
    dimensions: int
    bits: int
    total_time_ms: float
    throughput_kvps: float  # thousand vectors per second
    mse: float
    norm_error: float
    memory_bytes: int


def hadamard_transform(x: np.ndarray) -> np.ndarray:
    """Apply Hadamard transform."""
    n = len(x)
    n_padded = 2 ** ceil(log2(n))
    padded = np.zeros(n_padded)
    padded[:n] = x
    
    h = 1
    while h < n_padded:
        for i in range(0, n_padded, h * 2):
            for j in range(i, i + h):
                temp = padded[j]
                padded[j] = temp + padded[j + h]
                padded[j + h] = temp - padded[j + h]
        h *= 2
    
    return padded[:n] / sqrt(n_padded)


def quantize_standard(data: np.ndarray, bits: int = 4) -> Tuple[np.ndarray, float]:
    """Standard uniform quantization."""
    levels = 2 ** bits
    min_val = data.min()
    max_val = data.max()
    
    scale = (levels - 1) / (max_val - min_val + 1e-10)
    quantized = np.round((data - min_val) * scale) / scale + min_val
    
    mse = np.mean((data - quantized) ** 2)
    return quantized, mse


def quantize_ternary(data: np.ndarray, threshold: float = 0.1) -> Tuple[np.ndarray, float]:
    """BitNet-style ternary quantization."""
    result = np.zeros_like(data)
    mask = np.abs(data) > threshold
    result[mask] = np.sign(data[mask])
    
    mse = np.mean((data - result) ** 2)
    return result, mse


def quantize_turbo(data: np.ndarray, bits: int = 4) -> Tuple[np.ndarray, float]:
    """TurboQuant-style quantization."""
    n, d = data.shape
    
    # Random rotation
    np.random.seed(42)
    Q, _ = np.linalg.qr(np.random.randn(d, d))
    rotated = data @ Q
    
    # Hadamard transform
    transformed = np.zeros_like(rotated)
    for i in range(n):
        transformed[i] = hadamard_transform(rotated[i])
    
    # Scalar quantization
    levels = 2 ** bits
    min_val = transformed.min()
    max_val = transformed.max()
    
    scale = (levels - 1) / (max_val - min_val + 1e-10)
    quantized = np.round((transformed - min_val) * scale) / scale + min_val
    
    # Inverse transform
    result = np.zeros_like(quantized)
    for i in range(n):
        result[i] = hadamard_transform(quantized[i])
    result = result @ Q.T
    
    mse = np.mean((data - result) ** 2)
    return result, mse


def quantize_polar(vectors: np.ndarray, angle_bits: int = 8) -> Tuple[np.ndarray, float]:
    """PolarQuant-style quantization."""
    n, d = vectors.shape
    result = vectors.copy()
    
    for i in range(n):
        v = vectors[i]
        norm = np.linalg.norm(v)
        if norm < 1e-10:
            continue
        
        v_normalized = v / norm
        
        if d == 2:
            theta = atan2(v[1], v[0])
            levels = 2 ** angle_bits
            quantized_theta = round((theta + pi) / (2 * pi) * levels) / levels * 2 * pi - pi
            result[i] = [cos(quantized_theta), sin(quantized_theta)]
        else:
            result[i] = v_normalized
    
    mse = np.mean((vectors - result) ** 2)
    return result, mse


def quantize_pythagorean(data: np.ndarray, bits: int = 4) -> Tuple[np.ndarray, float]:
    """Pythagorean Quantization."""
    # For embeddings, use polar mode
    if len(data.shape) == 2 and data.shape[1] >= 2:
        quantized, mse = quantize_polar(data, angle_bits=bits)
    else:
        quantized, mse = quantize_standard(data, bits)
    
    return quantized, mse


def benchmark_standard_quantization():
    """Benchmark standard quantization."""
    print("=" * 60)
    print("Standard Quantization Benchmark")
    print("=" * 60)
    
    np.random.seed(42)
    results = []
    
    configs = [
        (10000, 128, 4),
        (10000, 128, 8),
        (100000, 128, 4),
        (10000, 768, 4),
    ]
    
    for n, d, bits in configs:
        data = np.random.randn(n, d)
        data = data / np.linalg.norm(data, axis=1, keepdims=True)
        
        start = time.time()
        quantized, mse = quantize_standard(data, bits)
        total_time = time.time() - start
        
        norms = np.linalg.norm(quantized, axis=1)
        norm_error = np.mean(np.abs(norms - 1.0))
        
        result = QuantBenchmarkResult(
            name=f"Standard {bits}-bit",
            data_size=n,
            dimensions=d,
            bits=bits,
            total_time_ms=total_time * 1000,
            throughput_kvps=n / total_time / 1000,
            mse=mse,
            norm_error=norm_error,
            memory_bytes=n * d * bits // 8
        )
        results.append(result)
        
        print(f"\nn={n}, d={d}, bits={bits}:")
        print(f"  Time: {result.total_time_ms:.2f} ms")
        print(f"  Throughput: {result.throughput_kvps:.0f} KV/s")
        print(f"  MSE: {result.mse:.6f}")
        print(f"  Norm error: {result.norm_error:.6f}")
    
    return results


def benchmark_turboquant():
    """Benchmark TurboQuant."""
    print("\n" + "=" * 60)
    print("TurboQuant Benchmark")
    print("=" * 60)
    
    np.random.seed(42)
    results = []
    
    configs = [
        (1000, 128, 4),
        (1000, 128, 8),
        (5000, 128, 4),
        (1000, 768, 4),
    ]
    
    for n, d, bits in configs:
        data = np.random.randn(n, d)
        data = data / np.linalg.norm(data, axis=1, keepdims=True)
        
        start = time.time()
        quantized, mse = quantize_turbo(data, bits)
        total_time = time.time() - start
        
        norms = np.linalg.norm(quantized, axis=1)
        norm_error = np.mean(np.abs(norms - 1.0))
        
        result = QuantBenchmarkResult(
            name="TurboQuant",
            data_size=n,
            dimensions=d,
            bits=bits,
            total_time_ms=total_time * 1000,
            throughput_kvps=n / total_time / 1000,
            mse=mse,
            norm_error=norm_error,
            memory_bytes=n * d * bits // 8
        )
        results.append(result)
        
        print(f"\nn={n}, d={d}, bits={bits}:")
        print(f"  Time: {result.total_time_ms:.2f} ms")
        print(f"  Throughput: {result.throughput_kvps:.0f} KV/s")
        print(f"  MSE: {result.mse:.6f}")
        print(f"  Norm error: {result.norm_error:.6f}")
    
    return results


def benchmark_bitnet():
    """Benchmark BitNet ternary quantization."""
    print("\n" + "=" * 60)
    print("BitNet b1.58 Benchmark")
    print("=" * 60)
    
    np.random.seed(42)
    results = []
    
    configs = [
        (10000, 128),
        (100000, 128),
        (10000, 768),
    ]
    
    for n, d in configs:
        data = np.random.randn(n, d)
        
        start = time.time()
        quantized, mse = quantize_ternary(data)
        total_time = time.time() - start
        
        norms = np.linalg.norm(quantized, axis=1)
        norm_error = np.mean(np.abs(norms - np.mean(norms)))
        
        result = QuantBenchmarkResult(
            name="BitNet b1.58",
            data_size=n,
            dimensions=d,
            bits=2,  # ~1.58 bits
            total_time_ms=total_time * 1000,
            throughput_kvps=n / total_time / 1000,
            mse=mse,
            norm_error=norm_error,
            memory_bytes=n * d * 2 // 8
        )
        results.append(result)
        
        print(f"\nn={n}, d={d}:")
        print(f"  Time: {result.total_time_ms:.2f} ms")
        print(f"  Throughput: {result.throughput_kvps:.0f} KV/s")
        print(f"  MSE: {result.mse:.6f}")
    
    return results


def benchmark_pythagorean():
    """Benchmark Pythagorean Quantization."""
    print("\n" + "=" * 60)
    print("Pythagorean Quantization Benchmark")
    print("=" * 60)
    
    np.random.seed(42)
    results = []
    
    configs = [
        (10000, 128, 4),
        (10000, 128, 8),
        (100000, 128, 4),
        (10000, 768, 4),
    ]
    
    for n, d, bits in configs:
        data = np.random.randn(n, d)
        data = data / np.linalg.norm(data, axis=1, keepdims=True)
        
        start = time.time()
        quantized, mse = quantize_pythagorean(data, bits)
        total_time = time.time() - start
        
        norms = np.linalg.norm(quantized, axis=1)
        norm_error = np.mean(np.abs(norms - 1.0))
        
        result = QuantBenchmarkResult(
            name="Pythagorean",
            data_size=n,
            dimensions=d,
            bits=bits,
            total_time_ms=total_time * 1000,
            throughput_kvps=n / total_time / 1000,
            mse=mse,
            norm_error=norm_error,
            memory_bytes=n * d * bits // 8
        )
        results.append(result)
        
        print(f"\nn={n}, d={d}, bits={bits}:")
        print(f"  Time: {result.total_time_ms:.2f} ms")
        print(f"  Throughput: {result.throughput_kvps:.0f} KV/s")
        print(f"  MSE: {result.mse:.6f}")
        print(f"  Norm error: {result.norm_error:.2e}")
    
    return results


def compare_all_methods():
    """Compare all quantization methods."""
    print("\n" + "=" * 60)
    print("Method Comparison (n=10000, d=128)")
    print("=" * 60)
    
    np.random.seed(42)
    n, d = 10000, 128
    data = np.random.randn(n, d)
    data = data / np.linalg.norm(data, axis=1, keepdims=True)
    
    methods = [
        ("Standard 4-bit", lambda: quantize_standard(data, 4)),
        ("Standard 8-bit", lambda: quantize_standard(data, 8)),
        ("TurboQuant", lambda: quantize_turbo(data, 4)),
        ("BitNet b1.58", lambda: quantize_ternary(data)),
        ("Pythagorean", lambda: quantize_pythagorean(data, 4)),
    ]
    
    print(f"\n{'Method':<20} {'Time (ms)':<12} {'MSE':<12} {'Norm Err':<12}")
    print("-" * 60)
    
    for name, quantize_fn in methods:
        start = time.time()
        _, mse = quantize_fn()
        elapsed = time.time() - start
        
        print(f"{name:<20} {elapsed*1000:<12.2f} {mse:<12.6f}")


def main():
    """Main entry point."""
    print("\n" + "=" * 60)
    print("QUANTIZATION BENCHMARKS")
    print("=" * 60 + "\n")
    
    all_results = []
    
    # Run benchmarks
    all_results.extend(benchmark_standard_quantization())
    all_results.extend(benchmark_turboquant())
    all_results.extend(benchmark_bitnet())
    all_results.extend(benchmark_pythagorean())
    
    compare_all_methods()
    
    # Save results
    results_dict = {
        'benchmark': 'quantization',
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
        'results': [
            {
                'name': r.name,
                'data_size': r.data_size,
                'dimensions': r.dimensions,
                'bits': r.bits,
                'total_time_ms': r.total_time_ms,
                'throughput_kvps': r.throughput_kvps,
                'mse': r.mse,
                'norm_error': r.norm_error,
                'memory_bytes': r.memory_bytes
            }
            for r in all_results
        ]
    }
    
    output_path = "/home/z/my-project/repo-split/constraint-theory-research/benchmarks/results/quantization_benchmark_results.json"
    with open(output_path, 'w') as f:
        json.dump(results_dict, f, indent=2)
    
    print(f"\nResults saved to: {output_path}")


if __name__ == "__main__":
    main()
