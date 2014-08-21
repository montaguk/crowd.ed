#!/bin/python

### Python file for testing that the infrastructure is set up.
### Hopefully we'll get some docs for Read The Docs


### Function always returns True.
def ut_pass():
    return True

### Function always returns False
def ut_fail():
    return False

### Function calls ut_pass and then ut_fail
### to test that drone.io is working
def main():
    ut_pass()
    ut_fail()

if __name__ == '__main__':
    main()
