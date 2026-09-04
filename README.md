Python TCP Port Scanner

A simple Python-based TCP port scanner that checks a range of ports on a specified host.

Features
Scans a user-defined range of TCP ports.
Uses Python's built-in socket library.
Displays the host being scanned.
Attempts to identify services running on open ports.
Requirements
Python 3.x
No external Python packages are required.
Installation

Clone the repository:

git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY


Make the script executable if necessary:

chmod +x 1.py

Usage

Run the scanner with:

python3 1.py <IP>


Example:

python3 1.py 192.168.1.1


The program can then be used to specify the port range to scan.

How It Works

The program uses Python's socket module to create a TCP connection to each port in the selected range.

Conceptually, the scanner:

Takes a target IP address or hostname.
Gets the starting and ending port numbers.
Loops through the selected port range.
Attempts to establish a TCP connection.
Reports ports where a connection succeeds.
Attempts to determine the service associated with an open port.
Example Output
[* Host-name ] : 192.168.1.1

22 ssh
80 http
443 https

Important Notes

The current version of the script is a learning project and still needs some corrections before it will run as intended.

For example:

sys.argv[2] is accessed even though the script checks for only one command-line argument.
input should be called as input().
Port values need to be converted to integers before being passed to socket.connect().
A new socket should generally be created for each connection attempt.
socket.getservbyport() should be given an integer port number.
Exception handling should preferably catch specific socket exceptions instead of using a bare except.
Legal and Ethical Use

Use this tool only on systems you own or have explicit permission to test.

Port scanning systems without authorization may violate organizational policies or applicable laws.

License

This project is provided for educational purposes. Add a license to this repository if you intend to distribute or modify the project publicly.
