def main():
    with open('lines.txt', "rt") as f, open('lines-copy.txt', "wt") as outfile:
        for line in f:
            # outfile.writelines(line)
            print(line.rstrip(), file=outfile)
            print('.', end='', flush=True)
    
    print('\done.')


if __name__ == "__main__":
    main()