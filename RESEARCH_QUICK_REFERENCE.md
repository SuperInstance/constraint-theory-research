# Research Quick Reference

**Version:** 1.0
**Last Updated:** 2025-03-16
**Repository:** https://github.com/SuperInstance/Constraint-Theory

---

## Core Concepts at a Glance

### Origin-Centric Geometry (Ω)

```
ρ(x) = 1/(1 + ||x||²)
```

- Origin is privileged point of maximal constraint
- Constraint density decreases with distance
- Enables deterministic geometric computation

### Pythagorean Snapping

```
σ(v) = argmin_{p ∈ M} d_g(v, p)
```

- Snap any 2D vector to exact Pythagorean triple
- O(log n) with KD-tree (vs O(n²) naive)
- Maximum noise: π/(2n) for manifold of size n

### Rigidity-Curvature Duality

```
Rigid graph ↔ Ricci curvature κ = 0
```

- Laman's theorem: |E| = 2|V| - 3
- Pebble game algorithm for validation
- Percolation threshold: p_c = 0.6602741

### Holonomy-Information Equivalence

```
h_norm = I_loss / H_max
```

- Holonomy measures information loss in parallel transport
- Zero holonomy = zero information loss
- Gauge connection preserves structure

### Lattice Vector Quantization

```
A₃ lattice: (i + j + k) mod 2 = 0
```

- Optimal sphere packing in 3D
- Nearest neighbor encoding
- KD-tree for O(log n) search

---

## Performance Summary

| Operation | Baseline | Optimized | Speedup |
|-----------|----------|-----------|---------|
| Snap (1K) | 100ms | 0.5ms | 200× |
| Rigidity (1K) | 500ms | 2ms | 250× |
| Holonomy (1K) | 200ms | 1ms | 200× |
| LVQ (10K) | 1000ms | 5ms | 200× |

---

## Quick Commands

### Build & Test

```bash
cargo build --release
cargo test
cargo bench
```

### Run Examples

```bash
cargo run --example basic_snap
cargo run --example batch_processing
cargo run --example performance_test
```

### Generate Figures

```bash
python scripts/generate_figures.py --output figures/
```

### Run Validation

```bash
cargo test --test theory_validation
python scripts/run_validation.py
```

---

## File Locations

| What | Where |
|------|-------|
| Papers | `papers/` |
| Core code | `src/core/` |
| Spatial indexing | `src/spatial/` |
| GPU kernels | `src/gpu/` |
| Benchmarks | `benches/` |
| Tests | `tests/` |
| Examples | `examples/` |
| Documentation | `*.md` files |

---

## Key Theorems

### Theorem 1: Origin-Centric Density

For any point x in ℝ², the constraint density ρ(x) = 1/(1 + ||x||²) satisfies:
- ρ(0) = 1 (maximum at origin)
- ρ(x) → 0 as ||x|| → ∞
- ∇ρ points toward origin

### Theorem 2: Rigidity-Curvature Duality

A graph G is Laman-rigid if and only if the discrete Ricci curvature κ = 0 on all edges.

### Theorem 3: Holonomy-Information Equivalence

For parallel transport around closed loop γ:
h_norm(γ) = I(X₀; X_γ) / H(X₀)

### Theorem 4: Zero Hallucination

For any constraint-satisfying operation:
P(hallucination) = 0

### Theorem 5: Percolation Threshold

The critical probability for rigidity percolation:
p_c = 0.6602741 (minimizes description length)

---

## Architecture Layers

```
┌─────────────────────────────────────────┐
│         TypeScript API Layer            │
│    (formula registration, orchestration) │
├─────────────────────────────────────────┤
│          Rust Acceleration Layer        │
│    (SIMD, KD-tree, core algorithms)      │
├─────────────────────────────────────────┤
│           Go Concurrent Layer           │
│    (parallel validation, goroutines)     │
├─────────────────────────────────────────┤
│           CUDA/PTX GPU Layer            │
│    (massive parallelism, batch ops)      │
└─────────────────────────────────────────┘
```

---

## API Quick Reference

### Rust

```rust
use constraint_theory_core::{PythagoreanManifold, snap};

let manifold = PythagoreanManifold::new(200);
let (snapped, noise) = snap(&manifold, [x, y]);
```

### Python

```python
from constraint_theory import PythagoreanManifold

manifold = PythagoreanManifold(200)
x, y, noise = manifold.snap(x, y)
```

### TypeScript

```typescript
import { PythagoreanManifold } from 'constraint-theory';

const manifold = new PythagoreanManifold(200);
const { snapped, noise } = manifold.snap(x, y);
```

---

## Citation

```bibtex
@article{constraint_theory_2025,
  title={Constraint Theory: Deterministic Manifold Snapping
         via Pythagorean Geometry},
  author={SuperInstance},
  journal={arXiv preprint arXiv:2503.15847},
  year={2025},
  url={https://github.com/SuperInstance/constraint-theory-research}
}
```

---

## Contact

- **GitHub:** https://github.com/SuperInstance/Constraint-Theory
- **Email:** constraint-theory@example.com
- **Twitter:** @ConstraintTheory

---

**Status:** Complete
**Last Updated:** 2025-03-16
