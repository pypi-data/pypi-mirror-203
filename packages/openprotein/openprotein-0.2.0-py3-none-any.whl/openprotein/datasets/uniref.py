from openprotein.data.factory import Data


class Uniref(Data):
    """
    UniProt Reference Cluster (UniRef) databases provide clustered sets of sequences from UniProtKB and selected
    UniParc records.

    Args:
        path (str): path for the dataset

    Examples:
        1:
        >>> from openprotein.data import MaskedConverter
        >>> from openprotein.datasets import Uniref
        >>> data = Uniref("./resources/uniref50/valid")
        >>> dataset = data.get_data()
        >>> print(dataset[0])
        MKWTNAGSRRGSKKAAPSARPLPVNLRLNDFSDDELHLATRRSTGNSPDAPPQAERVGYSQLTVLIAELRRSSRLGRSTCAEVTRHYPAIIYVFVFTRCLPQPNSCST

        2:

        >>> proteinseq_toks = {
                'toks': ['L', 'A', 'G', 'V', 'S', 'E', 'R', 'T', 'I', 'D', 'P', 'K', 'Q', 'N', 'F', 'Y', 'M', 'H', 'W',
                        'C','X', 'B', 'U', 'Z', 'O', '.', '-']
            }
        >>> converter = MaskedConverter(proteinseq_toks["toks"])
        >>> f = lambda x: converter(x)
        >>> dl = data.get_dataloader(batch_size=4, collate_fn=f)
        >>> for i, j, k in dl
                print(i)
        tensor([[32, 20, 15,  ..., 21, 11,  2],
                [32, 20,  8,  ...,  1,  1,  1],
                [32, 20,  8,  ...,  1,  1,  1],
                [32, 20, 18,  ...,  1,  1,  1]])
    """

    def __init__(self, path: str):
        super().__init__(path)

        # self._dataset = DataFactory.load(self, path)
