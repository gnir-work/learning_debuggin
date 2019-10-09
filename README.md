## Intro Exercise to debugging
In this exercise you will find a small python code which contains several bugs.
The purpose is to find the bugs using `pdb` or `ipdb`.

## Tests
In order to make the bugs easier to find there are several test cases writen under [tests](/tests).
In order to run the tests run the following commands from the root of the directory

```bash
pip install -e src
pip install -e tests
py.test
```

## The bugs
* generate_possible_options -> change `length == 0` to `length == 1`.
* get_all_posiible_passwords -> copy the given array before mutating it.
* get_arguments -> type of `--pasword-length` should be `int` it defaults to `str`.
