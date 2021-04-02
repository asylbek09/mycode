#!/usr/bin/python3
import simpsons
"""Alta3 Resaerch | Building functions to test"""

# tests MUST begin with the word test_ or they will be ignored
def test_homer():
    # assert will return true or raise an AssertionError
    # the primary application is debugging
    assert simpsons.homer("doughnuts") == "You don't win friends with doughnuts"

# tests MUST begin with the word test_ or they will be ignored
def test_milhouse():
    # assert will return true or raise an AssertionError
    # the primary application is debugging
    assert simpsons.milhouse("daffodils") == "Everything is coming up daffodils"

# tests MUST begin with the word test_ or they will be ignored
def test_troymcclure():
    assert simpsons.troymcclure(5) == "2 minus 5 equals negative fun!"
    assert not simpsons.troymcclure(1)
    
# testing a failure
def test_homer_fail():
    # This should produce a failure.
    assert simpsons.homer("pretzels") == "You don't win friends with salad"
