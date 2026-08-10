let jsonStr = '{"classname": "Dev with Python", "students": 20, "is_completed": false, "reg_no": null}';

let obj = JSON.parse(jsonStr);
console.log(obj['classname']);
// console.log(obj.students);

// let myData = {
//     name: "Ashabi Wole",
//     gender: `Female`,
//     age: 29,
//     isEngaged: true,
//     comments: null,
//     friends: ['Julia', 'Kim'],

// };

// // console.log(JSON.stringify(myData));

// let jsonStr = '[{"name": "Ali", "grade": 85}, {"name": "Zara", "grade": 92}, {"name": "John", "grade": 78}]';

// let obj = JSON.parse(jsonStr);
// console.log(obj);

let names = ["Ade", "Bolu", "Charles"];

console.log(JSON.stringify(names));