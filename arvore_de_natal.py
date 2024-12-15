def arvore_natal(altura):
    for i in range(altura):
        print(' ' * (altura - i - 1) + '*' * (2 * i + 1))

    for j in range(2):
        print(' ' * (altura - 1) + '|')

def main():
    num = int(input())

    arvore_natal(num)

main()