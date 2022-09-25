class COut:
    def __lshift__(self, other) -> 'COut':
        print(other, end='')
        return self

    def __repr__(self):
        return ''


class COut2:

    def __init__(self):
        self.strings: list[str] = []

    def __lshift__(self, other) -> 'COut2':
        self.strings.append(str(other))
        return self

    def __repr__(self) -> str:
        return ' '.join(self.strings)


# noinspection SpellCheckingInspection
cout = COut()

# noinspection SpellCheckingInspection
endl = '\n'

if __name__ == '__main__':
    cout << 1 << '2' << endl
