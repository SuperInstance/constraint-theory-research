# Contributing to Constraint Theory Research

Thank you for your interest in contributing to Constraint Theory Research! This document provides guidelines and instructions for contributing.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)
- [Style Guidelines](#style-guidelines)
- [Mathematical Contributions](#mathematical-contributions)

## Code of Conduct

This project and everyone participating in it is governed by our commitment to maintaining a welcoming and inclusive environment. By participating, you are expected to uphold this standard.

## How Can I Contribute?

### Reporting Bugs

- Use the GitHub issue tracker to report bugs
- Include a clear title and description
- Provide steps to reproduce the issue
- Include relevant logs or screenshots

### Suggesting Enhancements

- Open an issue with the label "enhancement"
- Clearly describe the enhancement and its motivation
- Explain how it would benefit the project

### Contributing Code

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

### Contributing Documentation

Documentation improvements are always welcome:
- Fix typos or clarify existing documentation
- Add new examples or tutorials
- Improve mathematical explanations

## Development Setup

### Prerequisites

- Rust 1.70+ (for constraint-theory-core)
- Python 3.8+ (for constraint-theory-python)
- Git

### Getting Started

```bash
# Clone the repository
git clone https://github.com/SuperInstance/constraint-theory-research.git
cd constraint-theory-research

# For Rust development
cd ../constraint-theory-core
cargo build
cargo test

# For Python development
cd ../constraint-theory-python
pip install -e .
pytest
```

## Pull Request Process

1. **Update Documentation**: Ensure any new functionality is documented
2. **Add Tests**: All new features should include appropriate tests
3. **Follow Style Guidelines**: See below for style requirements
4. **Link Issues**: Reference any related issues in your PR description
5. **Wait for Review**: Maintainers will review your PR promptly

### PR Checklist

- [ ] Code compiles without errors
- [ ] All tests pass
- [ ] New features have corresponding tests
- [ ] Documentation is updated
- [ ] Commit messages are clear and descriptive

## Style Guidelines

### Code Style

**Rust:**
- Follow standard Rust formatting (`cargo fmt`)
- Use `clippy` for linting (`cargo clippy`)
- Document public APIs with doc comments

**Python:**
- Follow PEP 8 style guidelines
- Use type hints for function signatures
- Document functions with docstrings

### Mathematical Notation

When contributing mathematical content:
- Use standard LaTeX notation in Markdown files
- Provide both formal definitions and intuitive explanations
- Include examples where appropriate
- Reference relevant literature

### Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters
- Reference issues and pull requests liberally

## Mathematical Contributions

### Proofs and Theorems

When contributing formal proofs:
1. State the theorem clearly
2. Provide a complete proof
3. Reference any lemmas used
4. Include a brief explanation of significance

### New Algorithms

For new algorithms:
1. Describe the algorithm mathematically
2. Provide pseudocode
3. Analyze time and space complexity
4. Include benchmark comparisons if applicable

### Literature References

When adding citations:
- Use BibTeX format for bibliographic entries
- Ensure DOIs are included where available
- Follow arXiv citation standards for preprints

## Questions?

Feel free to open an issue with the "question" label, or reach out to the maintainers directly.

Thank you for contributing to Constraint Theory Research!
