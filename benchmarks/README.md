# Constraint Theory Benchmark Suite

This directory contains benchmarks for validating and measuring the performance of Constraint Theory implementations.

## Directory Structure

```
benchmarks/
├── README.md                    # This file
├── run_all_benchmarks.py        # Run all benchmarks
├── benchmark_snap.py            # Snap operation benchmarks
├── benchmark_quantize.py        # Quantization benchmarks
├── benchmark_holonomy.py        # Holonomy check benchmarks
└── results/                     # Benchmark results (JSON)
    ├── snap_benchmark_results.json
    ├── quantization_benchmark_results.json
    ├── holonomy_benchmark_results.json
    └── benchmark_summary.json
```

## Running Benchmarks

### Run All Benchmarks

```bash
python run_all_benchmarks.py
```

### Run Individual Benchmarks

```bash
# Snap operation benchmarks
python benchmark_snap.py

# Quantization benchmarks
python benchmark_quantize.py

# Holonomy check benchmarks
python benchmark_holonomy.py
```

## Benchmark Descriptions

### 1. Snap Operation Benchmarks (`benchmark_snap.py`)

Measures performance of Pythagorean snap operations:
- **Naive Snap**: O(n) linear search through lattice
- **KD-Tree Snap**: O(log n) nearest neighbor search
- **HDE Snap**: Hidden Dimension Encoding snap

Key metrics:
- Operations per second
- Mean latency (microseconds)
- P50/P99 latency

### 2. Quantization Benchmarks (`benchmark_quantize.py`)

Compares quantization methods:
- **Standard**: Uniform scalar quantization
- **TurboQuant**: Near-optimal distortion with rotation
- **BitNet b1.58**: Ternary quantization {-1, 0, +1}
- **PolarQuant**: Unit norm preserving polar quantization
- **Pythagorean**: Constraint-preserving quantization

Key metrics:
- MSE (Mean Squared Error)
- Norm error
- Throughput (KV/s)
- Memory usage

### 3. Holonomy Check Benchmarks (`benchmark_holonomy.py`)

Measures performance of holonomy verification:
- Cycle traversal
- Holonomy computation
- Consistency verification
- Spectral vs standard methods

Key metrics:
- Cycles per second
- Mean holonomy
- Max holonomy

## Expected Results

### Snap Operations

| Method | Throughput | Latency |
|--------|------------|---------|
| Naive | ~1,000 ops/s | ~1,000 µs |
| KD-Tree | ~100,000 ops/s | ~10 µs |
| HDE | ~50,000 ops/s | ~20 µs |

### Quantization

| Method | MSE | Norm Error |
|--------|-----|------------|
| Standard 4-bit | 0.012 | 0.05 |
| TurboQuant | 0.003 | 0.002 |
| BitNet b1.58 | 0.038 | 0.01 |
| Pythagorean | 0.002 | <1e-15 |

### Holonomy

| Cycle Length | Throughput | Mean Holonomy |
|--------------|------------|---------------|
| 3 | ~100,000/s | <1e-15 |
| 10 | ~50,000/s | <1e-15 |
| 50 | ~10,000/s | <1e-14 |
| 100 | ~5,000/s | <1e-14 |

## Dependencies

- Python 3.8+
- NumPy
- SciPy (optional, for optimized KD-Tree)

## Results Format

All results are saved in JSON format:

```json
{
  "benchmark": "benchmark_name",
  "timestamp": "2025-01-27T12:00:00",
  "results": [
    {
      "name": "Test Name",
      "metric1": value1,
      "metric2": value2
    }
  ]
}
```

## Related Documentation

- Paper 4: Hidden Dimension Encoding
- Paper 5: Pythagorean Quantization
- Master Integration Schema
- BENCHMARK_METHODOLOGY.md
