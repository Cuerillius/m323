from collections import defaultdict

class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        
        lost_once = []
        lost_never = []
        
        loss_map = {}
        for winner, loser in matches:
            loss_map.setdefault(winner, 0)
            loss_map[loser] = loss_map.get(loser, 0) + 1
            

        for player, loss in loss_map.items():
            match loss:
                case 1:
                    lost_once.append(player)
                case 0:
                    lost_never.append(player)
        return sorted(lost_never), sorted(lost_once)
    
    
print(Solution().findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))