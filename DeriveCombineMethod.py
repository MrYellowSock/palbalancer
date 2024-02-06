from Status import IPalStatus,IStatCombineMethod
class MaximumStatusCombineMethod(IStatCombineMethod) :
    def execute(self,arr: list[IPalStatus]) -> IPalStatus:
        result = None
        mx = -500
        for stat in arr:
            if stat.val > mx:
                mx = stat.val
                result = stat
        return result.clone()
