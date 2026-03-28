# Standardized Notation Guide for Constraint Theory Papers

**Version:** 1.0
**Last Updated:** 2025-03-16
**Status:** Mandatory for all papers

---

## 1. Core Mathematical Symbols

### 1.1 Greek Letters

| Symbol | Name | LaTeX | Meaning | Context |
|--------|------|-------|---------|---------|
| Ω | Omega | `\Omega` | Origin-centric geometry | The privileged origin point |
| Φ | Phi | `\Phi` | Phi-folding operator | Manifold transformation |
| φ | phi | `\phi` | Scalar function | General scalar field |
| ρ | rho | `\rho` | Constraint density | Density function ρ(x) = 1/(1+‖x‖²) |
| κ | kappa | `\kappa` | Curvature | Discrete Ricci curvature |
| γ | gamma | `\gamma` | Path/loop | Closed loop for holonomy |
| λ | lambda | `\lambda` | Eigenvalue | Matrix eigenvalues |
| ε | epsilon | `\varepsilon` | Small quantity | Tolerance, threshold |
| δ | delta | `\delta` | Variation | Small change, Kronecker delta |
| μ | mu | `\mu` | Measure | Probability measure |
| Σ | Sigma | `\Sigma` | Summation | Summation operator |

### 1.2 Sets and Spaces

| Symbol | LaTeX | Meaning |
|--------|-------|---------|
| ℝ | `\mathbb{R}` | Real numbers |
| ℝⁿ | `\mathbb{R}^n` | n-dimensional real space |
| ℤ | `\mathbb{Z}` | Integers |
| ℕ | `\mathbb{N}` | Natural numbers |
| ℳ | `\mathcal{M}` | Manifold |
| 𝒢 | `\mathcal{G}` | Gauge field |
| 𝒯 | `\mathcal{T}` | Set of Pythagorean triples |
| ℂ | `\mathbb{C}` | Complex numbers |
| S¹ | `S^1` | Unit circle |
| SO(3) | `SO(3)` | Special orthogonal group (3D rotations) |

### 1.3 Operators

| Symbol | LaTeX | Meaning |
|--------|-------|---------|
| ‖x‖ | `\|x\|` | Norm of x |
| ‖x‖₂ | `\|x\|_2` | L2 norm |
| ‖x‖_F | `\|x\|_F` | Frobenius norm |
| ⟨a, b⟩ | `\langle a, b \rangle` | Inner product |
| ∇ | `\nabla` | Gradient/Del operator |
| ∂ | `\partial` | Partial derivative |
| ∈ | `\in` | Element of |
| ∉ | `\notin` | Not element of |
| ⊂ | `\subset` | Proper subset |
| ⊆ | `\subseteq` | Subset or equal |
| ∪ | `\cup` | Union |
| ∩ | `\cap` | Intersection |
| ∀ | `\forall` | For all |
| ∃ | `\exists` | There exists |
| ⇒ | `\Rightarrow` | Implies |
| ⇔ | `\Leftrightarrow` | If and only if |
| → | `\rightarrow` | Maps to / approaches |
| ∝ | `\propto` | Proportional to |
| ≈ | `\approx` | Approximately equal |
| ≡ | `\equiv` | Equivalent to |

---

## 2. Constraint Theory Specific Notation

### 2.1 Origin-Centric Geometry

| Notation | Description | Example Usage |
|----------|-------------|---------------|
| Ω = (0, 0, 0) | Origin point | "The origin Ω is privileged" |
| ρ(x) | Constraint density | "ρ(x) = 1/(1 + ‖x‖²)" |
| ω_density(x, y) | Density function | Equation (1) |
| ω_transform(x, y) | Transform function | Equation (2) |

### 2.2 Pythagorean Triples

| Notation | Description | Example Usage |
|----------|-------------|---------------|
| (a, b, c) | Pythagorean triple | "(3, 4, 5) is the simplest triple" |
| a² + b² = c² | Pythagorean relation | "All triples satisfy a² + b² = c²" |
| ℙ | Set of Pythagorean points | "Φ maps to ℙ" |
| m, n | Euclid's parameters | "For m > n > 0" |

### 2.3 Holonomy

| Notation | Description | Example Usage |
|----------|-------------|---------------|
| H(γ) | Holonomy matrix | "H(γ) ∈ SO(3)" |
| h_norm(γ) | Normalized holonomy | "h_norm(γ) = ‖H(γ) - I‖_F / 2√d" |
| R(θ) | Rotation matrix | "R(θ) rotates by angle θ" |
| I | Identity matrix | "h = 0 when H = I" |

### 2.4 Curvature and Rigidity

| Notation | Description | Example Usage |
|----------|-------------|---------------|
| κ_ij | Edge curvature | "κ_ij = 0 for rigid edges" |
| G = (V, E) | Graph with vertices V and edges E | "Let G be a graph" |
| \|V\| | Number of vertices | "For \|V\| = n nodes" |
| \|E\| | Number of edges | "Laman condition: \|E\| = 2\|V\| - 3" |
| p_c | Percolation threshold | "p_c = 0.6602741" |

### 2.5 Lattice Vector Quantization

