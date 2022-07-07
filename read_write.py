def read_data():
    with open('input.txt', 'r') as f:
        data: str
        data = f.read()
    return data


def write_data(accepted: bool):
    with open('output.txt', 'w') as f:
        f.write('ACCEPT' if accepted else 'REJECT')
