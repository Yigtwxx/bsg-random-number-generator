# Makefile for bsg-random-number-generator
# Management commands for the Collatz Conjecture-based random number generator.

.PHONY: help run test clean lint

# Default target: Shows the help menu
help:
	@echo "Please select a command:"
	@echo "  make run    - Runs the visual demo (demo.py)"
	@echo "  make test   - Runs the basic tests in collatz_rng.py"
	@echo "  make clean  - Cleans temporary files and cache (__pycache__)"
	@echo "  make lint   - Performs code style checks (requires flake8)"

# Run the visual demo
run:
	python demo.py

# Run module-based self-test
test:
	python collatz_rng.py

# Clean cache and temporary files
clean:
	@echo "Cleaning up..."
	if exist "__pycache__" rmdir /s /q "__pycache__"
	@echo "Cleanup complete."

# Code style check (if flake8 is installed)
lint:
	@flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	@flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
