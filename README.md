# HMM-Viterbi
Implementation of HMM Viterbi algorithm in Python

This algorithm can run for any number of states and observations. The default example has two states (H&C) and three possible observations (emissions) namely 1, 2 and 3. Following are the matrices/variables that needs to be adjusted:

Transition: contains transition probabilies. The value at [0,0] is transition from H to H and value at [1,1] is transition from C to C. (keeping in view the default example)
emission: contains emission probabilies. The value at [0,0] is emission of symbol 1 from H and the value at [0,1] is emission of symbol 2 from H. (keeping in view the default example)
states_dic: the dictionary that contains corresponding digits/indices for each state. The value starts from 0 and goes upto number of states for each state
sequence_syms: simply a dictionary of all possible observations with their corresponding indice. Indice start from 0 and increments with each observation
test_sequence: a string containing the sequence on which we want to train our matrices
