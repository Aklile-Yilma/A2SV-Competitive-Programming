let buildings = [18, 14, 13, 16, 12]

function findBuildings(buildings) {
 let stack = [0];
  
  for (let i = 0; i < buildings.length; i++) {
    let currHeight = buildings[i]
    while (stack.length && currHeight >= buildings[stack[stack.length - 1]]) {
      stack.pop();
    }
    stack.push(i);
  }
  
  return stack;
};

console.log(findBuildings(buildings)) // [ 0, 3, 4 ]