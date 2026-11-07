Object subclass: #Counter instanceVariableNames: 'count'
Counter count_val [ count ]
Counter increment [ count := count + 1 ]

c := Counter new.
c increment.
Transcript show: c count_val.
