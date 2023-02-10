class book:
    def __init__(self,title,author,publisher,price,copies,royalty):
        self.title=title
        self.author=author
        self.publisher=publisher
        self.price=price
        self.copies=copies
        self.royalty=royalty

    def settitle(self, x):
        self.title= x
    def setauthor(self, x):
        self.author= x
    def setpublisher(self, x):
        self.publisher= x
    def setprice(self, x):
        self.price= x
    def setcopies(self, x):
        self.copies= x


    def gettitle(self):
        return self.title
    def getauthor(self):
        return self.author
    def getpublisher(self):
        return self.publisher
    def getprice(self):
        return self.price
    def getcopies(self):
        return self.copies

    def royalty_method(self):
        if self.copies <= 500 :
            self.royalty  = 0.1*self.price*self.copies 
        if self.copies > 500 and self.copies <= 1500:
            self.royalty = 0.1*self.price*500 + 0.125*self.price*(self.copies - 500)
        if self.copies > 1500 :
            self.royalty = 0.1*self.price*500 + 0.125*self.price*1000 + 0.15*self.price*(self.copies - 1500)

        return self.royalty

b=book("Vivek's Biography","Vivek Kumar","Vivek K printing Ltd.",150,15000,0)
print("Book details : \n ")
print("Book name  :",b.gettitle())
print("Author :",b.getauthor())
print("Publisher :",b.getpublisher())
print("Price :",b.getprice())
print("No. of Copies :",b.getcopies())
print("Author's royalty :",b.royalty_method())


class ebook(book):
    def __init__(self,title,author,publisher,price,copies,royalty,foormat):
        super().__init__(title,author,publisher,price,copies,royalty)
        self.format=foormat

    def getformat(self):
        return self.foormat
    def setformat(self,x):
        self.format=x

    def royalty_method(self):
        if self.copies <= 500 :
            self.royalty  = 0.1*self.price*self.copies 
        if self.copies > 500 and self.copies <= 1500:
            self.royalty = 0.1*self.price*500 + 0.125*self.price*(self.copies - 500)
        if self.copies > 1500 :
            self.royalty = 0.1*self.price*500 + 0.125*self.price*1000 + 0.15*self.price*(self.copies - 1500)
        return 0.88*self.royalty



b=ebook("Vivek's Biography","Vivek Kumar","Vivek K printing Ltd.",150,15000,0,"pdf")
print("Book details : \n ")
print("Book name  :",b.gettitle())
print("Author :",b.getauthor())
print("Publisher :",b.getpublisher())
print("Format :",b.format)
print("Price :",b.getprice())
print("No. of Copies :",b.getcopies())
print("Author's royalty :",b.royalty_method())
