from sortedcontainers import SortedDict

class Leaderboard:

    def __init__(self):
        self.scores = defaultdict(int) # {userID: score}
        self.sorted_scores = SortedDict() # {[-score]: count}        

    '''
    {player 
    
        2: 107,
        4: 51,
        3: 39,        
    }

    sorted_scores { 
        
        56: 1
        51: 1
        39: 1
    }
    '''

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.scores:
            prevScore = self.scores[playerId]
            self.scores[playerId] += score
            self.sorted_scores[-prevScore] -= 1
            if self.sorted_scores[-prevScore] == 0:
                del self.sorted_scores[-prevScore]
            newScore = -prevScore-score
            if newScore in self.sorted_scores:
                self.sorted_scores[newScore] +=1
            else:
                self.sorted_scores[newScore] =1
        else:
            # add score to player and sorted score
            self.scores[playerId] = score
            if -score in self.sorted_scores:
                self.sorted_scores[-score] += 1
            else:
                self.sorted_scores[-score] = 1

    def top(self, K: int) -> int:
        total = count = 0
        for score in self.sorted_scores:
            times = self.sorted_scores[score]
            score = -score
            for _ in range(times):
                total += score
                count += 1
                if count == K:
                    break
            if count == K:
                break
        return total
        

    def reset(self, playerId: int) -> None:
        prevScore = self.scores[playerId]
        self.sorted_scores[-prevScore] -= 1
        if self.sorted_scores[-prevScore] == 0:
            del self.sorted_scores[-prevScore]
        del self.scores[playerId]
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)