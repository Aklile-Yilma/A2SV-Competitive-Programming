class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        supplies = set(supplies)
        graph = defaultdict(list)
        indegree = defaultdict(int)
        order = []
        
        for idx in range(len(ingredients)):
            for ingredient in ingredients[idx]:
                if ingredient in supplies:
                    continue
                else:
                    graph[ingredient].append(recipes[idx])
                    indegree[recipes[idx]] += 1
                    
        q = deque()
        
        for recipe in recipes:
            if indegree[recipe] == 0:
                q.append(recipe)
                
        while q:
            recipe = q.popleft()
            order.append(recipe)
            for child in graph[recipe]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    q.append(child)
        
        return order