# Feedback

## Section 1
### Testing and Pure Functions
 
Using the `@pytest.fixture` to ensure that your data is fresh is great! _However_, is has really hindered your ability to increment. In make_name_tags, there are several behaviours to cover:
  -   `make_name_tags` should return a new list
  -   `make_name_tags` should add a `name_tag` property to a dictionary inside a list
  -   `make_name_tags` should be able to add `name_tag` properties to multiple dictionaries
  -   `make_name_tags` should not mutate the original data

Right now, you're only doing two of these, although it _looks_ like you're doing three. Your first test ensures that whatever is returned from `make_name_tags` looks like a list, but doesn't check that it is not in fact the one that is passed to it.

How would you go about testing that it is not the same list that has been passed to the function?

## Section 2
### OOP and testing

For your `add_stock` method, I really appreciate your testing here, it's very thorough! I would suggest that the 'replacement stock' would be a separate test, as the 'replacement' is technically separate intended behaviour.

You've tested for `Exceptions` really well, but convention would usually suggest testing for that _after_ the test case in which everything goes well. Realistically, this is because developers will read your test suites from top to bottom, so therefore it makes sense to see the intention of the method _before_ seeing the 'misuses'.

## Section 3
### Higher Order Functions and Closure

Excellent list comprehension in `generate_multiples`! Nice and clear variable names too for `multiple` and `list_length`. 

Again, lovely solution for `capitaliser`, including the naming of the inner function. I think storing your function output is a good thing to ensure also. Well done!

## Section 4
### Iterators, Iterables and Generators

Lovely solutions throughout! I'd advise that if you're using `'index'`, then you should probably use `'char'` or `'character'` too. If you had written `'index'` as `'i'`, I wouldn't have thought about it really, but because you've determined a convention with index, I would expect to see it continued with 'c'.

I'd really like to see you attempt to write `cool_cat` as an Iterator, for the challenge.

## Section 5
### Recursion

Your incrementation of testing here is great - a real show of understanding and taking smaller steps. Well done.
