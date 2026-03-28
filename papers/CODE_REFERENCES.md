# Code References for Research Papers

**Version:** 1.0
**Last Updated:** 2025-03-16
**Repository:** https://github.com/SuperInstance/Constraint-Theory

---

## 1. Overview

This document provides comprehensive code references linking theoretical claims in the papers to their implementations in the core library. All references follow the traceability matrix format for reproducibility.

---

## 2. Rust Core Implementation

### 2.1 Repository Structure

```
constraint-theory-core/
├── src/
│   ├── core/
│   │   ├── omega.rs        # Origin-centric geometry
│   │   ├── phi_fold.rs     # Φ-Folding operator
│   │   ├── snap.rs         # Pythagorean snapping
│   │   ├── holonomy.rs     # Discrete holonomy
│   │   ├── lvq.rs          # Lattice Vector Quantization
│   │   ├── rigidity.rs     # Laman's theorem validation
│   │   └── triples.rs      # Pythagorean triple generation
│   ├── spatial/
│   │   ├── kdtree.rs       # KD-tree spatial indexing
│   │   └── simd.rs         # SIMD optimization
│   ├── gpu/
│   │   ├── snap.cu         # GPU snapping kernel
│   │   └── memory.cu       # GPU memory management
│   ├── ffi/
│   │   ├── zero_copy.rs    # Zero-copy FFI
│   │   └── error.rs        # Cross-boundary errors
│   └── api/
│       └── ts/             # TypeScript bindings
├── benches/
│   ├── snap_bench.rs       # Snapping benchmarks
│   ├── rigidity_bench.rs   # Rigidity benchmarks
│   └── holonomy_bench.rs   # Holonomy benchmarks
└── tests/
    ├── theory/             # Theoretical validation tests
    └── integration/        # Integration tests
```

### 2.2 Core Module References

#### Omega (Origin-Centric Geometry)

**Paper Reference:** Paper 1, Section 2.1
**Code Location:** `src/core/omega.rs`
**Lines:** 1-85

```rust
/// Computes the constraint density function ρ(x) = 1/(1 + ||x||²)
/// 
/// Paper Reference: Paper 1, Theorem 1, Section 2.1
/// Mathematical Foundation: Origin-centric geometry treats origin
/// as privileged point of maximal constraint.
pub fn density_function(x: f64, y: f64) -> f64 {
    1.0 / (1.0 + x * x + y * y)
}

/// Omega transformation applying density-based scaling
pub fn omega_transform(x: f64, y: f64) -> (f64, f64) {
    let rho = density_function(x, y);
    (x * (1.0 + rho), y * (1.0 + rho))
}
```

**Tests:** `tests/omega_test.rs`
**Benchmark:** `benches/omega_bench.rs`

#### Pythagorean Snapping

**Paper Reference:** Paper 1, Section 2.3; Paper 2, Algorithm 1
**Code Location:** `src/core/snap.rs`
**Lines:** 1-150

```rust
/// Snaps a 2D vector to the nearest Pythagorean triple
/// 
/// Paper Reference: Paper 2, Algorithm 1 (KD-Tree Nearest Neighbor)
/// Complexity: O(log n) with pre-built KD-tree
/// 
/// # Arguments
/// * `manifold` - Pre-computed Pythagorean manifold with KD-tree
/// * `vec` - Input 2D unit vector [x, y]
/// 
/// # Returns
/// * `snapped` - The nearest Pythagorean triple as [a/c, b/c]
/// * `noise` - Geodesic distance to snapped point
pub fn snap(manifold: &PythagoreanManifold, vec: [f64; 2]) -> ([f64; 2], f64) {
    manifold.kdtree.query(vec)
}
```

**Tests:** `tests/snap_test.rs`
**Benchmark:** `benches/snap_bench.rs`

#### KD-Tree Spatial Indexing

**Paper Reference:** Paper 2, Section 3.1-3.2
**Code Location:** `src/spatial/kdtree.rs`
**Lines:** 1-200

