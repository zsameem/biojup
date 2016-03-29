import ipywidgets as widgets
from traitlets import Unicode, List

class MsaParseUrl(widgets.DOMWidget):
    _view_name = Unicode('MsaParseUrlView').tag(sync=True)
    parse_url = Unicode('').tag(sync=True)



#Parse local sequence files and render them with msa
class MsaParseClustal(widgets.DOMWidget):
    _view_name = Unicode('MsaParseClustalView').tag(sync=True)
    seq_list = List([]).tag(sync=True)
    #location of the file to be parsed
    def __init__(self, loc, ftype):
        try:
            from Bio import AlignIO
        except ImportError:
            raise ImportError("No module named Bio. Make sure you have BioPython installed")
        tmp_list = []
        """
            Parse the clustal file using the appropriate parser of BioPython and
            make the parsed output to match the format for msa viewer and then
            append it to seq_list
        """
        align = AlignIO.read(loc, ftype)
        for seq in align:
            name = seq.name
            #handle unknown names so that output is not ugly
            if name == "<unknown name>":
                name = ""
            id = seq.id
            seqs = str(seq.seq)
            self.seq_list.append({'name':name, 'id':str(id), 'seq':seqs, 'height':1, 'ref':False })
        super(MsaParseClustal, self).__init__()
