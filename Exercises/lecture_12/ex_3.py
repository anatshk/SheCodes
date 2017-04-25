"""
1. Rewrite the program from the first question of exercise 2 so that it prints the text of
    Python’s original exception inside the except clause instead of a custom message.
2. Rewrite the program from the second question of exercise 2 so that the exception which is
    caught in the except clause is re-raised after the error message is printed.

# Answer:
1.  except ValueError as e:
        print(e)
2.   except IndexError as e:
        print('Your index ({}) exceeds list length ({})'.format(index, len(thelist)))
        raise e
"""

