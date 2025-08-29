# Makefile

.PHONY: build run test clean

build:
	go build -o app ./cmd/app

run: build
	./app

test:
	go test ./...

clean:
	go clean
	rm -f app