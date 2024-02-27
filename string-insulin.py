# Store the human preproinsulin sequence in a variable called preproinsulin:
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
    "reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Store the remaining sequence elements of human insulin in variables:
f1 = open('ainsulin-seq-clean.txt', 'r')
aInsulin = f1.read()
f1.close()

f2 = open('binsulin-seq-clean.txt', 'r')
bInsulin = f2.read()
f2.close()

f3 = open('cinsulin-seq-clean.txt', 'r')
cInsulin = f3.read()
f3.close()

f4 = open('lsinsulin-seq-clean.txt', 'r')
lsInsulin = f4.read()
f4.close()

insulin = aInsulin + bInsulin

# Printing "the sequence of human insulin" to console using successive print() commands:
print("The sequence of human preproinsulin:")
print(preproInsulin)
# Printing to console using concatenated strings inside the print function (one-liner):
print("The sequence of human insulin, chain a: " + aInsulin)

# Calculating the molecular weight of insulin
# Creating a list of the amino acid (AA) weights
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
             'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
             'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
             'V': 117.15, 'W': 204.23, 'Y': 181.19}

# Count the number of each amino acids in insulin
aaCountInsulin = {x: insulin.upper().count(x) for x in ('A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N',
                                                        'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y')}
print(aaCountInsulin)

# Multiply the count by the weights
molecularWeightInsulin = sum({x: aaCountInsulin[x] * aaWeights[x] for x in ('A', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                                                                            'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S',
                                                                            'T', 'V', 'W', 'Y')}.values())
print(f'The rough molecular weight of Insulin is: {molecularWeightInsulin}')

# Note: The actual molecular weight of human insulin is 5807.63, but the program delivers 6696.42 because it
# ignores certain bonds and post-translational processing. To calculate the error percentage:
# error percentage = (| measured – accepted | / accepted)*100%

molecularWeightInsulinActual = 5807.63
error_percentage = ((molecularWeightInsulin - molecularWeightInsulinActual) / molecularWeightInsulinActual) * 100
print(f'Error_percentage: {error_percentage}')

