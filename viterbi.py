import numpy as np

#generating initial probabilities

#transition probabilities
transition = np.array([[0.8,0.1],
                       [0.1,0.8]])
#Emission probabilities
emission = np.array([[0.1,0.2,0.7],
                     [0.7,0.2,0.1]])

#defining states and sequence symbols
states = ['H','C']
states_dic = {'H':0, 'C':1}
sequence_syms = {'1':0,'2':1,'3':2}


#test sequence
test_sequence = '111133333'
test_sequence = [x for x in test_sequence]

#node values stored during viterbi forward algorithm
node_values = np.zeros((len(states),len(test_sequence)))

#probabilities of going to end state
end_probs = [0.1, 0.1]
#probabilities of going from start state
start_probs = [0.5, 0.5]

#storing max symbol for each stage
max_syms = np.chararray((len(states),len(test_sequence)))

for i, sequence_val in enumerate(test_sequence):
    for j in range(len(states)):
        #if first sequence value then do this
        if(i == 0):
            node_values[j,i] = start_probs[j]*emission[j,sequence_syms[sequence_val]]
        #else perform this
        else:
            values = [node_values[k, i - 1] * emission[j, sequence_syms[sequence_val]] * transition[k, j] for k in
                      range(len(states))]

            max_idx = np.argmax(values)
            max_val = max(values)
            max_syms[j,i] = states[max_idx]
            node_values[j,i] = max_val

#end state value
end_state = np.multiply(node_values[:,-1],end_probs)
end_state_val = max(end_state)
end_state_max_idx = np.argmax(end_state)
end_state_sym = states[end_state_max_idx]

#Obtaining the maximum likely states
max_likely_states = [end_state_sym]

prev_max = end_state_sym
for count in range(1,len(test_sequence)):
    current_state = max_syms[:,-count][states_dic[prev_max]].decode('utf-8')
    max_likely_states.append(current_state)
    prev_max = current_state

max_likely_states = max_likely_states[::-1]
[print(x) for x in max_likely_states]

c = 1