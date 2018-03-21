def parse_post_request(parse_to):
    parse_to = parse_to[5:]
    *_, color, coords = parse_to.split('::')
    return color, coords
