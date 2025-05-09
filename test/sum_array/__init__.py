import check50

@check50.check()
def exists():
     #Checks if sum_of_array.c file exists"""
     check50.exists('sum_of_array.c')

@check50.check(exists)
def compiles():
     #Check if sum_of_array.c compiles successfully
     check50.run('gcc -o sum_of_array sum_of_array.c')
     
@check50.check(compiles)
def checkResult():
     
     result = check50.run('./sum_of_array').stdin('12 45 66 77 11')
     
     expected_output = 'Sum: 211'
     
     if expected_output not in result:
          help = f'Expected result:\nSum: 211\n Your result is\n {result}'
          raise check50.Mismatch(expected_output, help=help)

@check50.check(compiles)
def checkFloating():
     
     result = check50.run('./sum_of_array').stdin('12.6 45.4 66 77 11')
     
     expected_output = 'Sum: 212'
     
     if expected_output not in result:
          help = f'Expected result:\nSum: 212\n Your result is\n {result}'
          raise check50.Mismatch(expected_output, help=help)
     