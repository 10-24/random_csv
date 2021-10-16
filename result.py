import random
import csv

def random_dic(dicts):
	dict_key_ls = list(dicts.keys())
	random.shuffle(dict_key_ls)
	new_dic = {}
	for key in dict_key_ls:
		new_dic[key] = dicts.get(key)
	return new_dic

def load():
	global origin
	configname="configuration.csv"
	with open (configname) as f:
		reader=csv.reader(f)
		header_row=next(reader)
		names=[]
		id=[]
		for row in reader:
			names.append(row[0])
			id.append(row[1])
		origin=dict(zip(names,id))

def start():
	global result
	global result_0
	result=random_dic(origin)
	result_0=list(result.keys())

def out():
	out_f="result.csv"
	f=open(out_f,"w",newline="",encoding="utf-8")
	csv_writer=csv.writer(f)
	for row in result_0:
		i=result[row]
		csv_writer.writerow([row]+[i])

origin={}
result={}
result_0=[]

load()
start()
out()



	










	
