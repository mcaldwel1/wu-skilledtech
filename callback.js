function add(x, y) {
    return x + y;
}

function perim(callback, x, y) {
    return callback(x, y) + callback(x, y);
}

const result = perim(add, 2, 4); 
console.log(result);