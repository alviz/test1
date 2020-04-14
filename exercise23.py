

prime_list = []
with open('addon/primenumbers.txt','r') as file_prime:
    prime_list = [int(line.strip()) for line in file_prime]

print(prime_list)

overlap_list = []
with open('addon/happynumbers.txt','r') as file_happy:
    overlap_list = [int(line.strip()) for line in file_happy if int(line.strip()) in prime_list]

print(overlap_list)
