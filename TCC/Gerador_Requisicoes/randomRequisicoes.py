import random

setor = ['100','010','001']
att = ['100','110','111','101','010','011','001']
loc = ['0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
notas = ['100']
#notas = ['100','010','001']

def main():
	count = 0
	for i in range(len(setor)):
		for j in range(len(att)):
			for k in range(len(loc)):
				for l in range(len(notas)):
					#print(str(i)+'\t-\t'+str(j)+'\t-\t'+str(k)+'\t-\t'+str(l))
					nome_arquivo = 'req'+str(count)+'.txt'
					f = open(nome_arquivo, 'w')
					f.write(setor[i]+'\n')
					f.write(att[j]+'\n')
					f.write(loc[k]+'\n')
					f.write(notas[l])
					f.close()
					count += 1

	#print(count)
if __name__ == "__main__":
	main()