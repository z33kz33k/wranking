"""

    run.py
    ~~~~~~
    Run the code.

    @author: z33k

"""
# from goodreads import dump
# from meta import OTHER_AUTHORS
#
# dump(*OTHER_AUTHORS)
#


# from goodreads import AuthorParser
# parser = AuthorParser(fullname="Philip José Farmer")
# parser.fetch_stats_and_books()


# from meta.hn import scrape
# scrape(dump_json=True)


from meta.hn import Parser
parser = Parser()
parser.dump_reprs()
