# Creating-A-Portscanner

## Description
In this project, I wanted to create a portscanner. It was important to me that the portscanner accepted user input as well as a timeout for port scanning incase one port was taking too long. I did all this in Python. 

# Walkthrough
First thing I did was import the socket library as well as the re library to ensure that our inputs are properly formatted. <br>
![import_lib](https://imgur.com/FgxxQiC.png)
<br>
Next I assigned variables, as you can see instead of assigning the ip and port variables myself I used a `True` loop and the `input()` function to allow the user to put in whatever they wanted. It then used the `ip_add_pattern` variable i defined earlier for input validation to ensure that it was a valid IP address. If the input is not recognized, then it lets the user know and asks for another input. <br>
![inputs](https://imgur.com/QOciwfc.png)
<br>
Next, I defined the port scanning function. I used the `.connect_ex()` as it inputs true or false depending on if it connects or not. If it is true, that means the port is open, and if it is false, that means the port is closed. <br>
![defined](https://imgur.com/XJh4R6c.png)
<br>
Then, I called the function.<br>
![call](https://imgur.com/slEa6jr.png) <br>
Lastly, I tested it out. Using the IP address from hackthissite.org (137.74.187.100), I used my function to test if port 80 was open to allow for HTTP packets were allowed through. You can see me on purposly putting in an invalid IP address at first to check if the input validation worked before trying the proper IP address. As you can see it worked and port is open.<br>
![outputs](https://imgur.com/gCl6JdR.png) <br>
