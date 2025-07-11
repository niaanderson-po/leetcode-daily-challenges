class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int: 
        meetings.sort()

        avalible = [i for i in range(n)] # n -> 0 1 2 3
        used = [] #(end_time, room_number)
        count = [0] * n #count[n] = meetings schedules for each room

        for start, end in meetings: 
            #Finish meetings that finsih at start time or before start
            while used and start >= used[0][0]:
                end_time, room = heapq.heappop(used)
                heapq.heappush(avalible, room)
            
            #no room is avalible
            if not avalible:
                end_time, room = heapq.heappop(used)
                end = end_time + (end - start) #updated duration
                heapq.heappush(avalible, room)
            
            #a room is avalible
            room = heapq.heappop(avalible)
            heapq.heappush(used, (end,room))
            count[room] += 1

        return count.index(max(count)) #first meeting room with the max count in case there is a tie