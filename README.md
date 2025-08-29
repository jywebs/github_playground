# GitHub Features Learning

This project is designed to help you learn and explore various features of GitHub through practical examples in both Python and Go.

## Project Structure

```
github-features-learning
├── python
│   ├── src
│   ├── tests
│   ├── pyproject.toml
│   ├── requirements.txt
│   └── README.md
├── go
│   ├── cmd
│   ├── pkg
│   ├── internal
│   ├── go.mod
│   ├── Makefile
│   └── README.md
└── .github
    └── workflows
```

## Getting Started

### Python

1. Navigate to the `python` directory.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   python src/main.py
   ```
4. Run tests:
   ```
   python -m unittest discover -s tests
   ```

### Go

1. Navigate to the `go` directory.
2. Build the application:
   ```
   go build ./cmd/app
   ```
3. Run the application:
   ```
   ./app
   ```
4. Run tests:
   ```
   go test ./...
   ```

## Contributing

Contributions are welcome! Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for details on how to contribute to this project.