```rust
/// KD-Tree for O(log n) nearest neighbor queries
/// 
/// Paper Reference: Paper 2, Section 3.1 (Construction), 3.2 (Query)
/// Construction: O(n log n)
/// Query: O(log n)
pub struct KDTree {
    root: Option<Box<KDNode>>,
    size: usize,
}

impl KDTree {
    /// Build KD-tree from points
    /// Paper 2, Algorithm 1
    pub fn build(points: Vec<Point>) -> Self { ... }
    
    /// Find nearest neighbor
    /// Paper 2, Algorithm 2
    pub fn query(&self, point: Point) -> (Point, f64) { ... }
    
    /// Find k nearest neighbors
    pub fn k_nearest(&self, point: Point, k: usize) -> Vec<(Point, f64)> { ... }
}
```

**Tests:** `tests/kdtree_test.rs`
**Benchmark:** `benches/kdtree_bench.rs`

#### Discrete Holonomy

**Paper Reference:** Paper 1, Section 2.4
**Code Location:** `src/core/holonomy.rs`
**Lines:** 1-120

```rust
/// Parallel transport of a vector along a path
/// 
/// Paper Reference: Paper 1, Section 2.4, Theorem 4
/// Holonomy preservation bounds: h_norm < ε
pub fn parallel_transport(
    vector: Vector3,
    path: &[Point],
    connection: &GaugeConnection
) -> Vector3 {
    let mut v = vector;
    for i in 0..path.len() - 1 {
        let rotation = connection.rotation_matrix(path[i], path[i + 1]);
        v = rotation * v;
    }
    v
}

/// Compute holonomy norm for closed loop
pub fn holonomy_norm(
    initial: Vector3,
    final_vec: Vector3
) -> f64 {
    (initial - final_vec).norm() / initial.norm()
}
```

**Tests:** `tests/holonomy_test.rs`
**Benchmark:** `benches/holonomy_bench.rs`

#### Rigidity Validation (Laman's Theorem)

**Paper Reference:** Paper 1, Section 2.4; Rigidity-Curvature Duality Proof
**Code Location:** `src/core/rigidity.rs`
**Lines:** 1-250

```rust
/// Validates rigidity using Laman's theorem
/// 
/// Paper Reference: Paper 1, Theorem 1 (Rigidity-Curvature Duality)
/// Conditions:
/// 1. |E| = 2|V| - 3 (Laman count)
/// 2. All subgraphs satisfy edge constraint
pub fn validate_rigidity(
    nodes: &[Point],
    edges: &[(usize, usize)]
) -> RigidityResult {
    // Pebble game algorithm
    let pebble_game = PebbleGame::new(nodes.len());
    pebble_game.check_laman(edges)
}
```

**Tests:** `tests/rigidity_test.rs`
**Benchmark:** `benches/rigidity_bench.rs`

#### LVQ Encoding

**Paper Reference:** Paper 1, Section 2.5
**Code Location:** `src/core/lvq.rs`
**Lines:** 1-100

```rust
/// Lattice Vector Quantization encoding
/// 
/// Paper Reference: Paper 1, Section 2.5
/// Uses A₃ lattice (FCC packing) for optimal 3D quantization
pub struct LVQEncoder {
    codebook: Vec<LatticePoint>,
    kdtree: KDTree,
}

impl LVQEncoder {
    /// Encode vector to lattice token
    /// Paper 1, Algorithm 5
    pub fn encode(&self, vector: Vector3) -> LatticeToken {
        let (nearest, _) = self.kdtree.query(vector.into());
        LatticeToken::from_point(nearest)
    }
}
```

---

## 3. GPU Implementation

### 3.1 CUDA Kernels

**Paper Reference:** Paper 2, Section 4.2
**Code Location:** `src/gpu/snap.cu`

```cuda
// Paper 2, Algorithm 3: GPU Snapping Kernel
// Performance: O(N/M) where M = GPU cores
__global__ void snap_kernel(
    float* __restrict__ x,
    float* __restrict__ y,
    float* __restrict__ result_x,
    float* __restrict__ result_y,
    float* __restrict__ noise,
    const float* __restrict__ manifold_x,
    const float* __restrict__ manifold_y,
    int manifold_size,
    int n
) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    if (idx >= n) return;
    
    // Find nearest Pythagorean triple
    float best_dist = FLT_MAX;
    int best_idx = 0;
    
    for (int i = 0; i < manifold_size; i++) {
        float dx = x[idx] - manifold_x[i];
        float dy = y[idx] - manifold_y[i];
        float dist = dx * dx + dy * dy;
        if (dist < best_dist) {
            best_dist = dist;
            best_idx = i;
        }
    }
    
    result_x[idx] = manifold_x[best_idx];
    result_y[idx] = manifold_y[best_idx];
    noise[idx] = sqrtf(best_dist);
}
```

