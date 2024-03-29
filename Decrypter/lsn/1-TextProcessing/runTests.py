import sys
import unittest

import tests

class TermColor:
    # I've verified that these colors work on PyCharm as well!
    BOLDRED = '\033[1;31m'
    BOLDGRN = '\033[1;32m'
    BOLDYLW = '\033[1;33m'
    BOLDCYAN = '\033[1;36m'
    ENDC = '\033[0m'
    WHITE = '\033[1;37m'
    YLW = '\033[33m'
    UNDERLINE = '\033[4m'

class TestContainer:
    def __init__(self, testClass, argName, title, desc="", silenced=False):
        '''
        testClass: Class -- Pointer to TestCase Class to build the tests from
            OR  testClass may be a list of classes instead, if you want to group
                multiple TestCase objects together
        argName: String -- Name to be supplied to sys.argv
        title: String -- Title of the test
        desc: String -- Description of the TestCase class to be run
        silenced: Boolean -- If silenced is set to true, pre/post processes are
            skipped
        '''
        self.testClass = testClass
        self.argName = argName
        self.title = title
        self.desc = desc
        self.suite = None
        self.result = None
        self.pre = None
        self.post = None
        self.silenced = silenced

    def makeSuite(self):
        if self.suite:
            return self.suite

        # if the user provides multiple TestCase classes, place them all into a
        # suite
        elif isinstance(self.testClass, list) or isinstance(self.testClass, tuple):
            self.suite = unittest.TestSuite()
            for cls in self.testClass:
                self.suite.addTest(unittest.makeSuite(cls))
            return self.suite

        self.suite = unittest.makeSuite(self.testClass)
        return self.suite

    def runTest(self):
        '''
        Called to execute the test
        '''

        # Runs pre-test execution functions
        if not self.silenced:
            self.preTestPrint()
            if self.pre:
                for func in self.pre:
                    func()

        if not self.suite:
            self.makeSuite()
        self.runner = unittest.TextTestRunner(verbosity=2, stream=sys.__stdout__, )
        self.result = self.runner.run(self.suite)

        # Runs post-test execution functions
        if not self.silenced:
            self.postTestPrint()
            if self.post:
                for func in self.post:
                    func()

    def preTestPrint(self):
        '''
        Will be used to print something before a test is run
        '''
        print("=" * 70)
        print(f"{TermColor.BOLDYLW + TermColor.UNDERLINE}Tests for {self.title}{TermColor.ENDC}")
        if self.desc:
            print(f"{TermColor.YLW}{self.desc}{TermColor.ENDC}")
        print("=" * 70)

    def postTestPrint(self):
        '''
        Will be used to print something after a test is run
        '''
        print()

    def setPre(self, listOfFunctions):
        '''
        listOfFunctions: List of parameterless function pointers that are called
        before the test is run
        '''
        if isinstance(listOfFunctions, list):
            self.pre = listOfFunctions

    def setPost(self, listOfFunctions):
        '''
        listOfFunctions: List of parameterless function pointers that are called
        after the test is run
        '''
        if isinstance(listOfFunctions, list):
            self.post = listOfFunctions


def welcomeMessage(tests):
    msg = f"""\
Welcome to the DuckieCorp's automated testing system! Verify if you have
successfully completed the requested lesson exercises.
{TermColor.WHITE + TermColor.UNDERLINE}
You have requested tests on the following exercises:
{TermColor.ENDC}"""
    msg += TermColor.BOLDCYAN
    for test in tests:
        msg += f"    {test.title}\n"
    msg += TermColor.ENDC
    print(msg, end="")


def runTests(tests):
    welcomeMessage(tests)

    for test in tests:
        test.runTest()

    # Check All Results
    success = True
    for test in tests:
        result = test.result
        if not result.wasSuccessful():
            success = False
            break

    if success:
        print(f"""\
{TermColor.BOLDGRN + TermColor.UNDERLINE}\
SUCCESSFULLY PASSED ALL REQUESTED TESTS\
{TermColor.ENDC}
    Congratulations! Your code passes all of the tests that were ran. This
    likely means you will be receiving a good score when your code goes through
    the code review process.  However, be sure to double check that your work
    meets the requirements, to ensure that DuckieCorp code reviewers won't find
    something that these tests may have missed!{TermColor.ENDC}""")

    else:
        print(f"""\
{TermColor.BOLDRED + TermColor.UNDERLINE}\
DID NOT PASS ALL REQUESTED TESTS\
{TermColor.ENDC}
    One or more of your segments of code did not pass the tests. Check through
    the error logs above for a more detailed diagnosis of the problem. Sorry my
    friend, better luck next time.

    The following tests encountered an error or failed:{TermColor.BOLDRED}""")
        # LOG THE FAILURES/ERRORS TO THE USER:
        for test in tests:
            result = test.result
            if not result.wasSuccessful():
                print("    " * 2 + test.title)
                for err in result.errors:
                    print("    " * 3 + "ERROR: " + str(err[0]))
                for fail in result.failures:
                    print("    " * 3 + "FAILURE: " + str(fail[0]))
        print(TermColor.ENDC, end="")


