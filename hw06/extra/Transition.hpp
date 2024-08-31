#ifndef TRANSITION_HPP
#define TRANSITION_HPP

#include <iostream>

class Transition
{
private:
  int from;
  int to;
  char readc;

public:
  Transition() {}
  Transition(int f, int t, char r) : from(f), to(t), readc(r) {
    //std::cout << "New transition: " << from << " -> " << to << " (" << readc << ")" << std::endl;
  }
  ~Transition() {} // not really necessary

  // create a transition:
  /**
   * format (xml):
   * <transition>
   *  <from>#</from>
   *  <to>#</to>
   *  <read>@</read>
   * </transition>
   */ 
  static Transition* read(std::istream& is)
  {
    // yeah I have already built a java-like Scanner that 
    // would make this easier... oh well
    int f, t;
    char r;
    
    std::string line;

    do
    {
      std::getline(is, line);

      if(line == "<transition>") continue;
      else if(line.find("<from>") != std::string::npos)
      {
        f = stoi(line.substr(6, line.find("/")-1-6));
      }
      else if(line.find("<to>") != std::string::npos)
      {
        t = stoi(line.substr(4, line.find("/")-1-4));
      }
      else if(line.find("<read>") != std::string::npos)
      {
        r = line[6];
      }    
    } while(line != "</transition>");   

    return new Transition(f, t, r);
  }

  bool isValid(char c)
  {
    return c == readc;
  }

  int getID() { return from; }

  int transition() 
  {
    return to;
  }

};

#endif//TRANSITION_HPP