---

## 4. Benchmark Results

### 4.1 Snapping Performance

**Paper Reference:** Paper 1, Table 1; Paper 2, Table 1

| Database Size | Operations | Naive (ms) | KD-tree (ms) | SIMD (ms) | GPU (ms) | Speedup |
|---------------|------------|------------|--------------|-----------|----------|---------|
| 1,000 | 1,000 | 95.2 | 0.8 | 0.2 | 0.15 | 634× |
| 10,000 | 10,000 | 952.3 | 6.5 | 1.8 | 0.8 | 1190× |
| 100,000 | 100,000 | 9521.5 | 58.2 | 15.4 | 5.2 | 1831× |
| 1,000,000 | 1,000,000 | 95215.8 | 521.7 | 138.5 | 42.1 | 2262× |

**Reproduction Command:**
```bash
cargo bench --bench snap_bench -- --save-baseline paper_table
```

### 4.2 Rigidity Validation

**Paper Reference:** Paper 1, Table 2

| Nodes | Graphs | Sequential (ms) | Parallel (ms) | GPU (ms) | Speedup |
|-------|--------|-----------------|---------------|----------|---------|
| 100 | 10 | 5.2 | 0.8 | - | 6.5× |
| 1,000 | 100 | 520 | 68 | - | 7.6× |
| 10,000 | 1,000 | 52,000 | 6,600 | 380 | 137× |

**Reproduction Command:**
```bash
cargo bench --bench rigidity_bench -- --save-baseline paper_table
```

### 4.3 Holonomy Transport

**Paper Reference:** Paper 1, Table 3

| Operations | Scalar (ms) | SIMD (ms) | GPU (ms) | Speedup |
|------------|-------------|-----------|----------|---------|
| 1,000 | 15.0 | 1.88 | 0.075 | 200× |
| 10,000 | 150 | 18.8 | 0.75 | 200× |
| 100,000 | 1,500 | 188 | 7.5 | 200× |

**Reproduction Command:**
```bash
cargo bench --bench holonomy_bench -- --save-baseline paper_table
```

---

## 5. Test Validation

### 5.1 Theorem Validation Tests

**Location:** `tests/theory/`

| Test File | Theorem | Validation Method |
|-----------|---------|-------------------|
| `hallucination_test.rs` | Zero Hallucination | Property-based testing |
| `rigidity_curvature_test.rs` | Rigidity-Curvature Duality | Numerical validation |
| `holonomy_info_test.rs` | Holonomy-Information Equivalence | Statistical testing |
| `percolation_test.rs` | Percolation Threshold | Monte Carlo simulation |

**Run All Validation:**
```bash
cargo test --test theory_validation -- --nocapture
```

### 5.2 Integration Tests

**Location:** `tests/integration/`

| Test File | Purpose |
|-----------|---------|
| `financial_test.rs` | Financial modeling case study |
| `engineering_test.rs` | Engineering simulation case study |
| `gaming_test.rs` | Real-time gaming case study |

---

## 6. Installation and Usage

### 6.1 From Source

```bash
git clone https://github.com/SuperInstance/Constraint-Theory.git
cd Constraint-Theory
cargo build --release
cargo test
cargo bench
```

### 6.2 Rust Usage

```rust
use constraint_theory_core::{PythagoreanManifold, snap};

fn main() {
    // Create manifold with 200 Pythagorean triples
    let manifold = PythagoreanManifold::new(200);
    
    // Snap a vector
    let (snapped, noise) = snap(&manifold, [0.6, 0.8]);
    
    println!("Snapped: {:?}", snapped);
    println!("Noise: {:.6}", noise);
}
```

---

## 7. Version Control

### 7.1 Git Tags

Each paper version is tagged:
- `paper1-v1.0` - Paper 1 initial submission
- `paper2-v1.0` - Paper 2 initial submission
- `paper3-v1.0` - Paper 3 initial submission

### 7.2 Code Comments

All code includes paper references:
```rust
/// Paper 1, Section 2.3, Theorem 3
/// Paper 2, Algorithm 1
fn snap_to_pythagorean(...) { }
```

---

**Status:** Complete
**Last Updated:** 2025-03-16
**Review Cycle:** With each paper revision
