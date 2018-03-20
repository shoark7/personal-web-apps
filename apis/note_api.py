def parse_post_request(parse_to):
    parse_to = parse_to[5:]
    post_id, color, coords = parse_to.split('::')
    return (post_id, color, coords)
