#ifndef AUTOMATON_HPP
#define AUTOMATON_HPP

#include <string>
#include <iostream>
#include <vector>
#include "Transition.hpp"
#include "State.hpp"


class Automaton
{
  private:
    std::vector<State*> states;
    State* initial;

    State* getState(int id)
    {
      for(State* state : states)
      {
        if(state->getID() == id)
          return state;
      }
      return nullptr;
    }

  public:
    // assumes all states are in machine already    
    void addTransition(Transition* t)
    {
      for(State* state : states)
      {
        if(state->getID() == t->getID())
        {
          state->addTransition(t);
          break;
        }
      }  
    }

    // assume only one initial state
    void addState(State* state)
    {
      states.push_back(state);
      if(state->isInitial())
        initial = state;
    }

    bool run(std::string input)
    {
      State* cur = initial;

      for(char c : input)
      {
        //std::cout << "state (" << cur->getID() << ")\t" << c << std::endl;
        cur = getState(cur->nextState(c));
      }

      return cur->isFinal();
    }
};


#endif//AUTOMATON_HPP
