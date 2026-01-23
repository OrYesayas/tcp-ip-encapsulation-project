# TCP/IP Encapsulation Project

This project implements a TCP-based client–server chat application using Python sockets and demonstrates how application-layer messages are encapsulated into TCP/IP packets.

The application transmits messages over a TCP connection on the loopback interface (127.0.0.1). Application-layer messages are defined in a CSV file and sent by the client to the server. The resulting network traffic is captured and analyzed using Wireshark.

The analysis illustrates the TCP three-way handshake, acknowledgment packets, and data packets carrying application payloads (PSH + ACK). It demonstrates how a single application-layer message may result in multiple TCP packets at the transport and network layers.

---

## Project Contents

- Python implementation of a TCP client and server  
- CSV file representing application-layer messages  
- Jupyter Notebook demonstrating TCP/IP encapsulation across layers  
- Wireshark packet capture file (.pcapng) for traffic analysis  
- Execution instructions for running the application  

---

## How to Run

Detailed execution steps, including environment setup, server and client execution, and Wireshark capture instructions, are provided in the `RUN_INSTRUCTIONS.txt` file.
