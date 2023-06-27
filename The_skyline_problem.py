import heapq

class Solution:
    def getSkyline(self, buildings):
        # Combine the start and end points of each building and sort them by x-coordinate
        points = []
        for left, right, height in buildings:
            points.append((left, -height))  # Use negative height for the start point
            points.append((right, height))  # Use positive height for the end point
        points.sort()
        
        # Initialize a heap to store the heights of the active buildings
        active_heights = [0]
        
        # Initialize a variable to store the previous maximum height
        prev_height = 0
        
        # Initialize the resulting skyline
        skyline = []
        
        # Process each point
        for x, height in points:
            if height < 0:
                # Start of a building
                heapq.heappush(active_heights, height)
            else:
                # End of a building
                active_heights.remove(-height)
                heapq.heapify(active_heights)
            
            # Get the current maximum height
            current_height = -active_heights[0]
            
            # If the current maximum height is different from the previous height,
            # add a key point to the skyline
            if current_height != prev_height:
                skyline.append([x, current_height])
                prev_height = current_height
        
        return skyline
