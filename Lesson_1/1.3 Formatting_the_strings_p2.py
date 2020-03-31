#python 2 formatting
waluta = "dolar"
us = 1
pln = 4.08234915
print("Aktualnie %r %r kosztuje %.2r zł" % (us, waluta, pln))

waluta = "dolar"
us = 1
pln = 4.08234915
print("Aktualnie %d %s kosztuje %.2f zł" % (us, waluta, pln))

# in old python version, while formating for:
# strings we use: %s
# floats: %f
# int:   %d
# any type: %r




#python 3 formatting
waluta = "dolar"
us = 1
pln = 4.08234915
print("Aktualnie {} {} kosztuje {} zł" .format(us, waluta, pln))


print("{3} {1} {2} {0}".format("apple", "grape", "green", "red"))

#in new python we use:
# {} and .format for any type