# UDP-Traffic-Generator

Autonomous activity developed for the discipline of Computer Networks (Federal University of Rio Grande do Sul), professor Valter Roesler.

## Resume

Program to generate network traffic for testing (similar to IPERF, but simplified). The program sends a number of bits / s in the network in UDP (avoiding bursts).

### Prerequisites

* Linux
* Python 3

### How to execute

* python3 gt.py -i "ipdest" -p "port" -r "rate"