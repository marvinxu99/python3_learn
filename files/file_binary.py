def main():
    with open('berlin.jpg', "rb") as infile, \
            open('berlin-copy.jpg', "wb") as outfile:
        while True:
            buf = infile.read(10240)  # 10k
            if buf:
                outfile.write(buf)
                print('.', end='', flush=True)
            else:
                break
    print('\done.')

if __name__ == "__main__":
    main()