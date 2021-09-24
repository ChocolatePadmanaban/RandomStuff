# Debugging

Debugging is trying to find
why your code doesn’t behave the way you want it to. Maybe it’s generating some
errors. Maybe it’s not generating errors, but the output isn’t what you want it to be.
Either way, there’s a bug in the code: a bug is a mistake or problem that is causing
the code to fail at its goal. Debugging is the process of finding and removing those
bugs.

### Types of Error

- **Compilation Errors**
compilation errors are those that occur when compiling our code in the first
place. Not every language has compilation, and so, not every language has com-
pilation errors. Those languages that don’t require compilation, like Python and
JavaScript, can sometimes have tools that simulate this process, letting us know
before we execute our code if there are errors present within it.

Errors can differ significantly from language to language, but there are some
common ones. For compilation errors, some things you might often encounter are:
• _Syntax errors_. You’ve written code that just doesn’t make sense in the current
programming language. This is akin to a grammatical error in an essay.
• _Name errors_. You’ve written code that tries to use something that doesn’t exist.
Imagine, for example, I asked you, “Give her the book,” but never specified who
“her” is. The command doesn’t make sense because I’m including a person that
doesn’t exist.
• _Type errors_. You’ve written code that tries to do something that doesn’t make
sense, like requesting the smell of True or the color of the number 5.

- **Runtime Errors**
Runtime errors are errors that we encounter only when actually running the code.
Languages that don’t have compilation will only have runtime errors, and even
languages that do require compilation can have runtime errors because we can’t
anticipate every error just by looking at the code.

Runtime errors most often occur because of something specific to the results
that code generates when it runs. Some of the common runtime errors you will
encounter are:
• _Divide by zero errors_. Your code contains a number being divided by another,
but when those numbers actually have values, it turns out you’re trying to divide
by zero!
• _Null errors_. Null errors are like name errors: you’re referring to something that
doesn’t exist. Here, though, the variable would exist, but it wouldn’t have any
value. Imagine your code said, “Grab the twelfth book on the shelf,” but the
shelf only has six books. The request makes sense in the directions until you
see the shelf: then you realize you’re trying to use something that doesn’t exist,
but you only “see” that at runtime.
• _Memory errors_. Your computer can only remember a certain amount of stuff at
a time. If you try to require it to remember more than that, you’ll hit a memory
error.
