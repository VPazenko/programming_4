# imports
from Bio import Entrez
import multiprocessing as mp

class PubMed_references:
    """
    This class is designed to find all references of a selected article (article id required) 
    in the pubmed database. It is also possible to save all or a few of these references in .xml format
    """
    def __init__(self, article_id, your_api_key, your_email):
        self.target_id = article_id
        self.api_key = your_api_key
        self.email = your_email
        self.references = self.obtain_all_refs()


    def obtain_all_refs(self):
        """
        Function create a list of referenses ids (using target id). 
        Output: list of str
        """
        Entrez.email = self.email 
        file = Entrez.elink(dbfrom="pubmed",
                        db="pmc",
                        LinkName="pubmed_pmc_refs",
                        id=self.target_id,
                        api_key=self.api_key)
        results = Entrez.read(file)
        return [f'{link["Id"]}' for link in results[0]["LinkSetDb"][0]["Link"]]


    def save_article_in_xml(self, id):
        """
        Function save the article in .xml format (using any id)
        """
        handle = Entrez.efetch(db="pubmed",
                id=id,
                retmode="xml",
                api_key=self.api_key)
        xml = handle.read()
        name = './refs/' + id + '.xml'
        file =  open(name, "wb")
        file.write(xml)
        file.close()


    def save_first_n_refs_xml_without_mp(self, n = 10):
        """
        Function save n articles in .xml format (using references list)
        """        

        if n >= len(self.references):
            print('The inputted number is greater than the total number of references. '
                    f'A new number has been selected. n = {len(self.references)}')
            n = len(self.references)

        for id in self.references[:n]:
            self.save_article_in_xml(id)


    def save_first_n_refs_xml_with_mp(self, n = 10):
        """
        Function save n articles in .xml format (using references list)
        Using multiprocessing
        """     
        if n >= len(self.references):
            print('The inputted number is greater than the total number of references. '
                    f'A new number has been selected. n = {len(self.references)}')
            n = len(self.references)

        with mp.Pool() as p:
            p.map(self.save_article_in_xml, self.references[:n])


if __name__ == "__main__":
    print(__doc__)
else:
    print(f"Module '{__name__}' is imported successfully!\n")