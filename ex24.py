print("练习所有所学的")
print('you\'d need to know \'bout escape with \\ that do:')
print('\n newlines and \t tab')

poem="""
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("."*10)
print(poem)
print("."*10)

five=10-2+3-6
print(f'\n{five}')
def secret_formula(started):
    jelly_beans=started*500
    jars=jelly_beans/1000
    crates=jars/100
    return jelly_beans,jars,crates


print(secret_formula(10000))
