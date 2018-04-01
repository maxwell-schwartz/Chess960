import argparse
import json

def permutate(l):
    
    if len(l) <= 1:
        return l
    
    variations = []
    for perm in permutate(l[1:]):
        for i in range(len(l)):
            variations.append(perm[:i] + l[0:1] + perm[i:])
            
    return variations

def is_legal_position(l):
    
    r_indices = [(i, r) for i, r in enumerate(l) if r == 'R']
    k_index = l.index('K')
    if not (r_indices[0][0] < k_index and r_indices[1][0] > k_index):
        return False
    
    b_indices = [(i, b) for i, b in enumerate(l) if b == 'B']
    if not (b_indices[0][0] % 2) + (b_indices[1][0] % 2) == 1:
        return False
    
    return True

def main():
    parser = argparse.ArgumentParser(prog='chess960.py')
    parser.add_argument('-o', dest='output_file', help="Output file")
    args = parser.parse_args()

    all_options = permutate('RNBQKBNR')
    options = []
    for a in all_options:
        if a not in options:
            options.append(a)
    legal_positions = [o for o in options if is_legal_position(o)]
    positions = {}
    for ind, l in enumerate(legal_positions):
        w = ['w' + p + ('b' if i % 2 == 0 else 'w') + '.jpeg' for i, p in enumerate(l)]
        b = ['b' + p + ('w' if i % 2 == 0 else 'b') + '.jpeg' for i, p in enumerate(l)]
        positions[ind] = {}
        positions[ind]['w'] = w
        positions[ind]['b'] = b
    out_string =  json.dumps(positions)
    with open(args.output_file, 'w') as outfile:
        outfile.write('var positions = ' + out_string)

if __name__ == '__main__':
    main()