from pythonnet import load
load("coreclr")
import clr
clr.AddReference("/home/zhongfu/package/Seq2SeqSharp/Seq2SeqSharp.dll")


from Seq2SeqSharp.Applications import DecodingOptions
from Seq2SeqSharp.Applications import Seq2SeqOptions
from Seq2SeqSharp.Applications import GPT
from Seq2SeqSharp.Applications import Seq2Seq
from Seq2SeqSharp.Corpus import Seq2SeqCorpusBatch
from Seq2SeqSharp.Utils import ModeEnums
from Seq2SeqSharp.Utils import ProcessorTypeEnums

class S2SOptions:
    def __init__(self):
        self._my_class = Seq2SeqOptions()

        

    def CreateDecodingOptions(self):
        return self._my_class.CreateDecodingOptions()

