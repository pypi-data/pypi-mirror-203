from Seq2SeqSharp import Seq2SeqOptions
from Seq2SeqSharp import Seq2Seq
from Seq2SeqSharp import ModeEnums
from Seq2SeqSharp import ProcessorTypeEnums
from Seq2SeqSharp import Seq2SeqCorpusBatch

opts = Seq2SeqOptions()

opts.Task = ModeEnums.Test
opts.ModelFilePath = "./mt_chs_enu.model"
opts.InputTestFile = "./test.src"
opts.OutputFile = "./a.out"
opts.ProcessorType = ProcessorTypeEnums.CPU
opts.AMP = False

decodingOptions = opts.CreateDecodingOptions()

ss = Seq2Seq(opts)

ss.Test(opts.InputTestFile, opts.OutputFile, opts.BatchSize, decodingOptions, opts.SrcSentencePieceModelPath, opts.TgtSentencePieceModelPath, opts.OutputAlignmentsFile)



