import wikipedia


def get_summary(title):
    try:
        page = wikipedia.page(title)
        return page.title, page.summary, page.url
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
        choice = input("Please try again: ")
        page = wikipedia.page(choice)
        return page.title, page.summary, page.url


def main():
    while True:
        user_input = input("Enter a page title or search phrase (or press Enter to quit): ")
        if not user_input:
            break

        title, summary, url = get_summary(user_input)
        print(f"\nTitle: {title}\nSummary:\n{summary}\nURL: {url}\n")


if __name__ == "__main__":
    main()