
import check50

@check50.check()
def exists():
    """Checks if cube.c exists"""
    check50.exists("cube.c")
     
@check50.check(exists)
def compiles():
    """Checks if cube.c compiles successfully"""
    check50.run("gcc -o cube cube.c").exit(0)


@check50.check(compiles)
def test_0:
     """Checks if the program correctly calculates the cube of a number."""
     result = check50.run("./cube.c").stdin("23").stdout()

     expected_output = "12167"

     if expected_output not in result:
        raise check50.Mismatch(expected_output, result, help="Make sure your program correctly cubes the input and prints the result.")

@check50.check(compiles)
def test_1:
     """Another check for correct cubing."""
     result = check50.run("./cube.c").stdin("42").stdout()

     expected_output = "74088"

     if expected_output not in result:
        raise check50.Mismatch(expected_output, result, help="Double-check your cubing logic with a different number.")

@check50.check(compiles)
def test_error_2:
     """Reject A: Checks for a rejectable non-numeric input..
Your program should reject non-numeric input. Make sure you're checking for valid numbers."""
     check50.run("./cube.c").stdin("A").reject()
  

@check50.check(compiles)
def test_error_3:
     """Reject : Checks for a rejectable empty input..
Your program should reject empty input. Add a check to handle an empty string."""
     check50.run("./cube.c").stdin("").reject()
  

