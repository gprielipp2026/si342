M0 = (
        {'q1','q2','q3'}, # Q aka set of states
        {'a','b','c'},    # E aka Sigma
        {('q1','a','q2'),('q1','b','q1'),('q2','a','q1'), # D aka Delta 
         ('q2','b','q2'),('q2','c','q3')},     
        'q1',             # s aka start state
        {'q3'}            # W aka set of accepting states

        )
