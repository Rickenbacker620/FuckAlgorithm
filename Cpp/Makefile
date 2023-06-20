CXX = g++
CXXFLAGS = -std=c++20 -g -Wall -DDEBUG
BUILD_DIR = build

.PHONY: all clean run hook

all: run

$(BUILD_DIR)/solve: $(BUILD_DIR)/solve.o input
	@$(CXX) $(CXXFLAGS) $< -o $@

$(BUILD_DIR)/solve.o: solve.cpp
	@mkdir -p $(BUILD_DIR)
	@$(CXX) $(CXXFLAGS) -c $< -o $@

run: $(BUILD_DIR)/solve
	@$(BUILD_DIR)/solve

clean:
	@rm -rf $(BUILD_DIR)
