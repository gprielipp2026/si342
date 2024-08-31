#ifndef STATE_HPP
#define STATE_HPP

#include <vector>
#include <iostream>
#include "Transition.hpp"
#include <string>

#define INITIAL 1
#define FINAL 2

bool is(int flag, uint8_t& var)
{
  return var & flag;
}

void set(int flag, uint8_t& var)
{
  var = var | flag;
}

void unset(int flag, uint8_t& var)
{
  var = var & (!flag);
}

class State
{
private:
  int id;
  std::string name;
  uint8_t type;
  // pos not needed
  std::vector<Transition*> transitions;

public:
  State() {}
  ~State() 
  {
    for(Transition* t : transitions)
      delete t;
  }
  State(int i, std::string n, uint8_t t) : id(i), name(n), type(t) {
    //std::cout << "new state: " << id << " " << name << " " << type << std::endl;
  }

  static State* read(std::istream& is)
  {
    int id;
    std::string name;
    uint8_t type = 0;

    std::string line;

    do
    {
      std::getline(is, line);

      if(line.find("<state") != std::string::npos)
      {
        // yes I know this is bad
        // it extracts value from: id="value", no matter the length of the int value
        //std::cout << "getting id" << std::endl;
        //std::cout << "id str: " << line.substr( line.find("id=\"")+4, line.find("\"", line.find("id=\"")+5) - line.find("id=\"") - 4 ) << std::endl;
        id = stoi(line.substr( line.find("id=\"")+4, line.find("\"", line.find("id=\"")+5) - line.find("id=\"") - 4 )  );
        //std::cout << "getting name" << std::endl;
        name = line.substr(line.find("name=\""), line.find(">")-line.find("name=\"")-2);
        //std::cout << "State: " << id << " " << name << std::endl;
      }
      else if(line == "<initial/>")
      {
        set(INITIAL, type);
      }
      else if(line == "<final/>")
      {
        set(FINAL, type);
      }
    } while(line != "</state>");   

    return new State(id, name, type); 
  }

  void addTransition(Transition* t)
  {
    transitions.push_back(t);
  }

  int nextState(char c)
  {
    for(Transition* t : transitions)
    {
      if(t->isValid(c))
      {
        return t->transition();
      }
    }
    throw "error: symbol not in alphabet";
  }

  int getID() { return id; }

  bool isFinal() { return is(FINAL, type); }
  bool isInitial() { return is(INITIAL, type); }
};

#endif//STATE_HPP
