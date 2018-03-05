import math, operator, sys

def scores_calculation(uni_tokens_dict,q):

	path = r'Document_IDs.txt'
	content = open(path, 'r').read()
	doc_ids = content.split("\n")

	path = r'Global_statistics.txt'
	content = open(path, 'r').read()
	lines = content.split("\n")
	avg_dl = float(lines[0].split(" : ")[1])
	dls = lines[2:]

	N = 1000
	k1 = 1.2
	b = 0.75
	k2 = 100
	R = 0
	r = 0
	qf = 1

	Ks = []
	for dl in dls:
		ratio = int(dl)/avg_dl
		Ks.append(k1*(1-b+(b*ratio)))

	q = q.split("\t")
	qid = q[0]
	query = q[1]
	terms = query.split()
	doc_freqs = []
	term_freqs = []
	for term in terms:
		tfs = []
		if term in uni_tokens_dict:
			total_freq = 0
			t = []
			doc_freqs.append(len(uni_tokens_dict[term]))

			for each in uni_tokens_dict[term]:
				t.append(int(each["tf"]))
				total_freq+=int(each["tf"])

			for doc_id in doc_ids:
				flag = False
				for each in uni_tokens_dict[term]:
					if each["docid"] == doc_id:
						tfs.append(int(each["tf"]))
						flag = True
						break
				if not flag:
					tfs.append(0)
			term_freqs.append(tfs)
		else:
			print("No results found for the keyword '"+term+"' in the query '"+query+"'")
			sys.exit(0)

	scores = {}
	for j in range(0,len(doc_ids)):
		score = 0
		for i in range(0,len(terms)):
			a = ((r+0.5)/(R-r+0.5))/((doc_freqs[i]-r+0.5)/(N-doc_freqs[i]-R+r+0.5))
			first = math.log(a)
			second = (k1+1)*term_freqs[i][j]/(Ks[j]+term_freqs[i][j])
			third = (k2+1)*qf/(k2+qf)
			this_term_score = first*second*third
			score+=this_term_score
		scores[doc_ids[j]] = score
	scores = sorted(scores.items(), key=operator.itemgetter(1), reverse=True)
	i = 1
	sc.write("\n\n"+query+":\n")
	for key,value in scores[:100]:
		sc.write("\n"+qid+" Q0 "+key+" "+str(i)+" "+str(value)+" OkapiBM25NoStopNoStem")
		i+=1


def extract_from_unigrams():
	
	uni_path = r'Unigrams.txt'
	uni_content = open(uni_path, 'r').read()
	uni_tokens_dict = {}
	lines = uni_content.split('\n')
	lines = [l for l in lines if l != ""]
	for line in lines:
		divide = line.split(' -> ')
		term = divide[0]
		uni_tokens_dict[term] = []
		each = divide[1].replace(')','').replace('(','').split(' ')
		for e in each:
			key_value = e.rsplit(',', 1)
			docid = key_value[0]
			tf = key_value[1]
			uni_tokens_dict[term].append({"docid":docid,"tf":tf})

	q_path = r'Queries.txt'
	uni_content = open(q_path, 'r').read()
	lines = uni_content.split('\n')
	for line in lines:
		scores_calculation(uni_tokens_dict,line)


sc = open("Scores.txt","w")
sc.write("Ranking (Top 100) for the queries in Queries.txt in the format:\n")
sc.write("query_id Q0 doc_id rank BM25_score system_name")
extract_from_unigrams()