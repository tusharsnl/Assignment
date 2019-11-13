def group_by_ownwers(sample):
    result = {}
    for file, owner in sample.items():
        result[owner] = result.get(owner, []) + [file]
    return result

sample1 = {
    'input.txt': 'rand',
    'dock.py': 'pary',
    'sample.py': 'rand',
    'uganda.doc': 'jery',
    'jack.txt' : 'rand'
}

print(group_by_ownwers(sample1))
