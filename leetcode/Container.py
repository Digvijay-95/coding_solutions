class Solution:
    def maxArea(self, height: List[int]) -> int:
        points=height
        f=0
        r=len(points)-1
        Max=0
        while(not(f==r)):
            width=int(abs(r-f))
            if points[f]<points[r]:
                height=int(points[f])
                area=height*width
                if area>Max:
                    Max=area
                f+=1
            else:
                height=int(points[r])
                area=height*width
                if area>Max:
                    Max=area
                r-=1
        return Max