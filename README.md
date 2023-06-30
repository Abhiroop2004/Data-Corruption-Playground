# Data-Corruption-Playground
<h3>A Mini-Project that simulates data corruption techniques and the use of hashing for detection.</h3>

**This is a simple Python program that allows the simulation of various data corruption techniques and checks file integrity using the SHA-256 hash algorithm.**

**Features:**
<ul>
<li>Flip random bits of a file,
<li>Modify specific bytes of a file
<li>Introduce noise into a file
<li>Swap contents of two files
</ul>

**Usage**
<ol>
  <li>Run the 'File Authentication.py' program and choose a desired option from the menu.</li>
  <li>Follow the prompts to provide the necessary inputs, such as file name, positions to modify, or noise intensity.</li>
  <li>The program will perform the selected data corruption technique on the file and calculate the SHA-256 hash before and after the modification.</li>
  <li>It will then compare the hashes to determine if the file integrity is maintained or compromised.</li>
  <li>For the "Swap contents of a file" option, it demonstrates that SHA-256 does not detect file swapping.</li>
  <li>You may repeat the process for different files or corruption techniques as needed.</li>
  <li>Choose the "Exit the system" option when you are finished.</li>
</ol>

**Requirements**
<ul>
  <li>Python version 3</li>
  <li>'hashlib' module</li>
</ul>

**Note**<br>
This program is for educational purposes only and serves as a playground to explore data corruption techniques and understand the concept of file integrity. It is not intended for real-world file manipulation or security applications.
Sample files have been added for the same purpose.

**Disclaimer**<br>
I am not liable for any loss or damage resulting from the use of this code. Use it at your own risk.
