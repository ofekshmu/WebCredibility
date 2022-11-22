def main():
    from urllib.request import urlopen

    # Download from URL and decode as UTF-8 text.
    with urlopen( 'https://example.com/' ) as webpage:
        content = webpage.read().decode()

    # Save to file.
    with open( 'output.html', 'w' ) as output:
        output.write( content )

if __name__ == "__main__":
    main()