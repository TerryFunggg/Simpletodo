SCRIPT = todo.py
EXECUTABLE = todo

all: build

build:
	@echo "Creating standalone executable with PyInstaller..."
	pyinstaller --onefile $(SCRIPT)

clean:
	@echo "Cleaning up build files..."
	rm -rf build dist $(EXECUTABLE).spec

.PHONY: all build clean install uninstall

