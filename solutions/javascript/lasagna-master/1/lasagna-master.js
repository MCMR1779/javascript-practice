/// <reference path="./global.d.ts" />
// @ts-check

/**
 * Implement the functions needed to solve the exercise here.
 * Do not forget to export them so they are available for the
 * tests. Here an example of the syntax as reminder:
 *
 * export function yourFunction(...) {
 *   ...
 * }
 */
export function cookingStatus(remainingTime) {
  if (remainingTime === 0) {
    return 'Lasagna is done.';
  } else if (remainingTime > 0) {
    return 'Not done, please wait.';
  } else {
    return 'You forgot to set the timer.';
  }
}

export function preparationTime(layers, timeNeeded) {
  if (!timeNeeded) {
    return layers.length * 2;
  } else {
    return layers.length * timeNeeded;
  }
}

export function quantities (layers) {
  let numberOfNoodles = 0;
  let numberOfSauce = 0;
  for (let i = 0; i <layers.length ; i++) {
    if (layers[i] === 'noodles') {
      numberOfNoodles ++;
    } else if (layers[i] === 'sauce'){
      numberOfSauce++;
    }
  }
  return{
    noodles : numberOfNoodles * 50,
    sauce : numberOfSauce * 0.2
  }
}
export function addSecretIngredient(friendsList, myList) {
  myList.push(friendsList[friendsList.length -1]);
}

export function scaleRecipe(recipe, numberOfPortions) {
  let newRecipe = {...recipe};
  for(let ingredient in newRecipe){
   newRecipe[ingredient] = newRecipe[ingredient]/2 * numberOfPortions;
  }
  return newRecipe;
}