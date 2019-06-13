# Copyright (c) European Synchrotron Radiation Facility (ESRF)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the 'Software'), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import unittest

from utils import UtilsTest

from tasks import ReadImageHeader


class ReadImageHeaderTasksExecTest(unittest.TestCase):

    def setUp(self):
        self.dataPath = UtilsTest.prepareTestDataPath(__file__)

    def test_readCBFHeader(self):
        referenceDataPath = self.dataPath / 'ControlReadImageHeader.json'
        inData = UtilsTest.loadAndSubstitueTestData(referenceDataPath)
        readImageHeader = ReadImageHeader(inData=inData)
        dictHeader = readImageHeader.readCBFHeader(inData['image'])
        self.assertEqual(
            dictHeader['Detector:'],
            'PILATUS2 3M, S/N 24-0118, ESRF ID23'
        )

    def test_execute_ReadImageHeader(self):
        referenceDataPath = self.dataPath / 'ControlReadImageHeader.json'
        inData = UtilsTest.loadAndSubstitueTestData(referenceDataPath)
        readImageHeader = ReadImageHeader(inData=inData)
        readImageHeader.execute()
        assert readImageHeader.isSuccess()
        outData = readImageHeader.outData
        assert outData is not None


