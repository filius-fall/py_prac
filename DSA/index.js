
// // console.log('one')

// // var letters = []
// // var pal_name = "racecar"
// // var rname = ""

// // for (var i = 0;i < pal_name.length;i++){
// //     letters.push(pal_name[i]);

// // };

// // for (var j = 0;j<pal_name.length;j++){
// //     rname += letters.pop()


// // }

// // if (rname === pal_name){
// //     console.log('Its a palindrome')
// // }

// // else{
// //     console.log('Not palindrome')
// // }

// function mySet(){
//     var collection = [];

//     this.has = function(element){
//         return (collection.indexOf(element) !== -1)
//     }

//     this.values = function(){
//         return collection
//     }
//     this.add = function(element){
//         if(!this.has(element)){
//             collection.push(element);
//             return true
//         }
//         return false
//     }
//     this.remove = function(element){
//         if(this.has(element)){
//             index = collection.indexOf(element)
//             collection.slice(index,1)
//             return true
//         }
//         return false
//     }
// }


// var setA = new mySet()

// setA.add('two')
// setA.add('three')
// // console.log(setA)
// // console.log(setA.values())


// class Node{
//     constructor(data,left=null,right=null){
//         this.data = data;
//         this.left = left;
//         this.right = right
//     }


// }


// class BST{
//     constructor(root){
//         this.root = null
//     }

//     add(data){
//         const node = this.root
//         if(node == null){
//             this.root = new Node(data)
//             return
//         }
//         else{
//             const searchTree = function(node){
//                 if(data < node.data){
//                     if(node.left === null){
//                         node.left = new Node(data)

//                     }
//                     else if(node.left !== null){
//                         return searchTree(node.left)
//                     }
//                 }

//                 else if(data > node.data){
//                     if(node.right === null){
//                         node.right = new Node(data)
//                     }
//                     else if(node.right !== null){
//                         return searchTree(node.right)
//                     }
//                 }
//                 else{
//                     return null
//                 }
//             };
//             return searchTree(node)
           
//         }
//     }

//     findMin(){
//         let current = this.root
//         while(current.left !== null ){
//             if(current.left !== null){
//                 current = current.left
//             }
//         }
//         return current.data
//     }
//     findMax(){
//         let current = this.root
//         while(current.right !== null ){
//             if(current.right !== null){
//                 current = current.right
//             }
//         }
//         return current.data
//     }
//     findData(data){
//         let current = this.root
//         while(current !== data){
//             if(data < current.data){
//                 current = current.left
//             }
//             else if(data > current.data){
//                 current = current.right
//             }
//             if(current === null){
//                 return null
//             }
//             return current
//         }
//     }
// }


// const bst = new BST()

// bst.add(4)
// bst.add(3)
// bst.add(2)
// bst.add(5)
// bst.add(7)
// bst.add(1)
// bst.add(8)
// bst.add(10)
// console.log(bst.findMin())


// console.log('test')
// function test1(){
//     slfkalflaf;
//     gjcchuu ==== jhghj;
// }


var str = "1234"
var t = []
k = ""

let i = 0
let j = str.length - 1

// while(j >= 0){
//     t.push(str[j])

//     console.log(str)
//     j -= 1
// }

for(let i of str){
    k = i + k
}

console.log(k)

s = ""
s = "w" + s
s = "r" + s
s = "o" + s
console.log(s)


// console.log(str[0],str[1])

// str[1] = "s"
// console.log(str[1])