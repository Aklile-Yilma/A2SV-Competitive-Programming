class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        #key is content and value is (path, filename)        
        content_map = defaultdict(list)
        
        for path in paths:
            path = path.split(" ")
            folder = path[0]
            
            for string in path [1:]:
                #1.txt(abcd)  == [1, (abcd)]
                string = string.split(".txt")
                filename = string[0]
                content = string[1]
                content_map[content].append((folder, filename))
        
        duplicate_file_paths = []
        for key,value in content_map.items():
            #send only duplicate directories
            if len(value)>1:
                tmp = []
                for path, filename in value:
                    tmp.append(path+'/'+filename+'.txt')
                duplicate_file_paths.append(tmp)
        
        
        return duplicate_file_paths