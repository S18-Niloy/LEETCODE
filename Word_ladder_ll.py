from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        # Create a set for efficient word lookup
        wordSet = set(wordList)

        # Create a dictionary to store the parent of each word
        parentMap = defaultdict(list)

        # Create a dictionary to store the minimum distance from beginWord to each word
        distanceMap = defaultdict(lambda: float('inf'))
        distanceMap[beginWord] = 0

        # Initialize a queue and enqueue beginWord
        queue = deque()
        queue.append(beginWord)

        # Perform BFS
        while queue:
            word = queue.popleft()

            # Generate all possible next words
            for i in range(len(word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    nextWord = word[:i] + char + word[i+1:]

                    # Check if the next word is in wordSet and has not been visited before
                    if nextWord in wordSet and distanceMap[word] + 1 <= distanceMap[nextWord]:
                        if distanceMap[word] + 1 < distanceMap[nextWord]:
                            # Update the distance if it is shorter
                            distanceMap[nextWord] = distanceMap[word] + 1
                            queue.append(nextWord)
                        # Add the current word as the parent of the next word
                        parentMap[nextWord].append(word)

        # Recursive function to backtrack and construct all the shortest transformation sequences
        def backtrack(word, sequence):
            if word == beginWord:
                sequences.append(sequence[::-1])
            else:
                for parent in parentMap[word]:
                    backtrack(parent, sequence + [parent])

        # List to store all the transformation sequences
        sequences = []

        # Backtrack from endWord to beginWord to construct all the shortest transformation sequences
        backtrack(endWord, [endWord])

        return sequences
