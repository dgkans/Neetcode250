class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        ins = set()
        outs = set()
        for a,b in paths:
            ins.add(a)
            outs.add(b)
        for city in outs:
            if city not in ins:
                return city
        