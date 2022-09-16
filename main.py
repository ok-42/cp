class COut:
    def __lshift__(self, other) -> 'COut':
        print(other, end='')
        return self

    def __repr__(self):
        return ''


# noinspection SpellCheckingInspection
cout = COut()

# noinspection SpellCheckingInspection
endl = '\n'

if __name__ == '__main__':
    cout << 1 << '2' << endl
