const fs = require('fs');
//var dataset = require('./dataset.json');
var dataset_2 = require('./dataset_2.json');

// if (dataset == dataset_2){
//     console.log("True")
// }
// else {
//     console.log("False")
// }

function list_to_tree(list) {
    var map = {}, node, roots = [], i;
    for (i = 0; i < list.length; i += 1) {
      map[list[i]['name']] = i; // initialize the map
      list[i]['children'] = []; // initialize the children
    }
    for (i = 0; i < list.length; i += 1) {
      node = list[i];
      if (node['parent'] != null) {
        // if you have dangling branches check that map[node.parentId] exists
        list[map[node['parent']['name']]]['children'].push(node);
      } else {
        roots.push(node);
      }
    }
    return roots;
}

var tree = list_to_tree(dataset_2['topics']);

var count = 0;

for (var i = 0 ; i < tree.length ; ++i){
    if (tree[i]['children'].length === 0){
        count++;
        //console.log(tree[i]['name']);
    }
}

console.log(count)

// const data = JSON.stringify(tree);

// fs.writeFile('topic_tree.json', data, (err) => {
//     if (err) {
//         throw err;
//     }
//     console.log("JSON data is saved.");
// });

// fs.readFile('topic_tree.json', 'utf-8', (err, data) => {
//     if (err) {
//         throw err;
//     }
//     Tree = JSON.parse(data.toString());
//     var count = 0;
//     console.log(count);
// });

