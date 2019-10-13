# 1) Create 5 variables
import numpy as np
import copy
seed = 10
STEPS = 100
sectionSize = 64
# Variables to operate on.
# 2) Choose a word to hash.
np.random.seed(seed)
HVars = [[np.random.randint(0, 2) for ii in range(sectionSize)] for i in range(5)]
# Now create encrypt method function.
rememberMe = []
for i in range(STEPS):
    rememberMe.append(np.random.randint(16))
results = []
dictionary = {chr(i): i for i in range(32, 127)}
def encrypt(words, dictionary):
    return [dictionary.get(i, "?") for i in list(words)]
def decrypt(words, dictionary):
    reverse = {i:j for j, i in dictionary.items()}
    return [reverse.get(i, "?") for i in list(words)]
def hash(inputStuff, HVars=HVars):
    wordHash = copy.deepcopy(inputStuff) # "".join([chr(np.random.randint(97, 97+25)) for i in range(64)]) for testing
    keepWordHash = copy.deepcopy(wordHash) # For later use
    # 4) Convert to binary. Yippee! This ain't gonna be fun w/o a library.
    # Okay. First we need to create a table.
    # 1 2 4 8 16 32 64
    wordHash = encrypt(wordHash, dictionary)
    def toPower(power, wordHash=wordHash, bitSize=8):
        maxChars = [power**i for i in range(bitSize-1, -1, -1)]
        # Then we go through that table and see how many times our value can evenly go into our table at pos i.
        finalAns = []
        for i in wordHash:
            # Convert to n-nary.
            leftOver = i
            newAns = []
            for ii in maxChars:
                try:
                    if (leftOver / ii) >= 1:
                        newAns.append(int((leftOver - leftOver % ii) / ii))
                        leftOver = leftOver % ii
                    else:
                        newAns.append(0)
                except:
                    newAns.append(0)
            finalAns += newAns
        return finalAns
    wordHash = toPower(2)
    wordHash += [1]
    # 6) Add 0s to make the size equal to 448 mod 512.
    # Basically, think about this like a clock w/ 512 hours.
    # At 512 the clock resets, and we have to get the rest equal to 448.
    addZeros = list(np.zeros((448 - (len(wordHash) % 512)), dtype=int))
    # print("Adding " + str(len(addZeros)) + " zeros to arr.")
    wordHash += addZeros
    # 7) Add original message length in binary to bottom of arr to fill up extra 64 bit place.
    wordHash += toPower(2, [len(keepWordHash)], 64)
    # 8) Break message up into x sections of sectionSize characters/bits.
    wordHash = np.array(wordHash).reshape(int(len(wordHash) / sectionSize), sectionSize)
    # 9) Now transform the 16 x 32 character bit words into 80 words using a step loop function.
    # It's gonna take four words from the first run from the loop(strings 1, 3, 9, and 14)
    # Then OR the words together and left rotate.
    def OR(*args):
        res = []
        for i in range(len(args[0])):
            res.append(1 if sum([ii[i] for ii in args]) else 0) #  == len(args)
        return res
    def AND(*args):
        res = []
        for i in range(len(args[0])):
            res.append(1 if sum([ii[i] for ii in args]) == len(args) else 0)
        return res
    def NOT(*args):
        res = []
        for i in range(len(args[0])):
            res.append(0 if sum([ii[i] for ii in args]) else 1)
        return res
    def SHIFT(arr):
        return arr[1:] + [0]
    results = []
    # We can't actually do 4 random words... So, if we want our results to be repeatable, we need to make sure wordHash follows our restrictions.
    # assert len(wordHash) == 16
    for i in range(STEPS):
        # ORs 4 random words.
        results.append(OR(*[wordHash[np.random.randint(len(wordHash))] for ii in range(4)])[1:] + [0])
    # return results
    # 10) Now run over those hVars from before and make SOME FIRE.
    # We're gonna take:
    """
    We'll go through both hvars and results.
    AND *CANNOT* be run first. Otherwise things go bonkers.
    """
    copyHVars = copy.deepcopy(HVars)
    # NOTE: We CANNOT change HVars. That changes the results of the hashing in the future.
    for i in range(1000):
        copyHVars[4] = OR(SHIFT(AND(OR(*results, HVars[0]))))
        copyHVars[3] = NOT(SHIFT(AND(NOT(*results, HVars[1]))))
        copyHVars[2] = OR(NOT(*results, SHIFT(SHIFT(AND(NOT(*results, HVars[2]))))))
        copyHVars[0] = SHIFT(OR(NOT(SHIFT(SHIFT(AND(SHIFT(OR(*results, HVars[3]))))))))
        copyHVars[1] = NOT(SHIFT(OR(*results, HVars[4])))
    def similarPower(power, arr):
        maxChars = [power**ii for ii in range(len(arr)-1, -1, -1)]
        return sum([arr[ii]*maxChars[ii] for ii in range(len(arr))])
    ans = ""
    for i in range(len(copyHVars)):
        ans += "".join(str(hex(similarPower(2, copyHVars[i]))).split("0x"))
    del copyHVars, wordHash
    return ans

def hashTag(input1):
    return str(hash(input1))