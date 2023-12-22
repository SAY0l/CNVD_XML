from cli.cli import *

class App:
    Description = "CNVD_XML: Collect and Store CNVD_XML Data Rapidly"
    Author = "sayol"
    Email = "github@sayol.com"
    Verion ="1.0"
    Ps = ">>> Please edit base.py file when u first use <<<"

    def __init__(self) :
        Gen_cli([self.Description, self.Author, self.Email, self.Verion,self.Ps])


if __name__ == "__main__":
    start = App()