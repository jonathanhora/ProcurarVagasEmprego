
from indeed import search_keyword
#from stackoverflow import sof_keyword
from save import save_to_csv

search = input("Informe a área que deseja: \n")

result = search_keyword(search)
save_to_csv(result)

#sof_keyword('python')