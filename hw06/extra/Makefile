CXX=g++
CXXFLAGS= -Wall -g

#HPP=$(wildcard *.hpp)
#OBJS=$(HPP:%.hpp=%.o)
OBJS=

all: $(OBJS)
	$(CXX) $(CXXFLAGS) EC.cpp $^ -o extra


%.o: %.hpp
	$(CXX) $(CXXFLAGS) -c $^ -o $@

clean:
	$(RM) $(RF) $(OBJS) extra
