
def app(environ, start_response):
    qs = environ['QUERY_STRING']
    query_data = b""
    query_data_len = 0
    if qs:
        kv = qs.split('&')
        query_data = "\n".join(kv).encode()
        query_data_len = len(query_data)
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(query_data_len))
    ])
    return iter([query_data])
