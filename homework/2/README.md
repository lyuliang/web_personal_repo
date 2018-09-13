The reason why I use GET method in this application is that although POST is more secure, we don't really need that much security in this calculator application. GET request let users see the values of every variable in the request so that users can have a more clear vision on the working process of the calculator.

Here is some illustration on how this calculator deal with any error situations or ambiguous user behaviors.

Error situations:

When some number is divided by zero, the calculator will display "Error".

When user input some arbitrary text in the display box that is not a valid number, it will display "Error".

When the user modified some fields in the url and made it invalid, the calculator will display "Error".

When user deleted some fields in the url, the calculator will display "Error".

When the calculator displays "Error", if you press any symbol buttons, it will still display "Error". If you press any digit buttons, it will start over.



Ambiguous behaviors:

When press symbol buttons(i.e. '+', '−', '×', '÷') continuously, the calculator will use the last one.

When press '=' button continuously, the display content will remain the same.

When press '=' after other symbol button, the displayed number will remain the same, and the calculation will start over from that number.

When user input some number directly into the display box, it will start over from this number, ignoring the previous operands. 

By refreshing the web page, the calculator will not return to the initial state, but will keep the current status and inputs.

There is actually a hidden button on the bottom-left, which can reset the calculator to initial state, but since the writeup requires 15 buttons, I made it invisible.
