import cqc, numpy

indata = numpy.ones((5,6))
outdata = numpy.empty((5,6))
cqc.demo.fun(indata, indata.size, outdata)
print(outdata)
