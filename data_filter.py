import numpy as np

# read expression file and replace tabs by spaces
expr_file_tab = open("HiSeqV2.txt", "r");
expr_file_space = expr_file_tab.read().replace("\t", " ")

# write modified expression file
expr_file = open("HiSeqV2_Mod.txt", "w")
expr_file.write(expr_file_space)
expr_file.close()

# read modified expression file
expr_file = open("HiSeqV2_Mod.txt", "r")

# read data from modified expression file
data = np.genfromtxt(expr_file, skip_header = 1, dtype = 'float', usecols = range(1, 1219))
expr_file.close()

expr_file = open("HiSeqV2_Mod.txt", "r")
samples = np.genfromtxt(expr_file, skip_footer = 20530, dtype = 'string')
expr_file.close()

expr_file = open("HiSeqV2_Mod.txt", "r")
identifiers = np.genfromtxt(expr_file, skip_header = 1, dtype = 'string', usecols = range(1,))
print "Data read successfully"

zero_count = 0
zero_count_25 = 0
zero_count_50 = 0
zero_count_75 = 0
zero_count_90 = 0
zero_array = np.zeros((data.shape[0],))

# count number of zero expression instances for each of the identifiers
for i in xrange(data.shape[0]):
	count = 0
	for j in xrange(data.shape[1]):
		if(data[i][j] == 0):
			count += 1
	zero_array[i] = count

np.savetxt("zero_expression_counts.txt", zero_array.astype(int), fmt = '%i');
print "Zero expression counts file created successfully"

# calculate number of identifiers with at least x zero expression instances
percent_map = {1:[1, zero_count], 25:[305, zero_count_25], 50:[609, zero_count_50], 75:[914, zero_count_75], 90:[1096, zero_count_90]}
percent_chosen = [75, 90]

for i in xrange(zero_array.shape[0]):
	for j in percent_chosen:
		if(zero_array[i] >= percent_map[j][0]):
			percent_map[j][1] += 1

print "Number of identifiers with at least one zero expression instance", zero_count
for j in percent_chosen:
	print "Number of identifiers with at least", j, "per cent zero expression instance", percent_map[j][1]


# removing all identifiers with at least x per cent zero expression
for j in percent_chosen:
	modified_data = []
	modified_identifiers = []

	for i in xrange(data.shape[0]):
		if zero_array[i] < percent_map[j][0]:
			modified_data.append(data[i,:])
			modified_identifiers.append(identifiers[i])
			x = j
	
	modified_identifiers = np.array(modified_identifiers)
	modified_data = np.array(modified_data)
	modified_data = np.concatenate((modified_identifiers[:, None], modified_data), axis = 1)
	modified_data = np.concatenate((samples[None,:], modified_data), axis = 0)
	print "Data where identifiers with at least", x, "per cent zero expression are removed created successfully"

	np.savetxt("HiSeqV2_Filtered_" + `j` + ".txt", modified_data, fmt = '%s', delimiter = '\t');
	print "Zero expression filtered file created successfully"
