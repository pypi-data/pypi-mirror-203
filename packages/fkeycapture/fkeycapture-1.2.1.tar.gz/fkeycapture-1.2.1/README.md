# fkeycapture
This is a simple and easy to use package that allows you to capture individual keystrokes from the user.
#### Forms:
1. (Default) Recive key as a string
2. Recive key as bytes (get only)
3. Recive key as ints  (getnum only)
#### How to Use:
1. from fkeycapture import get, getnum, getchars
2. Use get like this: get([number of keys to capture],[if you want bytes output, make this 'True'])
3. Use getnum like this: getnum([number of numbers to capture], [if you want int output, make this `True`])
###### v.1.2.1:
Type hinting, docstrings, and int support for getnum!

~~Now includes a help command! Use fkeycapture.help() to recive help.~~ Help discontinued.
