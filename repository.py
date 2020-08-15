class RepoLocal:
    auto_init = True
    license = 'gpl-3.0'
    def __init__(self, name, description, private):
        self.name = name
        self.description = 'This is the description for {} repository'.format(name) if not description else description
        self.private = False if not private else True

