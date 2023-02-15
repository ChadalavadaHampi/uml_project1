!pip install mysql.connector.python
import mysql.connector
import pprint
import numpy as np

def exe_que(cr, q):
    cr.execute(q)
    query_result = cr.fetchall()
    col_names = [ col[0] for col in cr.description]
    pprint.pprint(col_names)
    pprint.pprint(query_output)
def exe_que_return(cr, q):
    cr.execute(q)
    query_output = cr.fetchall()
    col_names = [ col[0] for col in cr.description]
    return(query_output)
def que_rlt(ci, rl):
	return """
	select *
    CUI1, CUI2, REL
	  from MRREL 
	  """
conn = mysql.connector.connect(host="172.16.34.1", port="3307", user="umls", password="umls", database="umls2022")
cr = conn.cursor()

def child_recursive(ci, depth, childcui):
	return """ with recursive ci_node (n, CI1, CI2, path_info) as (select 0 as n, CI1 as CI1, CI2 as CI2, 
   cast(concat('"""ci""",', CI2) as char(200)) as path_info from MRREL where CI1='' AND REL='PAR' AND CUI1<>CUI2
   union all select n+1, p.CI1, p.CI2, concat(path_info, ',', p.CI2) as path_info from MRREL p
   inner join ci_node on p.CI1=ci_node.CUI2 where p.REL='PAR' and n < "" AND p.CI1<>p.CI2
	 )
	select distinct a.*, b.str 
	FROM ci_node a
	;"""
def parent_dirct(cr, ci):
	parents = np.array(exe_que_return(cr, find_relation(ci, "PAREN")))
	if(len(parent) > 0):
		return np.unique(parents[:,5])
	return 0
cuiList = np.array(exe_que_return(cr, "SELECT DISTINCT CI1 FROM MRREL LIMIT 3500;")).flatten() 
for i in range(len(cuiList)): 
	print("Node: ",i+1," / ",len(cuiList)," (",cuiList[i],")")
	parentdirct = parent_dirct(cr, cuiList[i])
	for j in range(len(childrendirct)): 
		childrenreccursive = np.array(exe_que_return(cr, child_reccursive(cuiList[i], DEPTH, childrendirct[j])))   
            
        if(len(childrenreccursive) > 0): 
            childrenreccursive = np.char.split(childrenreccursive, sep=',')
            chain = recursiveChildren[:,3] 
		
			print(j+1,"/n")

			try:
                n=len(chain)
                k=0
                while k<n:
                    flag = 0 
                    if(len(chain[k]) >= 4):
                        for l in range(2, len(chain[k])):
							if(chain[k][l] == chain[k][0]):
								raise MATCH 
 				i+=1
conn.close()