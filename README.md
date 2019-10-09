## Intro Exercise to debugging
In this exercise you will find a small python code which contains several bugs.
The purpose is to find the bugs using `pdb` or `ipdb`.


## Requirments
This projects only requires python3+ and pip installed :)

## Tests
In order to make the bugs easier to find there are several test cases writen under [tests](/tests/debug_me/test_utils.py).
In order to run the tests run the following commands from the projects root direcotry 

```bash
pip install -e src
pip install -e tests
py.test
```

## Test Run
With the code there is also a file called `test.zip` which is encrypted with the password `1234`.
The worker should be able to crack the zip file.
In order to run the cracker please execute the following line from the projects root directory

```bash
python src/debug_me/worker test.zip . --password-length 5 --verbose
```

## Exercise Execution
1. All of the tests should pass
2. The worker should crack `super_secret_stuff.zip`
3. Only then should you look at the files of `super_secret_stuff.zip`

## The bugs
* generate_possible_options -> change `length == 0` to `length == 1`.
* get_all_posiible_passwords -> copy the given array before mutating it.
* get_arguments -> type of `--pasword-length` should be `int` it defaults to `str`.
