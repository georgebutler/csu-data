class Course:
    def __init__(self, id, catalog, desc):
        self.id = id.strip()
        self.catalog = catalog.strip()
        self.desc = desc.strip()
        self.sections = []
        self.yearly_enrolled = 0
        self.yearly_enrolled_avg = -1
        self.yearly_enrolled_lowest = -1
        self.yearly_enrolled_highest = -1
        self.yearly_enrolled_median = -1

    def __eq__(self, other):
        return self.id == other.id
    
    def __repr__(self):
        return (f'{self.__class__.__name__}('f'{self.catalog!r}, {self.desc!r})')

    def add_section(self, section):
        if section not in self.sections:
            self.yearly_enrolled = int(self.yearly_enrolled + section.enroll_total)
            self.sections.append(section)