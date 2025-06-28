CXX = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -pedantic

TARGET = derivative_test
SRCS = test.cpp

all: $(TARGET)

$(TARGET): $(SRCS)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(SRCS)

clean:
	rm -f $(TARGET)

run: $(TARGET)
	./$(TARGET)
