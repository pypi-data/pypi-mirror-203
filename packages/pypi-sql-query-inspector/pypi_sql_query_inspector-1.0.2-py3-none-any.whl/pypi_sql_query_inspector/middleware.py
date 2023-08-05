from decimal import Decimal
from django.conf import settings
from django.db import connection
from pygments import highlight
from pygments.lexers.sql import SqlLexer
from pygments.formatters import TerminalFormatter
from sqlparse import format


def print_sql_queries_to_terminal(get_response):

    def middleware(request):
        response = get_response(request)

        if settings.DEBUG:
            queries = connection.queries
            num_queries = len(queries)
            total_execution_time = Decimal()
            check_duplicates = set()

            for q in queries:
                total_execution_time += Decimal(q.get('time'))
                check_duplicates.add(q.get('sql'))
                sqlformatted = format(q.get('sql'), reindent=True)
                print(highlight(sqlformatted, SqlLexer(), TerminalFormatter()))

            print("===========")
            print("[SQL Stats]")
            print(f"{num_queries} Total queries")
            print(f"{num_queries - len(check_duplicates)} Total duplicates")
            print(f"{total_execution_time}")
            print("===========")

        return response

    return middleware

