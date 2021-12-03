# Control Flow: Conditional Statements

## Learning Goals

- Conditionally execute code with `if/else` statements

## Introduction

In the last lesson, we saw how to use comparison methods and logical operators
in Python. In this lesson, we'll see more examples of how to use those tools to
perform control flow using **conditional statements** with the `if/else`
keywords.

Make sure to code along with the Python examples to help get a feel for the
syntax.

## `if/else` Statements

Python has slightly different syntax for writing conditional statements using
`if/else` than JavaScript. Here's a relatively complex `if/else` statement in
JavaScript:

```js
// JavaScript
let dog = "cuddly";
let owner;

if (dog === "hungry") {
  owner = "Refilling food bowl.";
} else if (dog === "thirsty") {
  owner = "Refilling water bowl.";
} else if (dog === "playful") {
  owner = "Playing tug-of-war.";
} else if (dog === "cuddly") {
  owner = "Snuggling.";
} else {
  owner = "Reading newspaper.";
}
```

Here's how we can write the equivalent statement in Python:

```py
# Python
dog = "cuddly"

if dog == "hungry":
  owner = "Refilling food bowl."
elif dog == "thirsty":
  owner = "Refilling water bowl."
elif dog == "playful":
  owner = "Playing tug-of-war."
elif dog == "cuddly":
  owner = "Snuggling."
else:
  owner = "Reading newspaper."
```

## Truthy/Falsy Values

In order to use control flow effectively, it's important to know what values
Ruby treats as "truthy" and "falsy".

As we saw in the lesson on data types, there are many values Python considers
falsy, such as empty lists and dictionaries; empty strings; 0; `None`, and
`False`. Using those values in control flow means the condition will be false:

```rb
def control_flow(value):
  if value:
    # if the value is truthy
    print("yep!")
  else:
    # if the value is falsy
    print("nope!")

control_flow(False)
# => "nope!"
control_flow(None)
# => "nope!"
control_flow(True)
# => "yep!"
control_flow('')
# => "nope!"
control_flow(0)
# => "nope!"
control_flow([])
# => "nope!"
```

## Instructions

Time to get some practice! Write your code in the `control_flow.rb` file. Run
`learn test` to check your work. Your goal is to practice using control flow in
Python to familiarize yourself with the syntax. There is a JavaScript version of
the solution for each of these deliverables in the `js/index.js` file you can
look at (but if you want an extra challenge, try solving them in Python without
looking at the JavaScript solution).

Write a method `admin_login` that takes two arguments, a username and a
password. If the username is "admin" or "ADMIN" and the password is "12345",
return "Access granted". Otherwise, return "Access denied".

```py
admin_login('sudo', '12345')
# => "Access denied"
admin_login('admin', '12345')
# => "Access granted"
admin_login('ADMIN', '12345')
# => "Access granted"
```

Write a method `hows_the_weather` that takes in one argument, a temperature. If
the temperature is below 40, return "It's brisk out there!". If the temperature
is between 40 and 65, return "It's a little chilly out there!". If the
temperature is above 85, return "It's too dang hot out there!". Otherwise,
return "It's perfect out there!"

```py
hows_the_weather(33)
# => "Brisk!"
hows_the_weather(99)
# => "Too dang hot"
hows_the_weather(75)
# => "Perfect!"
```

Write a method `fizzbuzz` takes in a number. For multiples of three, return
"Fizz" instead of the number. For the multiples of five, return "Buzz". For
numbers which are multiples of both three and five, return "FizzBuzz". For all
other numbers, just return the number itself.

```py
fizzbuzz(1)
# 1
fizzbuzz(2)
# 2
fizzbuzz(3)
# Fizz
fizzbuzz(4)
# 4
fizzbuzz(5)
# Buzz
fizzbuzz(15)
```

## Conclusion

Since you're already familiar with these control flow structures from
JavaScript, you should have a good intuition of when it's appropriate to use
these different tools. Try and develop familiarity with the differences in
syntax between JavaScript and Python first, so that you'll be able to take
advantage of some of Python's unique features like statement modifiers and the
`unless` keyword in your own code.

One excellent resource for familiarizing yourself with the syntax and the
preferred conventions of some Pythonistas is the [Python style
guide][python style guide]. Make sure to bookmark this resource and refer to it
if you're ever unsure how to format a particular block of code.

## Resources

- [PEP 8 - Python style guide][python style guide]

[python style guide]: https://www.python.org/dev/peps/pep-0008/