| Notation | Description | Example Usage |
|----------|-------------|---------------|
| A₃ | FCC lattice | "A₃ lattice structure" |
| (i, j, k) | Lattice coordinates | "(i+j+k) mod 2 = 0" |
| v | Input vector | "Encode vector v" |
| ℓ(v) | Nearest lattice point | "ℓ(v) = argmin ‖v - L‖" |

---

## 3. Complexity Notation

### 3.1 Asymptotic Notation

| Symbol | LaTeX | Meaning | Example |
|--------|-------|---------|---------|
| O(f(n)) | `O(f(n))` | Upper bound | O(n log n) |
| Ω(f(n)) | `\Omega(f(n))` | Lower bound | Ω(n) |
| Θ(f(n)) | `\Theta(f(n))` | Tight bound | Θ(n²) |
| o(f(n)) | `o(f(n))` | Strictly smaller | o(n²) |
| ω(f(n)) | `\omega(f(n))` | Strictly larger | ω(n) |

### 3.2 Time/Space Complexity

| Notation | Meaning |
|----------|---------|
| T(n) | Time complexity as function of n |
| S(n) | Space complexity as function of n |
| T_build | Construction time |
| T_query | Query time |
| T_amortized | Amortized time |

---

## 4. Performance Notation

### 4.1 Metrics

| Metric | Unit | Format | Example |
|--------|------|--------|---------|
| Latency | ns, ms, s | `X ns` | 74 ns |
| Throughput | ops/s | `X ops/s` | 13.5M ops/s |
| Speedup | factor | `X×` | 200× |
| Memory | B, KB, MB, GB | `X MB` | 12 MB |
| Utilization | percent | `X%` | 85% |
| Error rate | percent | `X%` | 0.01% |

### 4.2 Statistical Notation

| Symbol | LaTeX | Meaning |
|--------|-------|---------|
| μ | `\mu` | Mean |
| σ | `\sigma` | Standard deviation |
| σ² | `\sigma^2` | Variance |
| p | `p` | p-value |
| R² | `R^2` | Coefficient of determination |
| CI | `CI` | Confidence interval |

---

## 5. Algorithm Notation

### 5.1 Pseudocode Keywords

```
Input:    Description of inputs
Output:   Description of outputs
for       Iteration
while     Conditional loop
if        Conditional
else      Alternative
return    Return value
function  Function definition
```

### 5.2 Variable Naming

| Convention | Example | Context |
|------------|---------|---------|
| Lowercase | `x, y, z` | Scalars, coordinates |
| Uppercase | `X, Y, Z` | Matrices, random variables |
| Bold | `\mathbf{v}` | Vectors |
| Calligraphic | `\mathcal{M}` | Sets, manifolds |
| Subscripts | `x_i, x_{ij}` | Indexed elements |
| Superscripts | `x^*, x^{(n)}` | Special values, iterations |

---

## 6. LaTeX Package Requirements

### 6.1 Required Packages

```latex
\usepackage{amsmath}    % Mathematical typesetting
\usepackage{amssymb}    % Mathematical symbols
\usepackage{amsthm}     % Theorem environments
\usepackage{mathtools}  % Extended math tools
\usepackage{bm}         % Bold math symbols
```

### 6.2 Theorem Environments

```latex
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{proposition}[theorem]{Proposition}
```

### 6.3 Custom Commands

```latex
\newcommand{\R}{\mathbb{R}}           % Real numbers
\newcommand{\Z}{\mathbb{Z}}           % Integers
\newcommand{\N}{\mathbb{N}}           % Natural numbers
\newcommand{\calM}{\mathcal{M}}       % Manifold
\newcommand{\calG}{\mathcal{G}}       % Gauge field
\newcommand{\norm}[1]{\|#1\|}         % Norm
\newcommand{\inner}[2]{\langle #1, #2 \rangle}  % Inner product
\newcommand{\bigO}{\mathcal{O}}       % Big-O notation
```

---

## 7. Cross-Paper Consistency

### 7.1 Shared Concepts

The following concepts must use identical notation across all papers:

1. **Origin-centric geometry (Ω)**: Always use Ω for the origin
2. **Phi-folding (Φ)**: Always use Φ for the folding operator
3. **Pythagorean triples (a, b, c)**: Always use (a, b, c) notation
4. **Holonomy (H)**: Always use H(γ) for holonomy matrix
5. **Curvature (κ)**: Always use κ_ij for edge curvature
6. **Laman rigidity**: Always state "|E| = 2|V| - 3"

### 7.2 Paper-Specific Extensions

Each paper may introduce additional notation, but must:
- Define new symbols at first use
- Avoid conflicting with standard notation
- Cross-reference standard definitions where applicable

---

## 8. Common Errors to Avoid

| Incorrect | Correct | Issue |
|-----------|---------|-------|
| `||x||` | `\|x\|` | Wrong LaTeX for norm |
| `O(n^2)` | `O(n²)` | Inconsistent exponent |
| `h_norm` | `h_{\text{norm}}` | Missing text formatting |
| `A3 lattice` | `A₃ lattice` | Missing subscript |
| `O(n)` | `O(N)` | Inconsistent capitalization |
| `~` | `\sim` | Wrong symbol for "similar to" |
| `*` | `\times` | Wrong multiplication symbol |
| `.` | `\cdot` | Wrong dot product symbol |

---

**Status:** Approved
**Applies to:** All papers, documentation, and supplementary materials
**Review cycle:** With each paper submission
