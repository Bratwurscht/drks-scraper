def Address(object):
    def __init__(self, institution, name, street, postcode, city, country, phone, fax, mail, url):
        self.institution = institution
        self.name = name
        self.street = street
        self.postcode = postcode
        self.city = city
        self.country = country
        self.phone = phone
        self.fax = fax
        self.mail = mail
        self.url = url
