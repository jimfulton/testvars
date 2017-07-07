===================================================
testvars - Place-holders in complex test assertions
===================================================

Sometimes, when writing tests, you want to assert that a data
structure computed in a test matches some expected value, but the
expected value might have components, such as times or generated ids
that can't be predicted ahead of time.  Options in this situation
include:

- break the assertion into many assertions about various parts of the
  data structure.

- Use mocking/stubbing to control things like time and ids to make
  unpredictable parts of the data predictable.

Both of these approaches tend to be pretty tedious and potentially
error prone.

The tiny testvars package provides an alternative that is much easier
to use in many cases.  The package provides a ``Vars`` class::

  >>> import testvars
  >>> vars = testvars.Vars()

When ``Vars`` attributes are compared equal the first time, the
comparison succeeds and alse sets their value:

  >>> vars.x == 1
  True

At that point, the value is set, and you can make assertions
against it:

  >>> vars.x
  1
  >>> vars.x > 0
  True

Further comparisons are against this set value:

  >>> vars.x == 2
  False

This is useful when dealing with data structures with unpredictable
parts:

  >>> expected = {'id': vars.child_id, 'name':"Alex"}
  >>> {'id': 32, 'name':"Alex"} == expected
  True

It's also interesting when, while you don't know what values will be,
you can make assertions about how values are related:

  >>> expected = {'id': vars.parent_id, 'name':'Cas',
  ...             'children': [vars.child_id]}
  >>> expected == {'id': 42, 'name':'Cas', 'children':[32]}
  True
  >>> expected == {'id': 42, 'name':'Cas', 'children':[33]}
  False

  >>> [vars.y, 2, 3, vars.y] == [9, 2, 3, 9]
  True

  >>> [vars.z, 2, 3, vars.z] == [8, 2, 3, 9]
  False
