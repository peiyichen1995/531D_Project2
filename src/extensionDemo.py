from Part3 import *
from Part2 import *
import tool

budgets0, queries0, bids0=tool.readData('../data/ds0.pkl')
budgets1, queries1, bids1=tool.readData('../data/ds1.pkl')
budgets2, queries2, bids2=tool.readData('../data/ds2.pkl')
budgets3, queries3, bids3=tool.readData('../data/ds3.pkl')


# #Below is the testing for extension 4
# ext4_0=extension4(budgets0, queries0, bids0, 0.01)
# ext4_1=extension4(budgets1, queries1, bids1, 0.01)
# ext4_2=extension4(budgets2, queries2, bids2, 0.01)
# ext4_3=extension4(budgets3, queries3, bids3, 0.01)

# print("ext4_0", ext4_0)
# print("ext4_1", ext4_1)
# print("ext4_2", ext4_2)
# print("ext4_3", ext4_3)

# print()

# print("greedyonline 0", greedyOnlineAdWord(budgets0, queries0, bids0)[1])
# print("greedyonline 1", greedyOnlineAdWord(budgets1, queries1, bids1)[1])
# print("greedyonline 2", greedyOnlineAdWord(budgets2, queries2, bids2)[1])
# print("greedyonline 3", greedyOnlineAdWord(budgets3, queries3, bids3)[1])

#Below is the testing for extension 2
e = 0.9
ext2_0=extension2_1(budgets0, queries0, bids0, e)
ext2_1=extension2_1(budgets1, queries1, bids1, e)
ext2_2=extension2_1(budgets2, queries2, bids2, e)
ext2_3=extension2_1(budgets3, queries3, bids3, e)

print("ext2_0", e, ext2_0[1])
print("ext2_1", e, ext2_1[1])
print("ext2_2", e, ext2_2[1])
print("ext2_3", e, ext2_3[1])

# print("ext2_0", ext2_0)
# print("ext2_1", ext2_1)
# print("ext2_2", ext2_2)
# print("ext2_3", ext2_3)

print()

print("LPonline 0", weightedgreedyOnlineAdWord(budgets0, queries0, bids0)[1])
print("LPonline 1", weightedgreedyOnlineAdWord(budgets1, queries1, bids1)[1])
print("LPonline 2", weightedgreedyOnlineAdWord(budgets2, queries2, bids2)[1])
print("LPonline 3", weightedgreedyOnlineAdWord(budgets3, queries3, bids3)[1])