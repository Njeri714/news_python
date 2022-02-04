class News:
    '''
    News class to define News Objects
    '''

    def __init__(self, id, title ,poster, url_link, description, published_date, content):
        self.id = id
        self.title = title
        self.poster = poster
        self.url_link = url_link
        self.description = description
        self.published_date = published_date
        self.content = content