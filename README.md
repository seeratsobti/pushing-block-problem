# pushing_blocks

The Company Blocks Regular Inventing Usefulness of Something, better known as Brisa , build blocks, always the same size . One detail that stands out is the manner in which the blocks are stored in stock, after manufactured . They are formed by a row of cells . Withdrawal of a stock box is somewhat cluttered when , for choosing a cell at random and cut up some top block it. However , the storage medium is somewhat interesting: a conveyor located at the top of the stack straight rightmost stock is used . With this, it forms a queue with the new blocks . The belt right wheel to the left. So there is a vacant space in one of two cells, the block will be inserted in it, if there is not, it progresses to the following cells. Below is an example of insert blocks.

# Input

There will be several test cases . Each test case have three integers , M , P and F , indicating the rightmost stack height , the number of stacks of blocks and the size of the row of blocks to be inserted . Following this, M lines are read with P values , with values 1 , which is represented block, and 0 , representing which does not block. Next, a line is read with F values representing the queue with the new blocks . The last test case is represented by three zeros , and should not be processed.

# Output

For each test case , print the cells after the addition of new blocks. In some cases, a row of new blocks is more than sufficient for all the cells remain the same size. In this case , disregard the blocks that are left in the queue.