ALL_TESTS = [
    TestContainer(testClass=tests.testEX0.ExerciseTests,
                  argName="0",
                  title="Text Processing Exercise 0",
                  desc="""\
    test_validity:
        Tests the validity of the output.
            EX: findWords(["keep reject"]) == ["keep"]
    test_emptyList:
        Tests the validity of the output when an empty list is expected.
            EX: findWords("reject") == []
                findWords("") == []"""),
    TestContainer(testClass=tests.testEX1.ExerciseTests,
                  argName="1",
                  title="Text Processing Exercise 1",
                  desc="""\
    test_validity:
        Tests whether or not the output of exercise 1 is correct. Extra white
        space at the start or end of a string will not affect the tests.
            EX: Ensures everyOtherWord("1 2 3 4 5 6 7 8") == "2 4 6 8"\
"""),
    TestContainer(testClass=tests.testEX2.ExerciseTests,
                  argName="2",
                  title="Text Processing Exercise 2",
                  desc="""\
    test_emptyList:
        Tests that the function returns an empty list when expected.
            EX: cleanSentence("#Nothing") == []
    test_validity:
        Tests the validity of the output with a list as input.
            EX: Ensures cleanSentence("What #do you expect?") == ["What", "you", "expect?"]"""),
    TestContainer(testClass=tests.testEX3.ExerciseTests,
                  argName="3",
                  title="Text Processing Exercise 3",
                  desc="""\
    test_validity_both:
        Verifies that both lists returned contain the correct output for the given input.
            EX: cleanSentenceTwoLists("Clean #Dirty") == (["Clean"], ["Dirty"])
    test_validity_clean:
        Verifies that the clean list returned contains the correct output for the given input.
            EX: cleanSentenceTwoLists("Clean #Dirty")[0] == ["Clean"]
    test_validity_dirty:
        Verifies that the dirty list returned contains the correct output for the given input.
            EX: cleanSentenceTwoLists("Clean #Dirty")[1] == ["Dirty"]
    test_removalOfCharFromDirty:
        Verifies that the special character is removed from the contents of the `dirty` list.
            EX: cleanSentenceTwoLists("#Dirty")[1] == ["Dirty"]
    test_emptyList_both:
        Verifies that an empty list is returned for both the `clean` and `dirty` list when expected.
            EX: cleanSentenceTwoLists("") == ([], [])
    test_emptyList_clean:
        Verifies that an empty list is returned for the `clean` list when expected.
            EX: cleanSentenceTwoLists("#Only #Dirty")[0] == []
    test_emptyList_dirty:
        Verifies that an empty list is returned for the `dirty` list when expected.
            EX: cleanSentenceTwoLists("Only clean")[1] == []"""),
]


def helpResponse(ALL_TESTS):
    '''
    To be invoked when the user asks for help with the program.
    Program quits with exit code 1
    '''
    print("""\
USAGE: $ python runTests.py [TESTS]

If [TESTS] is ommitted, the program will run all provided tests against the
exercises.

[TESTS] is an optional parameter of space separated integers. This is
provided only if the user wants to run specific tests. To run only tests
against exercises 0 and 3, one would input `python runTests.py 0 3`.

The following tests can be run:""")

    for test in ALL_TESTS:
        print("    " + test.argName + " : " + test.title)
    sys.exit(1)


if __name__ == '__main__':
    if '-h' in sys.argv or '--help' in sys.argv:
        helpResponse(ALL_TESTS)

    testsToRun = []
    if len(sys.argv) == 1:
        testsToRun = ALL_TESTS
    else:
        for test in ALL_TESTS:
            if test.argName in sys.argv[1:]:
                testsToRun.append(test)

    if len(testsToRun) == 0:
        helpResponse(ALL_TESTS)
    runTests(testsToRun)
