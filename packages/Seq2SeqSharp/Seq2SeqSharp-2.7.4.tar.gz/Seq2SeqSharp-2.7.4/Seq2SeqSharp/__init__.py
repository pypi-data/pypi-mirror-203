from pythonnet import load
load("coreclr")
import clr
import os
import sys

dir = os.path.dirname(sys.modules["Seq2SeqSharp"].__file__)
path = os.path.join(dir, "Seq2SeqSharp.dll")
clr.AddReference(path)

from Seq2SeqSharp.Applications import DecodingOptions
from Seq2SeqSharp.Applications import Seq2SeqOptions
from Seq2SeqSharp.Applications import GPT
from Seq2SeqSharp.Applications import Seq2Seq
from Seq2SeqSharp.Corpus import Seq2SeqCorpusBatch
from Seq2SeqSharp.Utils import ModeEnums
from Seq2SeqSharp.Utils import ProcessorTypeEnums

