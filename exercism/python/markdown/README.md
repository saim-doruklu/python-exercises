# Markdown

Refactor a Markdown parser.

The markdown exercise is a refactoring exercise. There is code that parses a
given string with [Markdown
syntax](https://guides.github.com/features/mastering-markdown/) and returns the
associated HTML for that string. Even though this code is confusingly written
and hard to follow, somehow it works and all the tests are passing! Your
challenge is to re-write this code to make it easier to read and maintain
while still making sure that all the tests keep passing.

It would be helpful if you made notes of what you did in your refactoring in
comments so reviewers can see that, but it isn't strictly necessary. The most
important thing is to make the code better!


## Exception messages

Sometimes it is necessary to raise an exception. When you do this, you should include a meaningful error message to
indicate what the source of the error is. This makes your code more readable and helps significantly with debugging. Not
every exercise will require you to raise an exception, but for those that do, the tests will only pass if you include
a message.

To raise a message with an exception, just write it as an argument to the exception type. For example, instead of
`raise Exception`, you should write:

```python
raise Exception("Meaningful message indicating the source of the error")
```

## Running the tests

To run the tests, run `pytest markdown_test.py`

Alternatively, you can tell Python to run the pytest module:
`python -m pytest markdown_test.py`

### Common `pytest` options

- `-v` : enable verbose output
- `-x` : stop running tests on first failure
- `--ff` : run failures from previous test before running other test cases

For other options, see `python -m pytest -h`

## Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the `$EXERCISM_WORKSPACE/python/markdown` directory.

You can find your Exercism workspace by running `exercism debug` and looking for the line that starts with `Workspace`.

For more detailed information about running tests, code style and linting,
please see [Running the Tests](http://exercism.io/tracks/python/tests).

## Submitting Incomplete Solutions

It's possible to submit an incomplete solution so you can see how others have completed the exercise.



- `__x __y y__ x__` &nbsp;2 2 2 2  &nbsp;&nbsp;&nbsp;&nbsp;__x __y y__ x__ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2 2 2 2        
- `__x __y y__ x_` &nbsp;&nbsp;2 2 2 1 &nbsp;&nbsp; __x __y y__ x_ &nbsp;&nbsp;&nbsp;  2 2 2 1      
- `__x __y y_ x_` &nbsp;&nbsp;&nbsp;2 2 1 1&nbsp;&nbsp;&nbsp;&nbsp; __x __y y_ x_  &nbsp;  2 2 1 1    
- `__x __y y_ x__` &nbsp;&nbsp;2 2 1 2 &nbsp;&nbsp;&nbsp;&nbsp;__x __y y_ x__ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  2 2 1 2       
- `__x _y y__ x__` &nbsp;&nbsp;2 1 2 2 &nbsp;&nbsp;&nbsp;&nbsp;__x _y y__ x__ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  2 1 2 2      
- `__x _y y__ x_` &nbsp;&nbsp;&nbsp;&nbsp;2 1 2 1 &nbsp;&nbsp;&nbsp;&nbsp;__x _y y__ x_  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  2 1 2 1       
- `__x _y y_ x__` &nbsp;&nbsp;&nbsp;&nbsp;2 1 1 2 &nbsp;&nbsp;&nbsp;&nbsp;__x _y y_ x__  &nbsp;&nbsp;&nbsp;&nbsp;  2 1 1 2       
- `__x _y y_ x_` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2 1 1 1 &nbsp;&nbsp; __x _y y_ x_   &nbsp;&nbsp;&nbsp;  2 1 1 1      
- 
- `_x __y y__ x__` &nbsp;&nbsp;&nbsp;1 2 2 2 &nbsp;&nbsp;&nbsp;&nbsp;_x __y y__ x__ &nbsp;&nbsp;&nbsp; 1 2 2 2        
- `_x __y y__ x_` &nbsp;&nbsp;&nbsp;&nbsp;1 2 2 1&nbsp;&nbsp;&nbsp;&nbsp; _x __y y__ x_  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1 2 2 1        
- `_x __y y_ x_` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 2 1 1 &nbsp;&nbsp;&nbsp;&nbsp;_x __y y_ x_   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1 2 1 1     
- `_x __y y_ x__`&nbsp;&nbsp;&nbsp;&nbsp; 1 2 1 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; _x __y y_ x__  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1 2 1 2     
- `_x _y y__ x__`&nbsp;&nbsp;&nbsp;&nbsp; 1 1 2 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; _x _y y__ x__  &nbsp;&nbsp;&nbsp; 1 1 2 2     
- `_x _y y__ x_` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 1 2 1&nbsp;&nbsp;&nbsp;&nbsp; _x _y y__ x_   &nbsp;&nbsp;&nbsp; 1 1 2 1     
- `_x _y y_ x__` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 1 1 2&nbsp;&nbsp;&nbsp;&nbsp; _x _y y_ x__   &nbsp;&nbsp;&nbsp; 1 1 1 2       
- `_x _y y_ x_` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 1 1 1 &nbsp;&nbsp;&nbsp;&nbsp; _x _y y_ x_    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1 1 1 1       

____a b___   
____x a__ _b a_ a_  

* ### aaa
* #### aaa
* asdasdads  
<strong><em>qqq</em></strong>    
_x y</strong>___ _a b_ kk  
_____ ______ __a__