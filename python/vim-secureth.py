import hashlib

def update_hash(current_line: str) -> str:
    assert '@req' in current_line, "Must begin with '@req' indicator"
    statement = current_line.split('@req')[-1].lstrip()  # Everything after '@req'
    try:
        # If 'int()' succeeds, first chunk is hexidecimal
        current_hash = int(statement.split(' ')[0], 16)
        # Therefore, statement is everything after that
        statement = ' '.join(statement.split(' ')[1:])
    except ValueError:
        current_hash = 0x0  # First statement is not hex, do not process further

    new_hash = hashlib.sha256(statement.encode('utf-8')).hexdigest()[:4]  # First 4 digits (16 bits) of sha256 hash
    new_line = current_line.split('@req')[0] + '@req {} {}'.format(new_hash, statement)
    return new_line

if __name__ == '__main__':
    import sys
    print(update_hash(' '.join(sys.argv[1:])))
